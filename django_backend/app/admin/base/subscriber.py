from django.contrib import admin


class HistoryOfUserActionsAdmin(admin.ModelAdmin):
    list_display = ('email', 'confirmed_email', 'date')
