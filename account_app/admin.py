from django.contrib import admin

from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .forms import UserChangeForm, UserCreationsForm
from .models import User, OtpCode
from django.contrib.auth.models import Group

@admin.register(OtpCode)
class OtpCodeAdmin(admin.ModelAdmin):
    list_display = ('phone_number', 'code', 'created')



class UserAdmin(BaseUserAdmin):
    form = UserChangeForm
    add_form = UserCreationsForm
    
    
    list_display = ('full_name', 'phone_number', 'is_admin')
    list_filter = ('is_admin', )
    
    
    
    fieldsets = (
        (None, {'fields':('email', 'phone_number', 'full_name', 'password')}),
        ('permissions', {'fields':('is_active', 'is_admin', 'last_login','is_superuser', 'groups', 'user_permissions')}),
    )
    
    
    add_fieldsets = (
        
        (None, {'fields':('phone_number', 'email', 'full_name', 'password1', 'password2')}),
        
    )
    
    
    search_fields = ('email', 'full_name')
    
    ordering = ('full_name', )
    
    filter_horizontal = ('groups', 'user_permissions')
    
    
# admin.site.unregister(Group)
admin.site.register(User, UserAdmin)

    
    
    
