from django.urls import path
from .views import index_view, login_view

app_name = 'users'

urlpatterns = [
    path('', index_view, name='index'),
    path('login/', login_view, name='login'),
]