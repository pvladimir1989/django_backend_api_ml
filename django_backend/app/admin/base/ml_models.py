from django.contrib import admin


class HistoryOfUserActionsAdmin(admin.ModelAdmin):
    list_display = ('ml_model ', 'model_name')
