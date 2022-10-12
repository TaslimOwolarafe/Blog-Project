import sys
from django.core.management import call_command
from aBlog.celery import app
# from celery.decorators import task
from celery.utils.log import get_task_logger
from .email import send_review_email
from celery import shared_task
logger = get_task_logger(__name__)

# @task(name="send_review_email_task")
@shared_task
def send_review_email_task(name, email, review):
    logger.info("Sent review email")
    return send_review_email(name, email, review)


@shared_task
def add(x,y):
    return x + y

# @app.task(name='theBlog.tasks.bkup')
# def bkup():
#     sys.stdout = open('db.json', 'w')
#     call_command('dumpdata', 'theBlog')