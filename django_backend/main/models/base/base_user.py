from django.db import models
from django.contrib.auth.models import User

MALE = "male"
FEMALE = "female"
MALE_OR_FEMALE = [(MALE, "male"), (FEMALE, "female")]

YES = "Yes"
NO = "No"
MARRIED_YES_NO_CHOICE = [(YES, "yes"), (NO, "no")]

URBAN = "urban"
RURAL = "rural"
PROPERTY_AREA_URBAN_RURAL = [(URBAN, "urban"), (RURAL, "rural")]

Y = "Y"
N = "N"
LOAN_STATUS_Y_N = [(Y, "Y"), (N, "N")]

SELF_EMPLOYED_YES_NO = [(YES, "Yes"), (NO, "No")]

GRADUATE = "Graduate"
NOT_GRADUATE = "Not Graduate"
EDUCATION_GRADUATE_NOT_GRADUATE = [(GRADUATE, "Graduate"), (NOT_GRADUATE, "Not Graduate")]


class BaseUser(User):
    """ Признаки """
    loan_id = models.CharField("Идентификатор кредита", max_length=12)

    gender = models.CharField(max_length=2, choices=MALE_OR_FEMALE)

    married = models.CharField(max_length=2, choices=MARRIED_YES_NO_CHOICE)

    dependents = models.BooleanField("Есть ли иждивенцы", default=False)

    education = models.CharField(max_length=2, choices=EDUCATION_GRADUATE_NOT_GRADUATE)

    self_employed = models.CharField(max_length=2, choices=SELF_EMPLOYED_YES_NO)

    applicant_income = models.PositiveIntegerField(verbose_name="Доход", default=0, max_length=10)

    coapplicant_income = models.PositiveIntegerField(verbose_name="Доход поручителя", default=0, max_length=10)

    loan_amount = models.PositiveIntegerField(verbose_name="Размер кредита", default=0, max_length=10)

    loan_amount_term = models.IntegerField(verbose_name="Срок займа в днях", max_length=5)

    credit_history = models.BooleanField(verbose_name="Кредитная история", default=False)

    property_area = models.CharField(max_length=2, choices=PROPERTY_AREA_URBAN_RURAL)

    loan_status = models.CharField(max_length=2, choices=MARRIED_YES_NO_CHOICE)


    class Meta:
        verbose_name = "Профиль"
        verbose_name_plural = "Профили"
