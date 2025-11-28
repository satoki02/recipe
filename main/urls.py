from django.contrib.auth import views as auth_views
from django.urls import path
from django.contrib.auth.views import LoginView
from . import views
from .forms import LoginForm 
from main.views import aboutus

app_name = 'main'

urlpatterns = [
    path('', views.index, name='index'),
    path('signup/', views.signup, name='signup'),
    path('contact/', views.contact, name='contact'),
    path('aboutus/', views.aboutus, name='aboutus'),
    path('privacy/', views.privacy, name='privacy'),
    path('terms/', views.terms, name='terms'),
    path('login/', auth_views.LoginView.as_view(template_name='main/login.html', authentication_form=LoginForm), name='login'),
    path('logout/', views.custom_logout_view, name='logout'),
]
