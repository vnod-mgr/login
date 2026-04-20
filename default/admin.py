from django.contrib import admin
from .models import check_form

@admin.register(check_form)
class CheckFormAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'ip_address', 'created_at']
