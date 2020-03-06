# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.urls import reverse
from django.core.validators import MinLengthValidator
from django.conf import settings
from django.db.models.signals import post_save
import os

class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    subcategories = models.ForeignKey('self', blank=True, null=True, related_name="subcategories_list", on_delete=models.PROTECT)
    slug = models.SlugField(max_length=200, db_index=True, unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('planome:subcategory_list_by_category', args=[self.slug])

class SubCategory(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    category = models.ForeignKey(Category, blank=True, null=True, related_name="subcategory", on_delete=models.PROTECT)
    parent = models.ManyToManyField('self', blank=True, related_name="children")
    products = models.ForeignKey('self', blank=True, null=True, related_name="products_list", on_delete=models.PROTECT)
    slug = models.SlugField(max_length=200, db_index=True, unique=True)
    is_parent = models.BooleanField(default=False)

    class Meta:
        ordering = ('-is_parent', 'name',)
        verbose_name = 'subcategory'
        verbose_name_plural = 'subcategories'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('planome:product_list_by_subcategory', args=[self.slug])


def image_path(self, filename):
    ext = os.path.splitext(filename)[1]
    filePath = 'image/products/' + str(self.created.year) + '/' + str(self.created.month) + '/' + str(self.id) + '/' + 'main'+ ext
    if os.path.isfile(settings.MEDIA_ROOT + filePath):
        os.remove(settings.MEDIA_ROOT + filePath)
    return filePath


class Store(models.Model):
    name = models.CharField(max_length=100)
    products = models.ForeignKey('self', blank=True, null=True, related_name='products_in_store', on_delete=models.SET_DEFAULT, default=False)

    def __str__(self):
        return self.name


class Product(models.Model):
    subcategory = models.ForeignKey(SubCategory, null=True, related_name='product', on_delete=models.PROTECT, limit_choices_to={'is_parent': False})
    id = models.AutoField(primary_key=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True, allow_unicode=True)
    image = models.ImageField(upload_to=image_path, blank=True, null=True)
    description = models.TextField(blank=True)
    price = models.PositiveIntegerField()
    off_price = models.PositiveIntegerField(blank=True, null=True, default=False)
    store = models.ForeignKey(Store, blank=True, null=True, related_name='store', on_delete=models.SET_DEFAULT, default=False)
    stock = models.PositiveIntegerField()
    available = models.BooleanField(default=True)

    class Meta:
        ordering = ('-created',)
        index_together = (('id', 'slug'),)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('planome:product_detail', args=[self.id, self.slug])

def update_image(sender, instance, **kwargs):
    if len(str(instance.image).split('None')) == 2:
        os.makedirs(settings.MEDIA_ROOT + str(instance.image).split('None')[0] + str(instance.id))
        os.rename(settings.MEDIA_ROOT + str(instance.image), settings.MEDIA_ROOT + str(instance.image).split('None')[0] + str(instance.id) + str(instance.image).split('None')[1])
        os.rmdir(settings.MEDIA_ROOT + str(instance.image).split('None')[0] + 'None')
        instance.image = str(instance.image).split('None')[0] + str(instance.id) + str(instance.image).split('None')[1]
        instance.save()

post_save.connect(update_image, sender=Product)

class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    address = models.CharField(max_length=250)
    postal_code = models.CharField(max_length=20)
    phone_number = models.CharField(max_length=100)
    password = models.CharField(validators=[MinLengthValidator(6)], max_length=12)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return '{} {}'.format(self.first_name, self.last_name)
