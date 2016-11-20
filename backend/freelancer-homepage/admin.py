from django.contrib import admin
from solo.admin import SingletonModelAdmin
from core.shared.admin import EnableDisableAdmin
from django.utils.translation import ugettext_lazy as _
from filebrowser.settings import ADMIN_THUMBNAIL
from .models import ServicePackage, Service, AdditionalService, WorkStage, ServicesPageTexts,\
    PortfolioWork, Contacts, AboutMe, PortfolioImage, CustomerReview


class ServiceInline(admin.TabularInline):
    model = Service


class ServicePackageAdmin(EnableDisableAdmin):
    inlines = (ServiceInline,)


class AdditionalServiceAdmin(EnableDisableAdmin):
    pass


class CustomerReviewAdmin(EnableDisableAdmin):
    pass


class PortfolioImageInline(admin.TabularInline):
    model = PortfolioImage


class PortfolioWorkAdmin(EnableDisableAdmin):
    list_display = ('id', 'thumbnail', 'name', 'is_enabled', 'created', 'modified')
    list_filter = ('is_enabled',)
    list_display_links = ('id', 'thumbnail')

    def thumbnail(self, obj):
        if obj.cover_image and obj.cover_image.filetype == "Image":
            return '<img src="%(image_url)s" alt="%(alt_text)s"/>' % {
                'image_url': obj.cover_image.version_generate(ADMIN_THUMBNAIL).url,
                'alt_text': obj.name
            }
        else:
            return "<span>%s</span>" % _('cover photo not set')
    thumbnail.allow_tags = True
    thumbnail.short_description = _('thumbnail')

    inlines = (PortfolioImageInline,)


admin.site.register(CustomerReview, CustomerReviewAdmin)
admin.site.register(PortfolioWork, PortfolioWorkAdmin)
admin.site.register(ServicePackage, ServicePackageAdmin)
admin.site.register(AdditionalService, AdditionalServiceAdmin)
admin.site.register(Contacts, SingletonModelAdmin)
admin.site.register(AboutMe, SingletonModelAdmin)
admin.site.register(ServicesPageTexts, SingletonModelAdmin)
