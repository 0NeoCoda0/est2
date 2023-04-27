from django.contrib import admin

from .models import ProductCard, Category, FoodType, UserCart

admin.site.register(ProductCard)
admin.site.register(Category)
admin.site.register(FoodType)
admin.site.register(UserCart)
# Register your models here.
