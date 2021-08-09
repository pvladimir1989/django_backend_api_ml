from django.db import models


class Subscriber(models.Model):
    """ Подписчик на новости"""

    email = models.EmailField()
    confirmed_email = models.EmailField()
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Подписчик"
        verbose_name_plural = "Подписчики"

    def __str__(self) -> str:
        return self.email
