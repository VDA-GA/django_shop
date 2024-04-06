from django.urls import path
from django.views.decorators.cache import cache_page

from .views import ProductDetailView, ProductListView, ContactsView, ProductCreateView, ProductUpdateView, \
    ProductDeleteView, ModeratorProductUpdateView, CategoryListView, CategoryDeleteView, CategoryUpdateView, \
    CategoryCreateView, CategoryDetailView

app_name = 'Skystore'

urlpatterns = [
    path('', ProductListView.as_view(), name='product_list'),
    path('contacts/', ContactsView.as_view()),
    path('<int:pk>/', cache_page(60)(ProductDetailView.as_view()), name='product_page'),
    path('create_product/', ProductCreateView.as_view(), name='create_product'),
    path('<int:pk>/update_product', ProductUpdateView.as_view(), name='product_update'),
    path('<int:pk>/update_product/moderator', ModeratorProductUpdateView.as_view(), name='moderator_product_update'),
    path('<int:pk>/delete_product', ProductDeleteView.as_view(), name='product_delete'),
    path('category/', CategoryListView.as_view(), name='category_list'),
    path('create_category/', CategoryCreateView.as_view(), name='create_category'),
    path('update_category/<int:pk>', CategoryUpdateView.as_view(), name='category_update'),
    path('category/<int:pk>', CategoryDetailView.as_view(), name='category_page'),
    path('delete_category/<int:pk>', CategoryDeleteView.as_view(), name='category_delete'),
]
