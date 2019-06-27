# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-06-13 17:39
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=200)),
                ('slug', models.SlugField(max_length=200, unique=True)),
                ('subcategories', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='subcategories_list', to='planome.Category')),
            ],
            options={
                'ordering': ('name',),
                'verbose_name': 'category',
                'verbose_name_plural': 'categories',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(db_index=True, max_length=200)),
                ('slug', models.CharField(db_index=True, max_length=200)),
                ('image', models.ImageField(blank=True, upload_to='products/%Y/%m/%d')),
                ('description', models.TextField(blank=True)),
                ('price', models.PositiveIntegerField()),
                ('stock', models.PositiveIntegerField()),
                ('available', models.BooleanField(default=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ('-created',),
            },
        ),
        migrations.CreateModel(
            name='SubCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=200)),
                ('slug', models.SlugField(max_length=200, unique=True)),
                ('is_parent', models.BooleanField(default=False)),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='subcategory', to='planome.Category')),
                ('parent', models.ManyToManyField(blank=True, related_name='_subcategory_parent_+', to='planome.SubCategory')),
                ('products', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='products_list', to='planome.SubCategory')),
            ],
            options={
                'ordering': ('name',),
                'verbose_name': 'subcategory',
                'verbose_name_plural': 'subcategories',
            },
        ),
        migrations.AddField(
            model_name='product',
            name='subcategory',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='product', to='planome.SubCategory'),
        ),
        migrations.AlterIndexTogether(
            name='product',
            index_together=set([('id', 'slug')]),
        ),
    ]
