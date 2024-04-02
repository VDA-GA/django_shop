from django.urls import path

from .views import ProductDetailView, ProductListView, ContactsView, ProductCreateView, ProductUpdateView, \
    ProductDeleteView, ModeratorProductUpdateView

app_name = 'Skystore'

urlpatterns = [
    path('', ProductListView.as_view(), name='product_list'),
    path('contacts/', ContactsView.as_view()),
    path('<int:pk>/', ProductDetailView.as_view(), name='product_page'),
    path('create/', ProductCreateView.as_view(), name='create_product'),
    path('<int:pk>/update', ProductUpdateView.as_view(), name='product_update'),
    path('<int:pk>/update/moderator', ModeratorProductUpdateView.as_view(), name='moderator_product_update'),
    path('<int:pk>/delete', ProductDeleteView.as_view(), name='product_delete'),
]
