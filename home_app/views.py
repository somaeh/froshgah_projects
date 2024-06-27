from django.shortcuts import render, get_object_or_404,redirect
from django.views import View
from.models import Product
from .import tasks
from django.contrib import messages


class HomeView(View):
    def get(self, request):
        products = Product.objects.filter(available=True) #فقط اون هایی را که موجود هستند بیاور
        return render(request, 'home_app/home.html', {'products':products}) 
    
    

class ProductDetailView(View):
    def get(self, request, slug):
        product = get_object_or_404(Product, slug=slug)
        return render(request, 'home_app/detail.html', {' product':product})
    
class BucketHome(View):
    
    template_name = 'home_app/bucket.html'
    
    
    def get(self, request):
        
        objects = tasks.all_bucket_objects_task()
        return render(request, self.template_name, {'objects':objects})
    
class DeleteBucketObjectView(View):
    def get(self, request, key):
        tasks.delete_object_task.delay(key)
        messages.success(request, 'delete object successfully', extra_tags='info')
        return redirect('home_app:bucket')
    
    
class DownloadBucketObjectView(View):
    
    def get(self, request, key):
        
        tasks.download_object_task.delay(key)
        messages.success(request, 'your download will be start soon', extra_tags='info')
        return redirect('home_app:bucket')
        
        
        
            
        