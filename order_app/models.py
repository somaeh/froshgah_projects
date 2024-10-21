from django.db import models
from home_app.models import Product
from django.contrib.auth import get_user_model
from django.core.validators import MinLengthValidator, MaxValueValidator


class Order(models.Model): 
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='orders')
    paid = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    discount = models.IntegerField(blank=True, null=True, default=None) #مقدار تخفیف است رو سفارش 
    
    class Meta:
        ordering = ('paid', '-updated')
        
    def __str__(self):
        return f'{self.user} - {str(self.id)}'
        
    def get_totall_price(self):
        total = sum(item.get_cost for item in self.items.all())   #همه سفارشات
        if self.discount :
            discount_price = (self.discount / 100 ) * total
            return int(total-discount_price)
        return total
        
    
    
    
    
class OrderItem(models.Model):  #محصولاتی که داخل اون سفارش بوده را مشخص می کنه 
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='order_items')
    price = models.IntegerField()
    quantity = models.IntegerField(default=1)
    
    
    def __str__(self):
        return str(self.id)
    
    def get_cost(self):  #قیمت کل محصول را انجام می دهد  
         return self.price * self.quantity
     
     
class Coupon(models.Model):
    code = models.CharField(max_length=30, unique=True)
    valid_from = models.DateTimeField()#زمان شروع کد تخفیف
    valid_to = models.DateTimeField()  #زمان پایان کد
    discount = models.IntegerField(validators=[MinLengthValidator(0), MaxValueValidator(90)])  #چند درصد تخفیف می دهید
    active = models.BooleanField(default=False)#آیا کد فعال هست یا نه
    
    def __str__(self):
        return self.code