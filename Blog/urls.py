
from django.urls import path
from Blog import views

urlpatterns = [

    path('', views.Home, name='home'),
    path('404_page/', views.Page404, name='404_page'),
    path('category/<int:pk>', views.CategoryList, name='category'),
    path('details/<slug:slug>/', views.Details, name='details'),


]
