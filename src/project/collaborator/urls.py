from django.urls import path
from . import views


urlpatterns = [
    path('', views.collaborator, name='collaborator'),
]
