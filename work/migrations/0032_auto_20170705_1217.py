# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-07-05 12:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('work', '0031_project_resource_type_selection'),
    ]

    operations = [
        migrations.AlterField(
            model_name='joinrequest',
            name='requested_username',
            field=models.CharField(help_text='If you have already an account in OCP, you can put the same username to have this project in the same account, or you can choose another username to have it separate.', max_length=32, verbose_name='Requested username'),
        ),
    ]
