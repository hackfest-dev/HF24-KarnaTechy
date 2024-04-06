from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('complaint/', views.complaint, name='complaints'),
    path('feedback/', views.feedback, name='feedback'),
    path('login/', views.login, name='login'),
]