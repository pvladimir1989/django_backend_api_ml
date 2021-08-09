from django.db import models


class MLModels(models.Model):
    """ ML модели """
    ml_model = models.BinaryField(verbose_name='ML модель')
    model_name = models.CharField(verbose_name='Название модели', max_length=20)

    class Meta:
        verbose_name = "ML модель"
        verbose_name_plural = "ML модели"
