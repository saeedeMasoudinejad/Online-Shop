# Generated by Django 2.2 on 2020-02-04 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tradeapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='date',
            field=models.DateField(auto_now=True),
        ),
    ]
