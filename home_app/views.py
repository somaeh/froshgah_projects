from django.shortcuts import render, get_object_or_404
from django.views import View
from.models import Product


class HomeView(View):
    def get(self, request):
        product = Product.objects.filter(available=True) #فقط اون هایی را که موجود هستند بیاور
        return render(request, 'home_app/home.html', {'product':product}) 
    
    

class ProductDetailView(View):
    def get(self, request, slug):
        product = get_object_or_404(Product, slug=slug)
        return render(request, 'home_app/detail.html', {' product':product})