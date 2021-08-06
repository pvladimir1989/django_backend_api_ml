from django.contrib import admin


class BaseUserAdmin(admin.ModelAdmin):
    list_display = ('loan_id', 'gender', 'married', 'dependents', 'education',
                    'self_employed', 'applicant_income', 'coapplicant_income',
                    'loan_amount', 'loan_amount_term',
                    'credit_history', 'property_area', 'loan_status')
    # list_display_links = ('id', 'name')
    # search_fields = ('name',)
