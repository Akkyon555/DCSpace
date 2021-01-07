from django.urls import path
from . import views
from django.contrib.auth.views import LoginView

app_name = 'home'

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('services/', views.services, name='services'),
    path('contact/', views.CreateContact.as_view(), name='contact'),
    path('signup/', views.signup, name='signup'),
    path('login/', LoginView.as_view(template_name='home/login.html'), name='login'),
]

