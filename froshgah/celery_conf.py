from celery import Celery

from datetime import timedelta


import os

os.environ.setdefault('DJANGO_SETTINGS_MODUEL', 'froshgah.settings')

celery_app = Celery('froshgah')
celery_app.autodiscover_tasks()
celery_app.conf.broker_url = 'amqp://rabbitmq'   #سیستم لوکال 
celery_app.conf.result_backend = 'rpc://'
celery_app.conf.task_serializer = 'json'
celery_app.conf.result_serializer = 'pickle'
celery_app.conf.accep_content = ['json', 'pickle']
celery_app.conf.result_expiers = timedelta(days=1)
celery_app.conf.task_always_eager = False
celery_app.conf.worker_prefetch_multiplier = 1