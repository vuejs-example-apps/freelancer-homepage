from django.db import models
from ordered_model.models import OrderedModel
from django.utils.translation import ugettext_lazy as _


class EnabledDisabledManager(models.Manager):
    def enabled(self):
        return self.get_queryset().filter(is_enabled=True)

    def disabled(self):
        return self.get_queryset().filter(is_enabled=False)


class IsEnabledModel(models.Model):
    class Meta:
        abstract = True

    objects = EnabledDisabledManager()

    is_enabled = models.BooleanField(default=True, verbose_name=_('is enabled'))


class TimestampsModel(models.Model):
    class Meta:
        abstract = True
        ordering = ('-modified',)

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)


class NameModel(models.Model):
    class Meta:
        abstract = True
        ordering = ('name',)

    name = models.CharField(verbose_name=_('name'), max_length=255)

    def __str__(self):
        return self.name


class SlugModel(models.Model):
    class Meta:
        abstract = True
        ordering = ('slug',)

    slug = models.SlugField(verbose_name=_('slug'), max_length=40)

    def __str__(self):
        return self.slug


class NameSlugModel(NameModel, SlugModel):
    class Meta:
        abstract = True
        ordering = ('slug',)

    def __str__(self):
        return self.name


class NameTimestampsModel(TimestampsModel, NameModel):
    class Meta:
        abstract = True
        ordering = ('-created',)


class NameSlugTimestampsModel(TimestampsModel, NameSlugModel):
    class Meta:
        abstract = True
        ordering = ('slug',)
