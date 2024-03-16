from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView, TemplateView, CreateView

from catalog.forms import ProductForm
from catalog.models import Product


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('product:list')


class ProductListView(ListView):
    model = Product
    extra_context = {'title': 'Skystore'}


class ProductDetailView(DetailView):
    model = Product




class ContactsView(TemplateView):
    template_name = 'catalog/contacts.html'
