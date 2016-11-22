# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('freelancer-homepage', '0003_auto_20161122_1503'),
    ]

    operations = [
        migrations.AddField(
            model_name='aboutme',
            name='title',
            field=models.CharField(default='Welcome!', verbose_name='title', max_length=255),
        ),
    ]
