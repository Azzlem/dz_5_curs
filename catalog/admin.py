from django.contrib import admin

from catalog.models import Category, Product, Article, Version


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("pk", 'name')


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("pk", "name", "price", "category")
    list_filter = ("category",)
    search_fields = ("about",)


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ("pk", "title", "created_at")
    list_filter = ("published",)


@admin.register(Version)
class VersionAdmin(admin.ModelAdmin):
    list_display = ('name', 'product')
    list_filter = ('product',)
