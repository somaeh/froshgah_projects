from django.shortcuts import render, get_object_or_404,redirect
from django.views import View
from.models import Product, Category
from .import tasks
from django.contrib import messages
from django.contrib.auth.mixins import UserPassesTestMixin
from utils import IsAdminUserMixin
from order_app.forms import CartAddForm
from  order_app.forms import CartAddForm


class HomeView(View):
    def get(self, request, category_slug=None):
        products = Product.objects.filter(available=True) #فقط اون هایی را که موجود هستند بیاور
        categories = Category.objects.filter(is_sub=False)
        
        if category_slug:
            category = Category.objects.get(slug=category_slug)
            products = products.filter(category=category)
        return render(request, 'home_app/home.html', {'products':products, 'categories': categories }) 
    
    
    

class ProductDetailView(View):
    def get(self, request, slug):
        product = get_object_or_404(Product, slug=slug)
        form = CartAddForm()
        return render(request, 'home_app/detail.html', {'product':product, 'form':form})
    
class BucketHome(View, IsAdminUserMixin):
    
    template_name = 'home_app/bucket.html'
    
    
    def get(self, request):
        
        objects = tasks.all_bucket_objects_task()
        return render(request, self.template_name, {'objects':objects})
    
    
class DeleteBucketObjectView(View, IsAdminUserMixin):
    def get(self, request, key):
        tasks.delete_object_task.delay(key)
        messages.success(request, 'delete object successfully', extra_tags='info')
        return redirect('home_app:bucket')
    
    
    
class DownloadBucketObjectView(View, IsAdminUserMixin):
    
    def get(self, request, key):
        
        tasks.download_object_task.delay(key)
        messages.success(request, 'your download will be start soon', extra_tags='info')
        return redirect('home_app:bucket')
    
  
        
        
        
            
        