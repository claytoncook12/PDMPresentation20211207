from django.contrib import admin

from .models import MP3Audio

# Register your models here.
@admin.register(MP3Audio)
class MP3AudioAdmin(admin.ModelAdmin):
    class Meta:
        verbose_name = 'MP3Audio'
        verbose_name_plural = 'MP3 Audio Files'
    
    list_display = ("id","ip_address","file_name")
