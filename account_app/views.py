from django.shortcuts import render,redirect
from django.views import View
from .forms import UserResitrationForm
import random
from utils import send_otp_code
from.models import OtpCode, User
from django.contrib import messages
from .forms import VeriFycodeForm, UserLoginForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin

class UserRegisterview(View):
    
    form_class = UserResitrationForm
    def get(self, request):
        if request.user.is_authenticated:
            return redirect('home_app:home')
    
        form = self.form_class
        return render(request, 'account_app/register.html', {'form':form})
        
       
    
    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            random_code = random.randint(1000, 9999)
            send_otp_code(form.cleaned_data['phone_number'], random_code)
            OtpCode.objects.create(phone_number=form.cleaned_data['phone_number'], code=random_code)
            request.session['user_registration_info']={
                'phone_number': form.cleaned_data['phone_number'],
                'email': form.cleaned_data['email'],
                'full_name': form.cleaned_data['full_name'],
                'password': form.cleaned_data['password'],
            }
            messages.success(request, 'we send you a code for you', extra_tags='success')
            return redirect('account_app:verify_code')
        return redirect('home_app:home')
    
class UserRegiesterVerifyCodeView(View):
    
    form_class = VeriFycodeForm
    
    def get(self, request):
        form = self.form_class
        return render(request, 'account_app/verify.html', {'form':form})
       
       
    
    def post(self, request):
        user_session = request.session['user_registration_info']
        code_instance = OtpCode.objects.get(phone_number=user_session['phone_number']) 
        form = self.form_class(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            if cd['code'] == code_instance.code:
                User.objects.create_user(user_session['phone_number'], user_session['email'],
                                    user_session['full_name'], user_session['password'])
                
                
                code_instance.delete()
                messages.success(request, 'you regiester successfully', extra_tags='success')
                return redirect('home_app:home')
            else:
                messages.error(request, 'your code is wrong', extra_tags='danger')
                return redirect('account_app:verify_code')
        return render(request, 'account_app/register.html', {'form':form})

class UserLoginView(View):
    
    form_class = UserLoginForm
    template_name = 'account_app/login.html'
    
    def get(self, request):
        form = self.form_class
        return render(request, self.template_name, {'form':form})
        
    
    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, phone=cd['phone'], password=cd['password'])
            if user is not None:
                login(request, user)
                messages.success(request, 'you logged successfully', extra_tags='success')
                return redirect('home_app:home')
            messages.error(request, 'phone or password is wrong', extra_tags='warning')
        return render(request, self.template_name, {'form':form})
            
            
class UserLogoutView(View, LoginRequiredMixin):
    def get(self ,request):
        logout(request)
        messages.success(request, 'user logout successfully', extra_tags='success')
        return redirect('home_app:home')