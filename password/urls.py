from django.urls import path
from password import views


urlpatterns = [
    path('', views.home, name='home'),
    path('generated_password/', views.password, name='password'),
    path('about/', views.about, name='about'),
]