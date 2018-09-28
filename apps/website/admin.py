from django.contrib import admin
from .models import Paragraph, TextField


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


admin.site.register(Paragraph, ParagraphAdmin)
admin.site.register(TextField, TextFieldAdmin)
