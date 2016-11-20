from django.contrib import admin
from ordered_model.admin import OrderedModelAdmin
from django.utils.translation import ugettext_lazy as _


def enable(modeladmin, request, queryset):
    queryset.update(is_enabled=True)
enable.short_description = _('Enable')


def disable(modeladmin, request, queryset):
    queryset.update(is_enabled=False)
disable.short_description = _('Disable')


class EnableDisableAdmin(admin.ModelAdmin):
    list_display = ('id', '__str__', 'is_enabled')
    list_display_links = ('id', '__str__')
    list_editable = ('is_enabled',)
    actions = (enable, disable)


class TimestampsAdmin(admin.ModelAdmin):
    list_display = ('id', '__str__', 'created', 'modified')
    list_display_links = ('id', '__str__')


class NameTimestampsEnabledAdmin(admin.ModelAdmin):
    list_display = ('id', '__str__', 'name', 'is_enabled', 'created', 'modified')
    list_display_links = ('id', '__str__')
    list_editable = ('name', 'is_enabled',)
    list_filter = ('is_enabled',)


class NameSlugTimestampsAdmin(admin.ModelAdmin):
    list_display = ('id', '__str__', 'name', 'slug', 'created', 'modified')
    list_display_links = ('id', '__str__')
    list_editable = ('name', 'slug')
