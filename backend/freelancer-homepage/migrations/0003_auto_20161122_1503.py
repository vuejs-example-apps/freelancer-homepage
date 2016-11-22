# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('freelancer-homepage', '0002_auto_20161121_1017'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='additionalservice',
            options={'verbose_name_plural': 'additional services', 'ordering': ('order',), 'verbose_name': 'additional service'},
        ),
        migrations.AlterModelOptions(
            name='customerreview',
            options={'verbose_name_plural': 'customer reviews', 'ordering': ('order',), 'verbose_name': 'customer review'},
        ),
        migrations.AlterModelOptions(
            name='portfolioimage',
            options={'verbose_name_plural': 'portfolio images', 'ordering': ('order',), 'verbose_name': 'portfolio image'},
        ),
        migrations.AlterModelOptions(
            name='portfoliowork',
            options={'verbose_name_plural': 'portfolio works', 'ordering': ('order',), 'verbose_name': 'portfolio work'},
        ),
        migrations.AlterModelOptions(
            name='service',
            options={'verbose_name_plural': 'services', 'ordering': ('order',), 'verbose_name': 'service'},
        ),
        migrations.AlterModelOptions(
            name='servicepackage',
            options={'verbose_name_plural': 'service packages', 'ordering': ('order',), 'verbose_name': 'service package'},
        ),
        migrations.AlterModelOptions(
            name='workstage',
            options={'verbose_name_plural': 'work stages', 'ordering': ('order',), 'verbose_name': 'work stage'},
        ),
    ]
