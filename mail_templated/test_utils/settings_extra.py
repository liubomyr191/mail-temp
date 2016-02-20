"""
Extra Django settings for the test project

This will be attached to the settings file that is generated by the
startproject command.
"""

DATABASES['default']['ENGINE'] = 'django.db.backends.sqlite3'
DATABASES['default']['NAME'] = 'db.sqlite3'

INSTALLED_APPS += ('mail_templated',)

# Required by Django == 1.7
from django.conf import global_settings
MIDDLEWARE_CLASSES = global_settings.MIDDLEWARE_CLASSES
