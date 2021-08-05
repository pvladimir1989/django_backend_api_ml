from django.db import models
from django.contrib.auth.models import User


class Features(models.Model):
    features = models.ForeignKey("ProfileFeatures", on_delete=models.CASCADE, verbose_name='Список признаков')

    class Meta:
        verbose_name = 'список признаков'
        verbose_name_plural = 'списки признаков'


class Profile(User):
    phone_number = models.CharField(max_length=12, verbose_name='Номер', blank=True, null=True)
    profile_features = models.ForeignKey('ProfileFeatures', on_delete=models.CASCADE,
                                         verbose_name="Фичи (признаки) заемщика")

    class Meta:
        verbose_name = "профиль"
        verbose_name_plural = "профили"


class ProfileFeatures(models.Model):
    loan_id = models.CharField("Идентификатор кредита", max_length=12)

    male = "male"
    female = "female"
    male_or_female = [(male, "male"), (female, "female")]
    gender = models.CharField(max_length=2, choices=male_or_female)

    yes = "Yes"
    no = "No"
    married_yes_no_choice = [(yes, "yes"), (no, "no")]
    married = models.CharField(max_length=2, choices=married_yes_no_choice)

    dependents = models.BooleanField("Есть ли иждивенцы", default=False)

    graduate = "Graduate"
    not_graduate = "Not Graduate"
    education_graduate_not_graduate = [(graduate, "Graduate"), (not_graduate, "Not Graduate")]
    education = models.CharField(max_length=2, choices=education_graduate_not_graduate)

    self_employed_yes_no = [(yes, "Yes"), (no, "No")]
    self_employed = models.CharField(max_length=2, choices=self_employed_yes_no)

    applicant_income = models.PositiveIntegerField(verbose_name="Доход", default=0, max_length=10)

    coapplicant_income = models.PositiveIntegerField(verbose_name="Доход поручителя", default=0, max_length=10)

    loan_amount = models.PositiveIntegerField(verbose_name="Размер кредита", default=0, max_length=10)

    loan_amount_term = models.IntegerField(verbose_name="Срок займа в днях", max_length=5)

    credit_history = models.BooleanField(verbose_name="Кредитная история", default=False)

    urban = "urban"
    rural = "rural"
    property_area_urban_rural = [(urban, "urban"), (rural, "rural")]
    property_area = models.CharField(max_length=2, choices=property_area_urban_rural)

    y = "Y"
    n = "N"
    loan_status_y_n = [(y, "Y"), (n, "N")]
    loan_status = models.CharField(max_length=2, choices=married_yes_no_choice)

    class Meta:
        verbose_name = "признак"
        verbose_name_plural = "признаки"
