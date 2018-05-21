from accounts.models import account, transaction
from accounts.models import transactionCategory
from persons.models import owner
from pprint import pprint


def calculate_balance(account_object):
    response = calculate_balance_report(account_object)
    return response['balance']


def calculate_balance_report(account_object):
    transaction_list = transaction.objects.filter(account=account_object)
    balance = 0
    expenses = 0
    incomes = 0
    for item in transaction_list:
        if item.category.income:
            balance += item.value
            incomes += item.value
        else:
            balance -= item.value
            expenses += item.value
    return {
        'balance': balance,
        'expenses': expenses,
        'incomes': incomes
        }


def calculate_homebank_report(user_obj):
    """
    calculate resume for homebank sync
    """
    report = {}
    q_list = transaction.objects.filter(account=account.objects.get(owner=user_obj))
    for item in q_list:
        if item.category.name in report:
            report[item.category.name]['value'] += item.value
            report[item.category.name]['detail'].append(item.description)
        else:
            report[item.category.name] = {'value': item.value, 'detail': [item.description,]}
    for item in report:
        report[item]['detail'] = ';'.join(report[item]['detail'])
    return report


def reset_user_account_transactions(user_obj, initial_value):
    """
    delete transactions of an user and sets an initial value for account
    """
    cuenta = account.objects.get(owner=user_obj)
    tx_category = transactionCategory.objects.get(name='transfer')
    q_list = transaction.objects.filter(account=cuenta)
    for item in q_list:
        item.delete()
    tx = transaction.objects.create(
        value=initial_value,
        category=tx_category,
        description='saldo inicial',
        account=cuenta,
    )
    tx.save()
