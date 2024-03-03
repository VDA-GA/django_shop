from django.urls import path

from .views import ProductDetailView, ProductListView, ContactsView

app_name = 'Skystore'

urlpatterns = [
    path('', ProductListView.as_view()),
    path('contacts/', ContactsView.as_view()),
    path('<int:pk>/', ProductDetailView.as_view(), name='product_page'),
]