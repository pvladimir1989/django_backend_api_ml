from django.contrib import admin

from main.models.base import BaseUser


# @admin.register(BaseUser, BaseUserAdmin)
class BaseUserAdmin(admin.ModelAdmin):
    list_display = ('loan_id', 'gender', 'married', 'dependents', 'education',
                    'self_employed', 'applicant_income', 'coapplicant_income',
                    'loan_amount', 'loan_amount_term',
                    'credit_history', 'property_area', 'loan_status')
    list_display_links = ('loan_id',)
    search_fields = ('loan_id',)


admin.site.register(BaseUser, BaseUserAdmin)

