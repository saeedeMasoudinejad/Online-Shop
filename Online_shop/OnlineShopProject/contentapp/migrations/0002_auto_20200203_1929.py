# Generated by Django 2.2 on 2020-02-03 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contentapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='content',
            name='price',
            field=models.DecimalField(decimal_places=3, help_text='ریال', max_digits=10, verbose_name='قیمت'),
        ),
    ]
