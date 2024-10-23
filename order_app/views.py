from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from .cart import Cart  # ایمپورت کردن سشن کارت
from home_app.models import Product
from .forms import CartAddForm, CouponeApplyForm
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from.models import Order, OrderItem, Coupon 
from .forms import CouponeApplyForm
import datetime
from django.contrib import messages
class CartView(View):
    def get(self, request):
        cart = Cart(request)  # ایجاد یک نمونه از کلاس Cart
        return render(request, 'order_app/cart.html', {'cart':cart})  # اضافه کردن سبد خرید به context

class CartAddView(PermissionRequiredMixin, View):
    permission_required = ('orders.add_order')
    def post(self, request, product_id):
        cart = Cart(request)  # ایجاد نمونه‌ای از کلاس Cart برای مدیریت سبد خرید از طریق سشن
        product = get_object_or_404(Product, id=product_id)  # دریافت محصول موردنظر بر اساس ID
        form = CartAddForm(request.POST)  # دریافت داده‌های POST از طریق فرم
        if form.is_valid():
            cd = form.cleaned_data
            # quantity = form.cleaned_data['quantity']  # دریافت مقدار quantity از فرم
            cart.add(product, form.cleaned_data['quantity'])  # افزودن محصول به سبد خرید
        return redirect('order_app:cart')  # هدایت به صفحه سبد خرید
       

class CartRemoveView(View):
    def get(self, request, product_id):
        cart = Cart(request)  # ایجاد نمونه‌ای از کلاس Cart
        product = get_object_or_404(Product, id=product_id)  # دریافت محصول موردنظر برای حذف
        cart.remove(product)  # حذف محصول از سبد خرید
        return redirect('order_app:cart')  # هدایت به صفحه سبد خرید
    
    
class OrderDetailView(View, LoginRequiredMixin):
    
    form_class = CouponeApplyForm
    
    def get(self, request, order_id):
        oreder = get_object_or_404(Order, id=order_id)
        return render(request, 'order_app/order.html', {'oreder': oreder, 'form':self.form_class})
    
class OrderCreateView(View, LoginRequiredMixin):
    def get(self, request):
        cart = Cart(request)
        order = Order.objects.create(user=request.user)
        for item in cart:
            OrderItem.objects.create(order=order, product=item['product'], price=item['price'], quantity=item['quantity'])
        cart.clear()
        return redirect('order_app: order_detail', order.id)
    
    
class CouponeApplyView(LoginRequiredMixin, View):
    
    form_class = CouponeApplyForm
    def post(self, request, order_id):
        
        now = datetime.datetime.now()  #تاریخ همین الان 
        form = self.form_class(request.POST)
        if form.is_valid():
            code = form.cleaned_data['code']
            try:
                coupon = Coupon.objects.get(code__exact=code, valid_from__lte=now, valid_to__get=now, active=True)
            except coupon.DoesNotExist:
                messages.error(request, 'this coupon does not exist', extra_tags='danger')
                return redirect('order_app:order_detail', order_id)
            order = Order.objects.get(id=order_id)  #سفارشی که کاربر می خواد و می گیریم
            order.discount = coupon.discount  
            order.save()
        return redirect('order_app:order_detail', order_id)
       
                
            