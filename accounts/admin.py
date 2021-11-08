from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
	add_form = CustomUserCreationForm
	form = CustomUserChangeForm
	model = CustomUser
	list_display = ['email', 'username', 'zipcode', 'is_staff', ] 
	fieldsets = UserAdmin.fieldsets + ( 
		('Additional Info', {'fields': ('zipcode',)}),
	)
	add_fieldsets = UserAdmin.add_fieldsets + ( 
		('Additional Info', {'fields': ('zipcode',)}),
	)


admin.site.register(CustomUser, CustomUserAdmin)