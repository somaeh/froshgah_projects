from celery import Celery

from datetime import timedelta


import os

os.environ.setdefault('DJANGO_SETTINGS_MODUEL', 'froshgah.settings') #نشان بدهد ستینگ های پروؤه شما کجاست 

celery_app = Celery('froshgah') #از کلاس سلری یک اینستنس می سازیم
celery_app.autodiscover_tasks() #تسک هایی که در پروژه دارید را فراخوانی می کندداخل تمام اپ ها را می گردد
celery_app.conf.broker_url = 'amqp://'   #سیستم لوکال 
celery_app.conf.result_backend = 'rpc://'
celery_app.conf.task_serializer = 'json'
celery_app.conf.result_serializer = 'pickle'
celery_app.conf.accep_content = ['json', 'pickle']
celery_app.conf.result_expiers = timedelta(days=1)
celery_app.conf.task_always_eager = False
celery_app.conf.worker_prefetch_multiplier = 1