"""urls specified"""
from django.urls import path
from .views import home_view


urlpatterns = [
    path('', home_view.home_view, name='home'),
]
