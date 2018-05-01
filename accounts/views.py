from django.views.generic.edit import CreateView
from accounts.models import transaction, account
from persons.models import owner
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required


@method_decorator(login_required, name='dispatch')
class transactionCreateView(CreateView):
    model = transaction
    fields = ['value', 'category', 'description']
    logged_customer = None
    success_url = '/persons/dashboard'

    def get(self, request, *args, **kwargs):
        self.logged_customer = owner.objects.get(user=request.user)
        return super(transactionCreateView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        self.logged_customer = owner.objects.get(user=request.user)
        return super(transactionCreateView, self).post(request, *args, **kwargs)

    def form_valid(self, form):
        user_account = account.objects.filter(owner=self.logged_customer).last()
        form.instance.account = user_account
        return super(transactionCreateView, self).form_valid(form)
