from home_app.models import Product



CART_SESSION_ID = 'cart'

class Cart:
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get(CART_SESSION_ID)
        if not cart:
            cart = self.session[CART_SESSION_ID] = {}
        self.cart = cart 
        
    def __iter__(self): 
        product_id = self.cart.keys() 
        products = Product.objects.filter(id__in=product_id) 
        cart = self.cart.copy()
        for product in products:
            cart[str(product.id)]['product'] = product.name
            
        for item in cart.values():  #یعنی مقدارش و می خوایم
            item['total_price'] = int(item['price']) * item['quantity']
            yield item
            
            
    def __len__(self):
        return sum(item['quantity']for item in self.cart.values())
        
        
        
         
    def add(self, product, quantity): #خود محصول و تعداد را گرفتیم و ذخیره کردیم داخل سشن ها 
        product_id = str(product.id)
        
        if product_id not in self.cart:
            self.cart[product_id]= {'quantity':0, 'price':str(product.price)} 
        self.cart[product_id]['quantity'] += quantity
        self.save()
        
        # def save(self):
        #     self.session.modified = True
        
    def remove(self, product):   #ری مو کردن سشن 
        product_id = str(product.id) # اون محصولی که داره میاد آی دی اش را میگریم استرینگش می کنیم بعد 
        if product_id in self.cart: #اگر این پروداکت آی دی درون سبد خرید بود حذفش بکن
            del self.cart[product_id]
            self.save()
            
            
            
    def save(self):  #برای ذخیره کردن سشن ها بصورت دستی
        self.session.modified = True
    
    def get_total_price(self):  #قیمت کل را حساب می کند 
        
        return sum(int(item['price']) * item['quantity'] for item in self.cart.value())  #چند تا ابجکت ایتره بل را می گیرد و با هم جمع می کند
        
        
    def clear(self):
        del self.session[CART_SESSION_ID]
        self.save()