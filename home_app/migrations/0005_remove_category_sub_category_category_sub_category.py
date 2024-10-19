# Generated by Django 5.0.6 on 2024-10-17 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home_app', '0004_alter_product_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='sub_category',
        ),
        migrations.AddField(
            model_name='category',
            name='sub_category',
            field=models.ManyToManyField(blank=True, null=True, related_name='scategory', to='home_app.category'),
        ),
    ]
