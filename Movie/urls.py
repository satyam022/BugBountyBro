from django.urls import path

from Movie import views

urlpatterns = [

    path('movies/', views.Movies, name='movies'),
    path("moviesdetails/<slug:slug>/", views.Movie_details, name="moviesdetails"),
    path("moviescategory/<slug:slug>/", views.Movie_category, name="moviescategory")

]
