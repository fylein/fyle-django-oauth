from django.urls import path

from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='app=home'),
    path('login', views.HomeView.as_view(), name='app-login'),
    path('profile/', views.ProfileView.as_view(), name='app-profile'),

]
