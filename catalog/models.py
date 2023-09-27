from datetime import datetime

from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Category(models.Model):
    name = models.CharField(max_length=50, verbose_name='Наименование')
    about = models.TextField(verbose_name='Описание')

    def __str__(self):
        return f"{self.name} {self.about}"

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class Product(models.Model):
    name = models.CharField(max_length=50, verbose_name='Наименование')
    about = models.TextField(verbose_name='Описание')
    image = models.ImageField(upload_to='media/', verbose_name='Превью', **NULLABLE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.IntegerField(verbose_name='Цена')

    def __str__(self):
        return f"{self.name} {self.price}"

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"


class Article(models.Model):
    title = models.CharField(max_length=150, verbose_name='Заголовок')
    image = models.ImageField(upload_to='media/', verbose_name='Превью', **NULLABLE)
    about = models.TextField(verbose_name='содержимое')
    created_at = models.DateTimeField(default=datetime.now, verbose_name='Дата создания')
    published = models.BooleanField(default=True, verbose_name='опубликовано')
    slug = models.CharField(max_length=30, verbose_name='slug', **NULLABLE)
    views_count = models.IntegerField(default=0, verbose_name='просмотры')

    def __str__(self):
        return f'{self.title} {self.created_at}'

    class Meta:
        verbose_name = 'статья'
        verbose_name_plural = 'статьи'


class Version(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    number = models.IntegerField(verbose_name='номер версии')
    name = models.CharField(max_length=150, verbose_name='название версии')
    in_active = models.BooleanField(default=True, verbose_name='опубликовано')

    def __str__(self):
        return f"{self.name} {self.number}"

    class Meta:
        verbose_name = 'версия'
        verbose_name_plural = 'версии'
