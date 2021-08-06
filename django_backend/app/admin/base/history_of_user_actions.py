from django.contrib import admin

from app.models.base import HistoryOfUserActions


class HistoryOfUserActionsAdmin(admin.ModelAdmin):
    list_display = ('profile', 'task_id', 'result_task', 'date_of_request')


admin.site.register(HistoryOfUserActions, HistoryOfUserActionsAdmin)
