from django.urls import path

from Tutorial import views

urlpatterns = [

    path('tutorial/', views.Tutorial, name='tutorial'),
    path('tutorialdetails/<slug:slug>/',views.Course,name='tutorialdetails'),
    path('coursecategory/<int:pk>', views.Category_course, name='coursecategory'),

]