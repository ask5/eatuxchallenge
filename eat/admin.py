from django.contrib import admin
from eat.models import EarningSource, EarningsPage


# Register your models here.
class EarningSourceAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    fields = ('name',)


class EarningsPageAdmin(admin.ModelAdmin):
    list_display = ('id', 'entity', 'source', 'name', 'next', 'skip_to', 'page_type', 'value_field', 'frequency_field')
    ordering = ('entity', 'source', 'name')

admin.site.register(EarningSource, EarningSourceAdmin)
admin.site.register(EarningsPage, EarningsPageAdmin)
