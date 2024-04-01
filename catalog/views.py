from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin, PermissionRequiredMixin
from django.forms import inlineformset_factory
from django.urls import reverse_lazy, reverse
from django.views.generic import DetailView, ListView, TemplateView, CreateView, UpdateView, DeleteView

from catalog.forms import ProductForm, VersionForm, ModeratorProductForm
from catalog.models import Product, Version


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('Skystore:product_list')

    def form_valid(self, form):
        self.object = form.save()
        self.object.creator = self.request.user
        self.object.save()
        return super().form_valid(form)


class ProductUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Product

    def get_form_class(self):
        if self.request.user.has_perm('catalog.set_published'):
            return ModeratorProductForm
        else:
            return ProductForm

    def get_success_url(self):
        return reverse('Skystore:product_update', args=[self.kwargs.get('pk')])

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        VersionFormset = inlineformset_factory(Product, Version, form=VersionForm, extra=1)
        context_data['formset'] = VersionFormset()
        if self.request.method == 'POST':
            context_data['formset'] = VersionFormset(self.request.POST, instance=self.object)
        else:
            context_data['formset'] = VersionFormset(instance=self.object)
        return context_data

    def form_valid(self, form):
        formset = self.get_context_data()['formset']
        self.object = form.save()
        if formset.is_valid():
            formset.instance = self.object
            formset.save()
        return super().form_valid(form)

    def test_func(self):
        obj = self.get_object()
        return obj.creator == self.request.user or self.request.user.groups.filter(name='Moderators').exists()


class ProductListView(ListView):
    model = Product
    extra_context = {'title': 'Skystore'}

    def get_queryset(self):
        queryset = Product.objects.all()
        if self.request.user.groups.filter(name='Moderators').exists():
            return queryset
        return queryset.filter(status='PB')

    def get_context_data(self, *args, **kwargs):
        context_data = super().get_context_data(**kwargs)
        for product in context_data.get('object_list'):
            product.version = product.version_set.filter(is_current=True).first()
        return context_data


class ProductDetailView(DetailView):
    model = Product


class ProductDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Product
    permission_required = 'catalog.delete_product'
    success_url = reverse_lazy('Skystore:product_list')


class ContactsView(TemplateView):
    template_name = 'catalog/contacts.html'
