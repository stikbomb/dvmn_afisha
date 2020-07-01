from django.contrib import admin
from django.utils.html import format_html
from adminsortable2.admin import SortableInlineAdminMixin

from .models import Place, Image, models

admin.site.register(Image)


class ImageInline(SortableInlineAdminMixin, admin.TabularInline):
    model = Image
    fields = ['image', 'preview', 'position']
    readonly_fields = ['preview']
    # my_order = models.PositiveIntegerField(default=0, blank=False, null=False)
    #
    # class Meta(object):
    #     ordering = ['my_order']

    def preview(self, obj):
        image_height = 200
        return format_html(f'<img src="{obj.image.url}" height={image_height} />')


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    inlines = [
        ImageInline,
    ]


# @admin.register(Image)
# class ImageAdmin(SortableInlineAdminMixin, admin.ModelAdmin):
#     pass
