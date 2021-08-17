import json

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from main.models import BaseUser
from main.serializers import BaseUserSerializer

from django.contrib.auth.models import User


class BaseUserApiTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create(username="test_username")
        self.user1 = BaseUser.objects.create(gender="Male", married="No", dependents="0", education="Graduate",
                                             self_employed="No", applicant_income="5849",
                                             coapplicant_income="0.0", loan_amount="1.0", loan_amount_term="360.0",
                                             credit_history="1.0", property_area="Urban",
                                             loan_status="Y", user=self.user,
                                             )
        self.user2 = BaseUser.objects.create(gender="Male", married="No", dependents="1", education="Graduate",
                                             self_employed="No", applicant_income="5349",
                                             coapplicant_income="0.0", loan_amount="1.0", loan_amount_term="360.0",
                                             credit_history="1.0", property_area="Urban",
                                             loan_status="Y", user=self.user,
                                             )
        self.user3 = BaseUser.objects.create(gender="Male", married="No", dependents="1", education="Graduate",
                                             self_employed="No", applicant_income="5349",
                                             coapplicant_income="0.0", loan_amount="1.0", loan_amount_term="360.0",
                                             credit_history="1.0", property_area="Urban",
                                             loan_status="Y", user=self.user,
                                             )

    def test_get(self):
        # book_1 = Book.objects.create(name='Test book 1', price=25)
        # book_2 = Book.objects.create(name='Test book 2', price=55)
        url = reverse('baseuser-list')
        print(url)
        response = self.client.get(url)
        serializer_data = BaseUserSerializer([self.user1, self.user2, self.user3], many=True).data
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        # self.assertEqual(serializer_data, response.data)
        print(response.data)

    def test_get_filter(self):
        url = reverse('baseuser-list')
        response = self.client.get(url, data={'search': '5849'})
        serializer_data = BaseUserSerializer([self.user1, self.user3], many=True).data
        # print(serializer_data)
        print(response.status_code)
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        # self.assertEqual(serializer_data, response.data)

    def test_create(self):
        self.assertEqual(3, BaseUser.objects.all().count())
        url = reverse('baseuser-list')
        data = {
            "gender": "Male",
            "married": "No",
            "dependents": "0",
            "education": "Graduate",
            "self_employed": "No",
            "applicant_income": "5849",
            "coapplicant_income": "0.0",
            "loan_amount": "1.0",
            "loan_amount_term": "360.0",
            "credit_history": "1.0",
            "property_area": "Urban",
            "loan_status": "Y"
        }
        json_data = json.dumps(data)
        self.client.force_login(self.user)
        response = self.client.post(url, data=json_data, content_type='application/json')
        self.assertEqual(status.HTTP_201_CREATED, response.status_code)
        # self.assertEqual(serializer_data, response.data)
        self.assertEqual(4, BaseUser.objects.all().count())
        self.assertEqual(data['gender'], "Male")
        print(BaseUser.objects.last().user)

    def test_update(self):
        url = reverse('baseuser-detail', args=(self.user1.id,))
        data = {
            "gender": self.user1.gender,
            "married": self.user1.married,
            "dependents": "7",
            "education": "Graduate",
            "self_employed": "No",
            "applicant_income": "5849",
            "coapplicant_income": "0.0",
            "loan_amount": "1.0",
            "loan_amount_term": "360.0",
            "credit_history": "1.0",
            "property_area": "Urban",
            "loan_status": "Y"
        }
        json_data = json.dumps(data)
        self.client.force_login(self.user)
        response = self.client.put(url, data=json_data, content_type='application/json')
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.user1 = BaseUser.objects.get(id=self.user1.id)
        # self.user1.refresh_from_db()
        self.assertEqual("7", self.user1.dependents)
