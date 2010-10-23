from django.contrib import admin
from models import ShortenedUrl

class URLAdmin(admin.ModelAdmin):
    pass
    
admin.site.register(ShortenedUrl, URLAdmin)