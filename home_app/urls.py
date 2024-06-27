
from django.urls import path
from .import views

app_name = 'home_app'
urlpatterns =[
    
    path('', views.HomeView.as_view(), name="home"),
    path('bucket/', views.Buckethome.as_views(), name="bucket"),
    path('delete_obj_bucket/<str:key>', views.DeleteBucketObjectView.as_view(), name="delete_obj_bucket"),
    path('download_obj_bucket/<str:key>', views.DownloadBucketObjectView.as_view(), name="download_obj_bucket"),
    path('<slug:slug>/', views.ProductDetailView.as_view(), name="product_detail"),
]