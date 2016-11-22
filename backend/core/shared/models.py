from django.db import models
from ordered_model.models import OrderedModel
from filebrowser.fields import FileBrowseField
from django.utils.translation import ugettext_lazy as _
from filebrowser.settings import VERSIONS as FILEBROWSER_VERSIONS


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


class ToDictMixin:

    def to_dict(self):
        opts = self._meta
        data = {}

        # initializing manually specified field grouping
        if self.TO_DICT_GROUPING:
            for prefix in self.TO_DICT_GROUPING:
                data[prefix] = {}

        # initializing prefixed field grouping
        if self.TO_DICT_GROUPING_PREFIXES:
            for prefix in self.TO_DICT_GROUPING_PREFIXES:
                data[prefix.replace('_', '')] = {}

        for f in opts.concrete_fields:
            # skipping explicitly specified fields
            if self.TO_DICT_SKIP_FIELDS:
                if f.name in self.TO_DICT_SKIP_FIELDS:
                    continue
            # handling prefixed fields grouping
            if self.TO_DICT_GROUPING_PREFIXES:
                p = self._get_grouping_prefix(f.name)
                if p:
                    data[p][f.name] = f.value_from_object(self)
                    continue
            # handling manually specified field grouping
            if self.TO_DICT_GROUPING:
                if f.name in self.TO_DICT_GROUPING.keys():
                    data[f.name] = f.value_from_object(self)
                    continue
            # handling images and other files
            if type(f) == FileBrowseField:
                data[f.name] = {}
                try:
                    file = f.value_from_object(self)
                    if file:
                        data[f.name]['original'] = file.url
                        for version in FILEBROWSER_VERSIONS:
                            data[f.name][version] = file.version_generate(version).url
                except FileNotFoundError:
                    data[f.name]['error'] = 'file not found'
            # handling default case
            else:
                data[f.name] = f.value_from_object(self)

        # cleanup for unused grouping
        for k in [k for k in data.keys() if data[k] == {}]:
            del data[k]

        # the mixin allows to redifine the related fields strategy
        if hasattr(self, '_to_dict_related_fields_strategy'):
            self._to_dict_related_fields_strategy(opts, data)
        else:
            self._default_related_fields_strategy(opts, data)

        # calling pre_finish_hook if exists
        if hasattr(self, '_to_dict_pre_finish_hook'):
            self._to_dict_pre_finish_hook(data)

        return data

    def _default_related_fields_strategy(self, opts, data):
        related_fields = [f for f in opts.get_all_related_objects() if f.is_relation and f.multiple]
        for rf in related_fields:
            data[rf.name] = [i.to_dict() for i in getattr(self, rf.name).all()]

    def _get_grouping_prefix(self, field_name):
        if not self.TO_DICT_GROUPING_PREFIXES:
            return None
        for group_prefix in self.TO_DICT_GROUPING_PREFIXES:
            if field_name.startswith(group_prefix):
                return group_prefix.replace('_', '')


# TODO: maybe extract to global settings, but still allow local in-class setting rewriting
class ToDictModel(ToDictMixin):
    TO_DICT_SKIP_FIELDS = ('id', 'created', 'modified', 'is_enabled', 'order')
    TO_DICT_GROUPING = {
        'contacts': ('tel', 'email', 'hyperlink')
    }
    TO_DICT_GROUPING_PREFIXES = ('price_',)

    def _default_related_fields_strategy(self, opts, data):
        related_fields = [f for f in opts.get_all_related_objects() if f.is_relation and f.multiple]
        for rf in related_fields:
            data[rf.name] = [i.to_dict() for i in getattr(self, rf.name).enabled()]