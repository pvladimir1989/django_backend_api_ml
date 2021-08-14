from django.db import models
from django.contrib.auth.models import User

MALE = "Male"
FEMALE = "Female"
MALE_OR_FEMALE = [(MALE, "Male"), (FEMALE, "Female")]

YES = "Yes"
NO = "No"
MARRIED_YES_NO_CHOICE = [(YES, "yes"), (NO, "no")]

URBAN = "Urban"
RURAL = "Rural"
PROPERTY_AREA_URBAN_RURAL = [(URBAN, "urban"), (RURAL, "rural")]

Y = "Y"
N = "N"
LOAN_STATUS_Y_N = [(Y, "Y"), (N, "N")]

SELF_EMPLOYED_YES_NO = [(YES, "Yes"), (NO, "No")]

GRADUATE = "Graduate"
NOT_GRADUATE = "Not Graduate"
EDUCATION_GRADUATE_NOT_GRADUATE = [(GRADUATE, "Graduate"), (NOT_GRADUATE, "Not Graduate")]


class BaseUser(models.Model):
    """ Признаки """
    # loan_id = models.CharField("Идентификатор кредита", max_length=12)

    gender = models.CharField(max_length=100, choices=MALE_OR_FEMALE)

    married = models.CharField(max_length=100, choices=MARRIED_YES_NO_CHOICE)

    dependents = models.CharField("Количество иждивенцов", max_length=12)

    education = models.CharField(max_length=100, choices=EDUCATION_GRADUATE_NOT_GRADUATE)

    self_employed = models.CharField(max_length=100, choices=SELF_EMPLOYED_YES_NO)

    applicant_income = models.FloatField(verbose_name="Доход", default=0)

    coapplicant_income = models.FloatField(verbose_name="Доход поручителя", default=0)

    loan_amount = models.FloatField(verbose_name="Размер кредита", default=0)

    loan_amount_term = models.FloatField(verbose_name="Срок займа в днях")

    credit_history = models.CharField(verbose_name="Кредитная история", max_length=12)

    property_area = models.CharField(max_length=100, choices=PROPERTY_AREA_URBAN_RURAL)

    loan_status = models.CharField(max_length=100, choices=LOAN_STATUS_Y_N)

    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Базовый пользователь", null=True)

    class Meta:
        verbose_name = "Профиль"
        verbose_name_plural = "Профили"

    # def save(self):
    #     result =  super.save()
    #     if result:
    #         raw = self.get_prepare_for_ml_data()
    #
    #         ml.feed(raw)
    #
    #     return  result
    #
    # def get_prepare_for_ml_data(self):
    #     return {
    #         'loan_status': LOAN_STATUS_Y_N.index(self.loan_status),
    #         'loan_amount' : self.loan_amount,
    #     }