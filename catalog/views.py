from django.forms import inlineformset_factory
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.utils.text import slugify
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from catalog.forms import ArticleForm, ProductForm, VersionForm
from catalog.models import Product, Article, Version


class IndexListView(ListView):
    model = Product
    template_name = 'catalog/product_list.html'


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm

    def get_success_url(self):
        return reverse('catalog:product_list')


class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm

    def get_success_url(self):
        return reverse('catalog:product_list')

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        VersionFormset = inlineformset_factory(Product, Version, form=VersionForm, extra=1)
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


class ProductDetailView(DetailView):
    model = Product
    template_name = 'catalog/product_detail.html'


class ProductDeleteView(DeleteView):
    model = Product

    def get_success_url(self):
        return reverse('catalog:product_list')


class ArticleListView(ListView):
    model = Article


class ArticleDetailView(DetailView):
    model = Article

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views_count += 1
        self.object.save()
        return self.object


class ArticleCreateView(CreateView):
    model = Article
    form_class = ArticleForm

    def form_valid(self, form):
        if form.is_valid():
            new_content = form.save()
            new_content.slug = slugify(new_content.title)
            new_content.save()

        return super().form_valid(form)

    def get_success_url(self):
        return reverse('catalog:article_list')


class ArticleUpdateView(UpdateView):
    model = Article
    fields = ('title', 'about', 'image',)

    def form_valid(self, form):
        if form.is_valid():
            new_content = form.save()
            new_content.slug = slugify(new_content.title)
            new_content.save()

        return super().form_valid(form)

    def get_success_url(self):
        return reverse('catalog:article', args=[self.kwargs.get('pk')])


class ArticleDeleteView(DeleteView):
    model = Article

    def get_success_url(self):
        return reverse('catalog:article_list')


def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        print(name, email)

    return render(request, 'catalog/contact.html')
