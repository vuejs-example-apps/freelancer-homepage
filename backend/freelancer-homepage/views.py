from django.shortcuts import render
from django.http import JsonResponse
from .models import ServicePackage, PortfolioWork, Contacts, AboutMe,\
    ServicesPageTexts, AdditionalService, WorkStage, CustomerReview

def api_snapshot(request):
    return JsonResponse({
        'services': {
            'packages': [i.to_dict() for i in ServicePackage.objects.enabled()],
            'additional_services': [i.to_dict() for i in AdditionalService.objects.enabled()],
            'packages_global_note': ServicesPageTexts.get_solo().packages_global_note,
            'stages': [i.to_dict() for i in WorkStage.objects.enabled()],
        },
        'portfolio_works': [i.to_dict() for i in PortfolioWork.objects.enabled()],
        'texts': {
            'about_me': AboutMe.get_solo().to_dict(),
        },
        'contacts': Contacts.get_solo().to_dict(),
        'author': {
            'name': 'Grigoriy Beziuk',
            'hyperlink': 'http://vk.com/id85082'
        },
        'customer_reviews': [i.to_dict() for i in CustomerReview.objects.enabled()],
    })