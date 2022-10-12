# from __future__ import absolute_import, unicode_literals
import sys
from django.core.management import call_command
from aBlog.celery import app
from celery import shared_task

@shared_task
def add(x, y):
    return x + y

# @app.task(name='theBlog.tasks.bkup')
@shared_task
def bkup():
    sys.stdout = open('db.json', 'w')
    call_command('dumpdata', 'theBlog')
    