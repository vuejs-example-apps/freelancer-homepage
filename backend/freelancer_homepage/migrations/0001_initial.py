# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import filebrowser.fields
import core.shared.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AboutMe',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('title', models.CharField(verbose_name='title', max_length=255, default='Welcome!')),
                ('image', filebrowser.fields.FileBrowseField(verbose_name='image', max_length=500)),
                ('text', models.TextField(verbose_name='text', default='Lorem ipsum, ladies and gentlemen!')),
            ],
            options={
                'verbose_name': 'about me',
            },
            bases=(models.Model, core.shared.models.ToDictModel),
        ),
        migrations.CreateModel(
            name='AdditionalService',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('order', models.PositiveIntegerField(db_index=True, editable=False)),
                ('is_enabled', models.BooleanField(verbose_name='is enabled', default=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(verbose_name='name', max_length=255)),
                ('description', models.TextField(blank=True, verbose_name='description', null=True)),
                ('price_base', models.PositiveIntegerField(blank=True, verbose_name='base price', null=True)),
                ('price_discount', models.PositiveIntegerField(blank=True, verbose_name='discount price', null=True)),
                ('price_currency', models.CharField(verbose_name='price currency', max_length=10)),
                ('price_unit', models.CharField(verbose_name='price unit', max_length=10)),
            ],
            options={
                'verbose_name': 'additional service',
                'ordering': ('order',),
                'verbose_name_plural': 'additional services',
            },
            bases=(models.Model, core.shared.models.ToDictModel),
        ),
        migrations.CreateModel(
            name='Contacts',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('tel', models.CharField(verbose_name='tel', max_length=255, default='555 55 55')),
                ('email', models.EmailField(verbose_name='email', max_length=255, default='me@example.com')),
                ('vk', models.URLField(verbose_name='VK', max_length=255, default='https://vk.com/id85082')),
                ('facebook', models.URLField(verbose_name='Facebook', max_length=255, default='https://www.facebook.com/grigory.bezyuk')),
                ('instagram', models.URLField(verbose_name='Instagram', max_length=255, default='https://www.instagram.com/gbezyuk/')),
            ],
            options={
                'verbose_name': 'contacts',
            },
        ),
        migrations.CreateModel(
            name='CustomerReview',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('order', models.PositiveIntegerField(db_index=True, editable=False)),
                ('is_enabled', models.BooleanField(verbose_name='is enabled', default=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('customer_name', models.CharField(verbose_name='name', max_length=255)),
                ('review_text', models.TextField(verbose_name='review text')),
                ('avatar', filebrowser.fields.FileBrowseField(verbose_name='image', max_length=500)),
                ('tel', models.CharField(blank=True, verbose_name='tel', max_length=255, null=True)),
                ('email', models.EmailField(blank=True, verbose_name='email', max_length=255, null=True)),
                ('hyperlink', models.URLField(blank=True, verbose_name='hyperlink', max_length=255, null=True)),
            ],
            options={
                'verbose_name': 'customer review',
                'ordering': ('order',),
                'verbose_name_plural': 'customer reviews',
            },
            bases=(models.Model, core.shared.models.ToDictModel),
        ),
        migrations.CreateModel(
            name='PortfolioImage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('order', models.PositiveIntegerField(db_index=True, editable=False)),
                ('is_enabled', models.BooleanField(verbose_name='is enabled', default=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(verbose_name='title', max_length=255)),
                ('image', filebrowser.fields.FileBrowseField(verbose_name='image', max_length=500)),
            ],
            options={
                'verbose_name': 'portfolio image',
                'ordering': ('order',),
                'verbose_name_plural': 'portfolio images',
            },
            bases=(models.Model, core.shared.models.ToDictModel),
        ),
        migrations.CreateModel(
            name='PortfolioWork',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('order', models.PositiveIntegerField(db_index=True, editable=False)),
                ('is_enabled', models.BooleanField(verbose_name='is enabled', default=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(verbose_name='name', max_length=255)),
                ('description', models.TextField(blank=True, verbose_name='description', null=True)),
                ('cover_image', filebrowser.fields.FileBrowseField(verbose_name='image', max_length=500)),
            ],
            options={
                'verbose_name': 'portfolio work',
                'ordering': ('order',),
                'verbose_name_plural': 'portfolio works',
            },
            bases=(models.Model, core.shared.models.ToDictModel),
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('order', models.PositiveIntegerField(db_index=True, editable=False)),
                ('is_enabled', models.BooleanField(verbose_name='is enabled', default=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(verbose_name='name', max_length=255)),
            ],
            options={
                'verbose_name': 'service',
                'ordering': ('order',),
                'verbose_name_plural': 'services',
            },
            bases=(models.Model, core.shared.models.ToDictModel),
        ),
        migrations.CreateModel(
            name='ServicePackage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('order', models.PositiveIntegerField(db_index=True, editable=False)),
                ('is_enabled', models.BooleanField(verbose_name='is enabled', default=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(verbose_name='name', max_length=255)),
                ('note', models.TextField(blank=True, verbose_name='note', null=True)),
                ('price_base', models.PositiveIntegerField(blank=True, verbose_name='base price', null=True)),
                ('price_discount', models.PositiveIntegerField(blank=True, verbose_name='discount price', null=True)),
                ('price_currency', models.CharField(verbose_name='price currency', max_length=10)),
                ('price_unit', models.CharField(verbose_name='price unit', max_length=10)),
            ],
            options={
                'verbose_name': 'service package',
                'ordering': ('order',),
                'verbose_name_plural': 'service packages',
            },
            bases=(models.Model, core.shared.models.ToDictModel),
        ),
        migrations.CreateModel(
            name='ServicesPageTexts',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('packages_global_note', models.TextField(verbose_name='text', default='And it will be gone too.')),
            ],
            options={
                'verbose_name': 'services page texts',
            },
            bases=(models.Model, core.shared.models.ToDictModel),
        ),
        migrations.CreateModel(
            name='WorkStage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('order', models.PositiveIntegerField(db_index=True, editable=False)),
                ('is_enabled', models.BooleanField(verbose_name='is enabled', default=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(verbose_name='name', max_length=255)),
                ('description', models.TextField(blank=True, verbose_name='description', null=True)),
            ],
            options={
                'verbose_name': 'work stage',
                'ordering': ('order',),
                'verbose_name_plural': 'work stages',
            },
            bases=(models.Model, core.shared.models.ToDictModel),
        ),
        migrations.AddField(
            model_name='service',
            name='package',
            field=models.ForeignKey(to='freelancer_homepage.ServicePackage', verbose_name='package', related_name='services'),
        ),
        migrations.AddField(
            model_name='portfolioimage',
            name='portfolio_work',
            field=models.ForeignKey(to='freelancer_homepage.PortfolioWork', verbose_name='portfolio_work', related_name='images'),
        ),
    ]
