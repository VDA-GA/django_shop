from django.urls import path
from . import views

app_name = 'Skystore'

urlpatterns = [
    path('', views.home),
    path('contacts/', views.contacts),
    path('<int:pk>/', views.product, name='product_page'),
]