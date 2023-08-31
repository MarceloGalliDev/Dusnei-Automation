"""urls specified"""
from django.urls import path
from .views import auth_view, dashboard_view, info_view


app_name = 'dash'


urlpatterns = [
    path('info/', info_view.info_view, name='info'),
    path('dashboard/', dashboard_view.dashboard_view, name='dashboard'),
    path('login/', auth_view.login_usuario, name='login'),
    path('logout/', auth_view.logout_usuario, name='logout'),
]
