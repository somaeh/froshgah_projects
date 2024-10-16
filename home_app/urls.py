
from django.urls import path
from .import views

app_name = 'home_app'
urlpatterns =[
    
    path('', views.HomeView.as_view(), name="home"),
    path('category/<slug:category_slug>/', views.HomeView.as_view(), name="category_filter"),
    path('bucket/', views.BucketHome.as_view(), name="bucket"),
    path('delete_obj_bucket/<str:key>', views.DeleteBucketObjectView.as_view(), name="delete-obj-bucket"),
    path('download_obj_bucket/<str:key>', views.DownloadBucketObjectView.as_view(), name="download-obj-bucket"),
    path('<slug:slug>/', views.ProductDetailView.as_view(), name="product_detail"),
]