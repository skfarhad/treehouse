from django.contrib import admin
from .models import Paragraph, TextField, ImageField


class ParagraphAdmin(admin.ModelAdmin):
    # readonly_fields = ['rating',]
    ordering = ('-timestamp',)
    list_filter = (
        'type',
    )
    search_fields = [
        'title',
    ]
    list_display = ('type',
                    'title',
                    'timestamp',
                    'text',
                    )


class TextFieldAdmin(admin.ModelAdmin):

    list_display = ('type',
                    'text',
                    )


class ImageFieldAdmin(admin.ModelAdmin):

    list_display = ('title',
                    'image_path',
                    )


admin.site.register(Paragraph, ParagraphAdmin)
admin.site.register(TextField, TextFieldAdmin)
admin.site.register(ImageField, ImageFieldAdmin)
