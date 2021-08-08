from django.contrib import admin


class MlModelsAdmin(admin.ModelAdmin):
    list_display = ('ml_model ', 'model_name')
