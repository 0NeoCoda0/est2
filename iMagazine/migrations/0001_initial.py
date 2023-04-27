# Generated by Django 4.2 on 2023-04-11 18:44

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
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='Категория')),
            ],
        ),
        migrations.CreateModel(
            name='FoodType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='Тип')),
            ],
        ),
        migrations.CreateModel(
            name='ProductCard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='Название')),
                ('image', models.ImageField(upload_to='vkusSite/iMagazine/static/product_images')),
                ('desription', models.TextField(blank=True, null=True, verbose_name='Описание')),
                ('price', models.FloatField(blank=True, null=True, verbose_name='Цена')),
                ('weight', models.FloatField(blank=True, null=True, verbose_name='Вес')),
                ('caloryes', models.FloatField(blank=True, null=True, verbose_name='Калорийность')),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='iMagazine.category', verbose_name='Категория')),
                ('food_type', models.ForeignKey(help_text='готовое или замороженное?', null=True, on_delete=django.db.models.deletion.PROTECT, to='iMagazine.foodtype', verbose_name='Тип')),
            ],
        ),
    ]
