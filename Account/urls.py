from django.urls import path

from Account import views

urlpatterns = [
                  path('activate/<uidb64>/<token>', views.activate, name='activate'),
                  path('login/', views.Login, name='login'),
                  path('signup/', views.Signup, name='signup'),
                  path('logout/', views.Logout, name='logout'),

]