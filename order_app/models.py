from django.db import models
from home_app.models import Product
from django.contrib.auth import get_user_model


class Order(models.Model): 
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='orders')
    paid = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ('paid', '-updated')
        
    def __str__(self):
        return f'{self.user} - {self.id}'
        
    def get_totall_price(self):
        return sum(item.get_cost for item in self.items.all())   #همه سفارشات
        
    
    
    
    
class OrderItem(models.Model):  #محصولاتی که داخل اون سفارش بوده را مشخص می کنه 
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='order_items')
    price = models.IntegerField()
    quantity = models.IntegerField(default=1)
    
    
    def __str__(self):
        return self.id
    
    def get_cost(self):  #قیمت کل محصول را انجام می دهد  
         return self.price * self.quantity