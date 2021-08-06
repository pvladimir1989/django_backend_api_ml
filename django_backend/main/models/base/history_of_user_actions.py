from django.db import models
from .base_user import BaseUser


# YES = "Yes"
# NO = "No"
# CELERY_RESPONSE = [(YES, "yes"), (NO, "no")]


class HistoryOfUserActions(models.Model):
    profile = models.ForeignKey(BaseUser, on_delete=models.CASCADE, verbose_name="Профиль заемщика")
    task_id = models.AutoField(primary_key=True)
    result_task = models.BooleanField(verbose_name="Ответ celery")
    date_of_request = models.DateTimeField(verbose_name="Дата создания", auto_now_add=True)
