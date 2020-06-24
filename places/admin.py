from django.contrib import admin
from django.utils.html import format_html


from .models import Place, Image

admin.site.register(Image)


class ImageInline(admin.TabularInline):
    model = Image
    fields = ['image', 'preview', 'position']
    readonly_fields = ['preview']

    def preview(self, obj):
        image_height = 200

        return format_html(f'<img src="{obj.image.url}" height={image_height} />')


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    inlines = [
        ImageInline,
    ]
