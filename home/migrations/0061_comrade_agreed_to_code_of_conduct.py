# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-02-09 14:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0060_auto_20180208_2151'),
    ]

    operations = [
        migrations.AddField(
            model_name='comrade',
            name='agreed_to_code_of_conduct',
            field=models.BooleanField(default=False, verbose_name='I agree to the Code of Conduct'),
            preserve_default=False,
        ),
    ]
