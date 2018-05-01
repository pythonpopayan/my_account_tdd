from django.db import models
from persons.models import owner


class account(models.Model):
    name = models.CharField(max_length=100)
    owner = models.ForeignKey(owner, on_delete=models.CASCADE)
    description = models.TextField(max_length=500)

    def __str__(self):
        return '{0.name} from {0.owner}'.format(self)


class transactionCategory(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    income = models.BooleanField(default=False)

    def __str__(self):
        return '{0.name}'.format(self)


class transaction(models.Model):
    value = models.FloatField()
    category = models.ForeignKey(transactionCategory, on_delete=models.CASCADE)
    description = models.TextField(max_length=500, null=True, blank=True)
    account = models.ForeignKey(account, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{0.value} {0.account} {0.date}'.format(self)
