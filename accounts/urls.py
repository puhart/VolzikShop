from django.urls import path
from . import views


app_name = 'accounts'

urlpatterns = [
    path('registration', views.registration, name='registration')
]