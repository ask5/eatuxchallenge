from django.contrib import admin
from eat.models import EarningSources, EarningsPagesMetaData


# Register your models here.
class EarningSourcesAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    fields = ('name',)


class EarningsPagesMetaDataAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'entity', 'page_type', 'value_field', 'frequency_field', 'next_page_name',
                    'previous_page_name')


admin.site.register(EarningSources, EarningSourcesAdmin)
admin.site.register(EarningsPagesMetaData, EarningsPagesMetaDataAdmin)