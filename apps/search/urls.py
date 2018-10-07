# -*- coding: utf-8 -*-
from django.conf.urls import url
from .views import get_results


urlpatterns = [
    url(
        r'^get-search-results/$',
        view=get_results,
        name='search'),
]
