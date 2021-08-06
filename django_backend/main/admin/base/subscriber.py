from django.contrib import admin


class SubscriberAdmin(admin.ModelAdmin):
    list_display = ('email', 'confirmed_email', 'date')
