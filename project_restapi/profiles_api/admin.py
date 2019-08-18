from django.contrib import admin
from .models import userprofile
# Register your models here.


class useradmin(admin.ModelAdmin):
    list_display=['name','is_staff','is_active','email']
    class Meta:
        model=userprofile



admin.site.register(userprofile,useradmin)
