from django.urls import path
from catalog.apps import MainConfig

from catalog.views import ProductDetailView, contact, IndexListView, ArticleListView, ArticleDetailView, \
    ArticleCreateView, ArticleUpdateView, ArticleDeleteView, ProductCreateView, ProductUpdateView, ProductDeleteView

app_name = MainConfig.name

urlpatterns = [
    path('', IndexListView.as_view(), name='index'),
    path('contacts/', contact, name='contact'),
    path('<int:pk> /product/', ProductDetailView.as_view(), name='product'),
    path('create_product/', ProductCreateView.as_view(), name='create_product'),
    path('edit_product/<int:pk>', ProductUpdateView.as_view(), name='update_product'),
    path('delete/<int:pk>', ProductDeleteView.as_view(), name='delete_product'),

    path('article_list/', ArticleListView.as_view(), name='article_list'),
    path('<int:pk>/article/', ArticleDetailView.as_view(), name='article'),
    path('create/', ArticleCreateView.as_view(), name='create_article'),
    path('edit/<int:pk>', ArticleUpdateView.as_view(), name='update_article'),
    path('delete/<int:pk>', ArticleDeleteView.as_view(), name='delete_article'),


]
