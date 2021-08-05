from django.db import models
from .base_user import BaseUser


class HistoryOfUserActions(models.Model):
    profile = models.ForeignKey(BaseUser, on_delete=models.CASCADE, verbose_name="Профиль заемщика")
    # task_id
    # result_task
    # date какого числа запрос


class MLModels(models.Model):
    """ ML модели """
    ml_model = models.BinaryField(verbose_name='ML модель')
    model_name = models.CharField(verbose_name='Название модели', max_length=20)


class Subscriber(models.Model):
    """ Подписчик на новости"""

    email = models.EmailField()
    confirmed_email = models.EmailField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.email
