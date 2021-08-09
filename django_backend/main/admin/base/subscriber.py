from django.contrib import admin

from main.models.base import Subscriber


class SubscriberAdmin(admin.ModelAdmin):
    list_display = ('email', 'confirmed_email', 'date')


admin.site.register(Subscriber, SubscriberAdmin)
