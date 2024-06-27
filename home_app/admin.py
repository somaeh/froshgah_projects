from django.contrib import admin
from django.db import models


from home_app.models import Category, Product

admin.site.register(Category)
admin.site.register(Product)
