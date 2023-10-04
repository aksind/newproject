from django.contrib import admin
from .models import User1
# Register your models here.s
@admin.register(User1)
class UserAdmin(admin.ModelAdmin):
    list_display=('id', 'name', 'email', 'password')