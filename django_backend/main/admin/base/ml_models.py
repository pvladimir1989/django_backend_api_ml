from django.contrib import admin
from main.models.base import MLModels


class MlModelsAdmin(admin.ModelAdmin):
    list_display = ('ml_model', 'model_name')


admin.site.register(MLModels, MlModelsAdmin)
