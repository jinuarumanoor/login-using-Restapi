from django.contrib import admin
from .models import Account
from django.contrib.auth.admin import UserAdmin

# Register your models here.

# class Accountadmin(UserAdmin):
#     list_display = ('email', 'date_joined', 'is_admin', 'is_staff','is_block' )

#     filter_horizontal= ()
#     list_filter= ()
#     fieldsets=()


admin.site.register(Account)
