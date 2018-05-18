import os
from yaml import load

from django.views.generic import TemplateView, DetailView
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from persons.models import owner
from accounts.models import account, transaction, transactionCategory
from accounts.utils import calculate_balance_report


@method_decorator(login_required, name='dispatch')
class dashboardTemplateView(TemplateView):
    http_method_names = ['get']
    template_name = 'dashboard.html'

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        context['owner'] = owner.objects.get(user=request.user)
        context['account'] = account.objects.get(owner=context['owner'])
        context['balance_report'] = calculate_balance_report(context['account'])
        return self.render_to_response(context)

@method_decorator(login_required, name='dispatch')
class detailTemplateView(TemplateView):
    http_method_names = ['get']
    template_name = 'detail.html'

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        context['owner'] = owner.objects.get(user=request.user)
        context['account'] = account.objects.get(owner=context['owner'])
        balance_report = calculate_balance_report(context['account'])
        if kwargs['category'] == 'outcome':
            outcome_categories = transactionCategory.objects.filter(income=False)
            transactions = transaction.objects.filter(
            account=context['account'],
            category__in=outcome_categories
            ).order_by('-date')
            total = balance_report['expenses']
            label = 'outcomes'
        elif kwargs['category'] == 'income':
            income_categories = transactionCategory.objects.filter(income=True)
            transactions = transaction.objects.filter(
            account=context['account'],
            category__in=income_categories
            ).order_by('-date')
            total = balance_report['incomes']
            label = 'incomes'
        else:
            transactions = transaction.objects.filter(
            account=context['account'],
            ).order_by('-date')
            total = balance_report['balance']
            label = 'balance'
        context['transaction_list'] = transactions
        context['category_label'] = label
        context['category_total'] = total
        return self.render_to_response(context)


@method_decorator(login_required, name='dispatch')
class settingsTemplateView(TemplateView):
    http_method_names = ['get']
    template_name = 'settings.html'

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        context['owner'] = owner.objects.get(user=request.user)
        context['account'] = account.objects.get(owner=context['owner'])
        context['balance_report'] = calculate_balance_report(context['account'])
        # context['transactions'] = transaction.objects.filter(account=context['account'])
        return self.render_to_response(context)


def signupView(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            # create owner
            owner_obj, _created = owner.objects.get_or_create(name=username, user=user)
            if _created:
                owner_obj.save()
            # create account
            account_obj, _created = account.objects.get_or_create(
                name='{}_wallet'.format(username),
                owner=owner_obj,
                description='initial account of {}'.format(username)
                )
            if _created:
                account_obj.save()
            print('created all')
            return redirect('dashboard')
    else:
        if request.user.is_authenticated:
            return redirect('dashboard')
        else:
            form = UserCreationForm()
            context_file = os.path.join(os.path.dirname(__file__), 'landing_text.yaml')
            with open(context_file, 'r') as f:
                text = f.read()
                context = load(text)
            context['form'] = form
            return render(request, 'signup.html', context)
