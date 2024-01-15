from django.urls import path

from Imageworld import views

urlpatterns = [

    path('image/', views.Image_world, name='image'),


]