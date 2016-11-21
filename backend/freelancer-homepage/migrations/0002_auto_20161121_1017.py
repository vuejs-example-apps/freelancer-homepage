# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('freelancer-homepage', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='additionalservice',
            name='order',
            field=models.PositiveIntegerField(default=0, db_index=True, editable=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='customerreview',
            name='order',
            field=models.PositiveIntegerField(default=0, db_index=True, editable=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='portfolioimage',
            name='order',
            field=models.PositiveIntegerField(default=0, db_index=True, editable=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='portfoliowork',
            name='order',
            field=models.PositiveIntegerField(default=0, db_index=True, editable=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='service',
            name='order',
            field=models.PositiveIntegerField(default=0, db_index=True, editable=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='servicepackage',
            name='order',
            field=models.PositiveIntegerField(default=0, db_index=True, editable=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='workstage',
            name='order',
            field=models.PositiveIntegerField(default=0, db_index=True, editable=False),
            preserve_default=False,
        ),
    ]
