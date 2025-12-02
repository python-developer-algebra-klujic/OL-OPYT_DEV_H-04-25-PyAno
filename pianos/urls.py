from django.urls import path

from . import views


urlpatterns = [
    path('', views.list, name='pianos_list'),
    path('details', views.details, name='pianos_details')
]
