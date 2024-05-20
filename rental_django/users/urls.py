from django.urls import path
from .views import index_view, login_view, register_view, logout_view, dashboard_view

app_name = 'users'

urlpatterns = [
    path('', index_view, name='index'),
    path('entrar/', login_view, name='login'),
    path('registro/', register_view, name='register'),
    path('salir/', logout_view, name='logout'),
    path('dashboard/', dashboard_view, name='dashboard')
]