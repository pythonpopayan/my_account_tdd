from accounts.models import account, transaction


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
