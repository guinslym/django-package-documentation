# -*- coding: utf-8 -*-

from django.conf import settings
from django.contrib import admin
from django.conf.urls.static import static
from django.conf.urls import url, include

from django.views.generic.base import TemplateView


urlpatterns = [
	
	#Main application
    url(r'^', TemplateView.as_view(template_name='helloworld/index.html')),

    #url(r'^', include('applications.helloworld.urls')),
    url(r'^robots.txt$', TemplateView.as_view(template_name="robots.txt", content_type="text/plain"), name="robots_file")

    url(r'^humans.txt$', TemplateView.as_view(template_name="humans.txt", content_type="text/plain"), name="humans_file")

    
]
