from django.contrib import admin

# Register your models here.
from .models import Photo
class PhotoAdmin(admin.ModelAdmin):
    list_display = ['id','author','created','updated']
    raw_id_fields = ['author']
    list_filter = ['created','updated','author']
    search_fields = ['text','created','author__username'] #ForeignKey같은경우는 객체 검색하려면 __해야함
    ordering = ['-updated','-created']
admin.site.register(Photo,PhotoAdmin)