from django.urls import path
from .views import add_property, property_details, PropertyUpdateView

app_name = 'property'

urlpatterns = [
    path('property/nuevo/', add_property, name='add'),
    path('property/<int:id>/', property_details, name='details'),
    path('property/actualizar/<int:pk>/', PropertyUpdateView.as_view(), name='update'),
]
