from django.contrib import admin

# Register your models here.
from school_finder.models import School


@admin.register(School)
class SchoolAdmin(admin.ModelAdmin):
    list_display = ('id','name','address','created_at','modified_at')