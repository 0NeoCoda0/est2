from django.db import models
from django.contrib.auth.models import User

class ProductCard(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название', unique=True)
    image = models.ImageField(upload_to='product_images/')
    description = models.TextField(null=True, blank=True, verbose_name='Описание')
    price = models.FloatField(null=True, blank=True, verbose_name='Цена')
    weight = models.FloatField(null=True, blank=True, verbose_name='Вес')
    caloryes = models.FloatField(null=True, blank=True, verbose_name='Калорийность')
    category = models.ForeignKey('Category', null=True, on_delete=models.PROTECT, verbose_name='Категория')
    food_type = models.ForeignKey('FoodType', null=True, on_delete=models.PROTECT, verbose_name='Тип', help_text='готовое или замороженное?')

    class Meta:
        verbose_name_plural = 'Карточки товаров'
        verbose_name = 'карточка товара'

    def __str__(self) -> str:
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Категория', unique=True)

    class Meta:
        verbose_name_plural = 'Категории товаров'
        verbose_name = 'категория товара'

    def __str__(self) -> str:
        return self.name

class FoodType(models.Model):
    name = models.CharField(max_length=100, verbose_name='Тип', unique=True)

    class Meta:
        verbose_name_plural = 'Типы товаров'
        verbose_name = 'тип товара'

    def __str__(self) -> str:
        return self.name
    
class UserCart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE) 
    items = models.ManyToManyField(ProductCard, through='CartItem')

    def add_to_cart(self, product):
        item, created = CartItem.objects.get_or_create(cart=self, product=product)
        if not created:
            item.quantity += 1
            item.save()
    
    def remove_from_cart(self, product):
        item = CartItem.objects.get(cart=self, product=product)
        item.delete()
    
    def get_total_price(self):
        items = self.cartitem_set.all()
        return sum(item.get_total_price() for item in items)

class CartItem(models.Model):
    cart = models.ForeignKey(UserCart, on_delete=models.CASCADE)
    product = models.ForeignKey(ProductCard, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def get_total_price(self):
        return self.product.price * self.quantity
    