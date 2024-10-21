from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from .cart import Cart  # ایمپورت کردن سشن کارت
from home_app.models import Product
from .forms import CartAddForm

class CartView(View):
    def get(self, request):
        cart = Cart(request)  # ایجاد یک نمونه از کلاس Cart
        return render(request, 'order_app/cart.html',)  # اضافه کردن سبد خرید به context

class CartAddView(View):
    def post(self, request, product_id):
        cart = Cart(request)  # ایجاد نمونه‌ای از کلاس Cart برای مدیریت سبد خرید از طریق سشن
        product = get_object_or_404(Product, id=product_id)  # دریافت محصول موردنظر بر اساس ID
        form = CartAddForm(request.POST)  # دریافت داده‌های POST از طریق فرم
        if form.is_valid():
            quantity = form.cleaned_data['quantity']  # دریافت مقدار quantity از فرم
            cart.add(product=product, quantity=quantity)  # افزودن محصول به سبد خرید
            return redirect('order_app:cart')  # هدایت به صفحه سبد خرید
        return redirect('order_app:cart')  # در صورت نامعتبر بودن فرم نیز به سبد خرید هدایت می‌شود

class CartRemoveView(View):
    def get(self, request, product_id):
        cart = Cart(request)  # ایجاد نمونه‌ای از کلاس Cart
        product = get_object_or_404(Product, id=product_id)  # دریافت محصول موردنظر برای حذف
        cart.remove(product)  # حذف محصول از سبد خرید
        return redirect('order_app:cart')  # هدایت به صفحه سبد خرید
