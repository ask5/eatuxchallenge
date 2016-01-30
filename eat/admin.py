from django.contrib import admin
from eat.models import EarningSource, EarningsPage, EarningsWorkFlow


# Register your models here.
class EarningSourceAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    fields = ('name',)


class EarningsPageAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'entity', 'page_type', 'value_field', 'frequency_field')


class EarningsWorkFlowAdmin(admin.ModelAdmin):
    list_display = ('id', 'active', 'page', 'previous', 'next', 'skip_to')


admin.site.register(EarningSource, EarningSourceAdmin)
admin.site.register(EarningsPage, EarningsPageAdmin)
admin.site.register(EarningsWorkFlow, EarningsWorkFlowAdmin)