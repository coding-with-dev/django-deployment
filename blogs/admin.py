from django.contrib import admin
from django.utils.html import format_html
from .models import Blog

# Register your models here.
@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ("title", "image_preview")

    def image_preview(self, obj):
        if obj.image_url:
            return format_html('<img src="{}" width="100" height="auto" style="border-radius:5px"/>', obj.image_url.url)
        return "(No Image)"

    image_preview.short_description = "Preview"