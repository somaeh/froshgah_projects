from django.urls import path
from .import views

app_name = 'account_app'
urlpatterns = [
    path('register/', views.UserRegisterview.as_view(), name="register"),
    path('verify/', views.UserRegiesterVerifyCodeView.as_view(), name="verify_code"),
    path('login/', views.UserLoginView.as_view(), name="login"),
    path('logout/', views.UserLogoutView.as_view(), name="logout"),
]