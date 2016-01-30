from django.contrib import admin
from eat.models import EarningSources, EarningsPage, EarningsWorkFlow


# Register your models here.
class EarningSourcesAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    fields = ('name',)


class EarningsPageAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'entity', 'page_type', 'value_field', 'frequency_field')


class EarningsWorkFlowAdmin(admin.ModelAdmin):
    list_display = ('id', 'active', 'page', 'skip_to_page')


admin.site.register(EarningSources, EarningSourcesAdmin)
admin.site.register(EarningsPage, EarningsPageAdmin)
admin.site.register(EarningsWorkFlow, EarningsWorkFlowAdmin)