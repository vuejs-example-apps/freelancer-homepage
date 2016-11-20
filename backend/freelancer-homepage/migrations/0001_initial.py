# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import filebrowser.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AboutMe',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('image', filebrowser.fields.FileBrowseField(max_length=500, verbose_name='image')),
                ('text', models.TextField(verbose_name='text', default='Lorem ipsum, ladies and gentlemen!')),
            ],
            options={
                'verbose_name': 'about me',
            },
        ),
        migrations.CreateModel(
            name='AdditionalService',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('is_enabled', models.BooleanField(verbose_name='is enabled', default=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=255, verbose_name='name')),
                ('description', models.TextField(verbose_name='description', null=True, blank=True)),
                ('price_base', models.PositiveIntegerField(verbose_name='base price', null=True, blank=True)),
                ('price_discount', models.PositiveIntegerField(verbose_name='discount price', null=True, blank=True)),
                ('price_currency', models.CharField(max_length=10, verbose_name='price currency')),
                ('price_unit', models.CharField(max_length=10, verbose_name='price unit')),
            ],
            options={
                'verbose_name': 'additional service',
                'verbose_name_plural': 'additional services',
            },
        ),
        migrations.CreateModel(
            name='Contacts',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('tel', models.CharField(max_length=255, verbose_name='tel', default='555 55 55')),
                ('email', models.EmailField(max_length=255, verbose_name='email', default='me@example.com')),
                ('vk', models.URLField(max_length=255, verbose_name='VK', default='https://vk.com/id85082')),
                ('facebook', models.URLField(max_length=255, verbose_name='Facebook', default='https://www.facebook.com/grigory.bezyuk')),
                ('instagram', models.URLField(max_length=255, verbose_name='Instagram', default='https://www.instagram.com/gbezyuk/')),
            ],
            options={
                'verbose_name': 'contacts',
            },
        ),
        migrations.CreateModel(
            name='CustomerReview',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('is_enabled', models.BooleanField(verbose_name='is enabled', default=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('customer_name', models.CharField(max_length=255, verbose_name='name')),
                ('review_text', models.TextField(verbose_name='review text')),
                ('avatar', filebrowser.fields.FileBrowseField(max_length=500, verbose_name='image')),
                ('tel', models.CharField(max_length=255, verbose_name='tel', null=True, blank=True)),
                ('email', models.EmailField(max_length=255, verbose_name='email', null=True, blank=True)),
                ('hyperlink', models.URLField(max_length=255, verbose_name='hyperlink', null=True, blank=True)),
            ],
            options={
                'verbose_name': 'customer review',
                'verbose_name_plural': 'customer reviews',
            },
        ),
        migrations.CreateModel(
            name='PortfolioImage',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('is_enabled', models.BooleanField(verbose_name='is enabled', default=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=255, verbose_name='title')),
                ('image', filebrowser.fields.FileBrowseField(max_length=500, verbose_name='image')),
            ],
            options={
                'verbose_name': 'portfolio image',
                'verbose_name_plural': 'portfolio images',
            },
        ),
        migrations.CreateModel(
            name='PortfolioWork',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('is_enabled', models.BooleanField(verbose_name='is enabled', default=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=255, verbose_name='name')),
                ('description', models.TextField(verbose_name='description', null=True, blank=True)),
                ('cover_image', filebrowser.fields.FileBrowseField(max_length=500, verbose_name='image')),
            ],
            options={
                'verbose_name': 'portfolio work',
                'verbose_name_plural': 'portfolio works',
            },
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('is_enabled', models.BooleanField(verbose_name='is enabled', default=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=255, verbose_name='name')),
            ],
            options={
                'verbose_name': 'service',
                'verbose_name_plural': 'services',
            },
        ),
        migrations.CreateModel(
            name='ServicePackage',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('is_enabled', models.BooleanField(verbose_name='is enabled', default=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=255, verbose_name='name')),
                ('note', models.TextField(verbose_name='note', null=True, blank=True)),
                ('price_base', models.PositiveIntegerField(verbose_name='base price', null=True, blank=True)),
                ('price_discount', models.PositiveIntegerField(verbose_name='discount price', null=True, blank=True)),
                ('price_currency', models.CharField(max_length=10, verbose_name='price currency')),
                ('price_unit', models.CharField(max_length=10, verbose_name='price unit')),
            ],
            options={
                'verbose_name': 'service package',
                'verbose_name_plural': 'service packages',
            },
        ),
        migrations.CreateModel(
            name='ServicesPageTexts',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('packages_global_note', models.TextField(verbose_name='text', default='And it will be gone too.')),
            ],
            options={
                'verbose_name': 'services page texts',
            },
        ),
        migrations.CreateModel(
            name='WorkStage',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('is_enabled', models.BooleanField(verbose_name='is enabled', default=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=255, verbose_name='name')),
                ('description', models.TextField(verbose_name='description', null=True, blank=True)),
            ],
            options={
                'verbose_name': 'work stage',
                'verbose_name_plural': 'work stages',
            },
        ),
        migrations.AddField(
            model_name='service',
            name='package',
            field=models.ForeignKey(verbose_name='package', related_name='services', to='freelancer-homepage.ServicePackage'),
        ),
        migrations.AddField(
            model_name='portfolioimage',
            name='portfolio_work',
            field=models.ForeignKey(verbose_name='portfolio_work', related_name='images', to='freelancer-homepage.PortfolioWork'),
        ),
    ]
