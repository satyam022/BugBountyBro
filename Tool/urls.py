from django.urls import path

from Tool import views


urlpatterns = [

    path('ipfinder/', views.IP_Finder, name='ipfinder'),


]