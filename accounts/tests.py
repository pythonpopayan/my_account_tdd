from django.test import TestCase
from accounts.utils import calculate_balance, calculate_balance_report
from persons.models import owner
from accounts.models import transaction, transactionCategory, account
from django.contrib.auth.models import User


class accountingTestCase(TestCase):
    """
    unitary test for functionality
    """

    def setUp(self):
        # create user
        user = User.objects.create_user(
            'zebrahead',
            password='helloTomorrow2018'
            )
        user.save()
        self.user = owner.objects.create(
            name=user.username,
            user=user,
        )
        self.user.save()
        # create categories
        categories_stack = [
            {'name': 'job', 'description': 'get paid', 'income': True},
            {'name': 'food', 'description': 'get food', 'income': False}
        ]
        categories_dict = {}
        for item in categories_stack:
            c = transactionCategory.objects.create(**item)
            c.save()
            categories_dict[c.name] = c
        # create account
        self.user_account = account.objects.create(
            name='default',
            owner=self.user,
            description='default'
        )
        self.user_account.save()
        # create transactions for user
        transaction_stack = [
            {'value':60000,'category': categories_dict['job'], 'account': self.user_account},
            {'value':1500000,'category': categories_dict['job'], 'account': self.user_account},
            {'value':18000,'category': categories_dict['food'], 'account': self.user_account},
            {'value': 37000,'category': categories_dict['food'], 'account': self.user_account},
        ]
        for item in transaction_stack:
            t = transaction.objects.create(**item)
            t.save()
        # expected balance
        self.expected_balance = 1505000
        # expected balance report
        self.expected_balance_report = {
            'balance': self.expected_balance,
            'expenses': 55000,
            'incomes': 1560000
            }

    def test_balance(self):
        result = calculate_balance(self.user_account)
        self.assertEqual(result, self.expected_balance)

    def test_calculate_balance_report(self):
        result = calculate_balance_report(self.user_account)
        for key in result:
            self.assertEqual(result[key], self.expected_balance_report[key])

    def tearDown(self):
        pass
