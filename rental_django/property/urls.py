from django.urls import path
from .views import add_property

app_name = 'property'

urlpatterns = [
    path('property/add/', add_property, name='add')
]
