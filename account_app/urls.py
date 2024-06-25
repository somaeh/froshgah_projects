from django.urls import path
from .import views

app_name = 'account_app'
urlpatterns = [
    path('register/', views.UserRegisterview.as_view(), name="register"),
    path('verify/', views.UserRegiesterVerifyCodeView.as_view(), name="verify_code")
]