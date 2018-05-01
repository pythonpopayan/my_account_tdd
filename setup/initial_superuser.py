import os
import logging
from setup.utils import load_secrets
from django.contrib.auth.models import User
from accounts.models import transactionCategory

lg = logging.getLogger(__name__)

secrets = load_secrets(
    os.path.join(os.path.abspath(os.getcwd()), 'setup', 'initial_data.yaml')
    )

for person in secrets['ADMIN_ACCOUNTS']:
    try:
        user = User.objects.create_user(
            person['USERNAME'],
            password=person['PASSWORD']
            )
        user.is_superuser = True
        user.is_staff = True
        user.save()
        lg.debug('created {} admin'.format(person['USERNAME']))
    except Exception as e:
        lg.debug('admin user creation failed because of {}'.format(e))

for item in secrets['DEFAULT_CATEGORIES']:
    ct, _created = transactionCategory.objects.get_or_create(
        name=item['NAME'],
        income=item['INCOME'],
        description=item['DESCRIPTION'],
        )
    if _created:
        ct.save()
