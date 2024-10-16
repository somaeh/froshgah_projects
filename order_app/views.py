from django.shortcuts import render

from django.views import View



class CartView(View):
    def get(self, request):
        return render(request, 'order_app/cart.html')
    
    
    
    
class CartAddView(View):
    
    def post(self, request, product_id):
        
        pass
