# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.template.defaultfilters import striptags
from cms.models.pluginmodel import CMSPlugin


def get_results(request):
    data = request.GET.get('search', '')
    search_term = data.lower()

    page_instances = []
    content_objects = CMSPlugin.objects.filter(plugin_type='TextPlugin', djangocms_text_ckeditor_text__body__icontains=search_term)
    for obj in content_objects:
        if obj.page and not obj.page.publisher_is_draft:
            if search_term in striptags(obj.djangocms_text_ckeditor_text.body).lower():
                page_instances.append(obj.page)
    context = {
        'results': page_instances,
        'count': len(page_instances),
        'search_term': data,
    }
    return render(request, 'search.html', context)
