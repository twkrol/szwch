from pipes import Template
from django.urls import path
from django.views.generic import TemplateView

from . import views

urlpatterns = [
    path('', TemplateView.as_view(template_name="index.html")),
    path('resolve', views.resolve),
    path('shorten', views.shorten),
]
