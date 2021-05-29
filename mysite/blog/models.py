from django.db import models
from django.shortcuts import reverse


class Company(models.Model):
    title = models.CharField(max_length=150, db_index=True, verbose_name='Название')
    body = models.TextField(blank=True, db_index=True, verbose_name='Описание')
    date_pub = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')
    date_update = models.DateTimeField(auto_now=True, verbose_name='Дата изменения')
    city = models.ManyToManyField('City', related_name='companies')
    subcategory = models.ManyToManyField('SubCategory', related_name='companies')
    is_published = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Компания'
        verbose_name_plural = 'Компании'
        ordering = ['is_published']

    def get_absolute_url(self):
        return reverse('company_detail_url', kwargs={'pk': self.pk})

    def __str__(self):
        return self.title


class City(models.Model):
    title = models.CharField(max_length=50, verbose_name='Город')

    class Meta:
        verbose_name = 'Город'
        verbose_name_plural = 'Города'
        ordering = ['title']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('city_detail_url', kwargs={'pk': self.pk})


class Category(models.Model):
    title = models.CharField(max_length=50, unique=True, verbose_name='Название категории')

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.title


class SubCategory(models.Model):
    title = models.CharField(max_length=50, unique=True, verbose_name='Название подкатегории')
    category = models.ForeignKey(Category, on_delete=models.PROTECT, null=True, verbose_name='Категория',
                                 related_name='subcategories')

    class Meta:
        verbose_name = 'Под-категории'
        verbose_name_plural = 'Под-категории'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('subcategory_detail_url', kwargs={'pk': self.pk})


