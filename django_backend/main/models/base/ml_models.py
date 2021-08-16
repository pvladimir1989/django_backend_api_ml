from django.db import models
from django.core.validators import FileExtensionValidator


class MLModels(models.Model):
    """ ML модели """
    # ml_model = models.BinaryField(verbose_name='ML модель')
    model_name = models.CharField(verbose_name='Название модели', max_length=255)
    model_file = models.FileField(verbose_name='ML Модель', upload_to='sentiment/prediction/models/%Y/%m/%d/',
                                  validators=[FileExtensionValidator(['pkl'])], help_text='Только pkl файлы')

    class Meta:
        verbose_name = "ML модель"
        verbose_name_plural = "ML модели"
