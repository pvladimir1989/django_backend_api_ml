from django.contrib import admin


class HistoryOfUserActionsAdmin(admin.ModelAdmin):
    list_display = ('profile', 'task_id', 'result_task', 'date_of_request')
