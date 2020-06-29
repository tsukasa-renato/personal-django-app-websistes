from django.shortcuts import render, get_object_or_404
from django.views.generic import View
from django.core.paginator import Paginator
from . import models


class Home(View):

    def get(self, *args, **kwargs):

        # SQL Queries
        # https://stackoverflow.com/questions/42621402/django-manager-first-vs-model-objects-all1
        websites = models.Websites.objects.filter(url=kwargs['url']).first()
        contacts = models.Contacts.objects.filter(websites=websites).first()
        icons = models.Icons.objects.filter(websites=websites).first()
        colors = models.Colors.objects.filter(websites=websites).first()
        banners = models.Banners.objects.filter(websites=websites).order_by('position')
        categories = models.Categories.objects.filter(websites=websites).order_by('position')
        products = models.Products.objects.filter(websites=websites, is_highlight=True).order_by('position')

        # https://docs.djangoproject.com/en/3.0/topics/pagination/
        paginator = Paginator(products, 8)
        page_number = self.request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        context = {
            'websites': websites,
            'contacts': contacts or '',
            'icons': icons or '',
            'colors': colors or '',
            'banners': banners or '',
            'categories': categories or '',
            'products': page_obj or '',
        }

        return render(self.request, 'website.html', context)
