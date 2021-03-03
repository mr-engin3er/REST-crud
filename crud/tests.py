from json import dumps
from django.test import TestCase, Client
from django.urls import reverse
from rest_framework.test import APIRequestFactory
from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_204_NO_CONTENT, HTTP_404_NOT_FOUND, HTTP_400_BAD_REQUEST
from .models import Employee
from .api.serializers import EmployeeSerializer

# Using the standard RequestFactory API to create a form POST request
client = Client()

# test employee model


class EmployeeTest(TestCase):
    def setUp(self):
        Employee.objects.create(name="Dk", age=15, city="Bhilwara")
        Employee.objects.create(name="Dheeraj", age=25, city="Jaipur")

    def test_employee(self):
        dheeraj = Employee.objects.get(name="Dheeraj")
        dk = Employee.objects.get(name="Dk")
        self.assertEqual(
            dheeraj.city, "Jaipur"
        )
        self.assertEqual(
            dk.city, "Bhilwara"
        )

# test crud application all API's


class GetAllEmployeeTest(TestCase):
    def setUp(self):
        self.dk = Employee.objects.create(name="Dk", age=15, city="Bhilwara")
        self.dheeraj = Employee.objects.create(
            name="Dheeraj", age=25, city="Jaipur")
        self.valid_payload = {
            'name': 'dk',
            'age': 25,
            'city': 'Pune'
        }
        self.invalid_payload = {
            'name': '',
            'age': '25',
            'city': 'Pune'
        }

    # test index API
    def test_get_all_employee(self):
        response = client.get(reverse('crud:index'))
        employees = Employee.objects.all()
        serializer = EmployeeSerializer(employees, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, HTTP_200_OK)

    # test valid create API
    def test_create_valid_employee(self):
        response = client.post(reverse('crud:create'), data=dumps(
            self.valid_payload), content_type='application/json')
        employee = Employee.objects.last()
        serializer = EmployeeSerializer(employee)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, HTTP_201_CREATED)

    # test invalid create API
    def test_create_invalid_employee(self):
        response = client.post(reverse('crud:create'), data=dumps(
            self.invalid_payload), content_type='application/json')
        self.assertEqual(response.status_code, HTTP_400_BAD_REQUEST)

    # test get valid single API
    def test_get_valid_single_employee(self):
        response = client.get(
            reverse('crud:detail', kwargs={'pk': self.dk.id}))
        employee = Employee.objects.get(id=self.dk.id)
        serializer = EmployeeSerializer(employee)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, HTTP_200_OK)

    # test get invalid single API
    def test_get_invalid_single_employee(self):
        response = client.get(
            reverse('crud:detail', kwargs={'pk': 15}))
        self.assertEqual(response.status_code, HTTP_404_NOT_FOUND)

    # test update valid single API
    def test_update_valid_single_employee(self):
        response = client.put(reverse('crud:update', kwargs={'pk': self.dk.id}), data=dumps(
            self.valid_payload), content_type='application/json')
        employee = Employee.objects.get(id=self.dk.id)
        serializer = EmployeeSerializer(employee)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, HTTP_200_OK)

    # test update invalid single API
    def test_update_invalid_single_employee(self):
        response = client.put(reverse('crud:update', kwargs={'pk': self.dk.id}), data=dumps(
            self.invalid_payload), content_type='application/json')
        self.assertEqual(response.status_code, HTTP_400_BAD_REQUEST)

    # test delete valid single API
    def test_delete_valid_single_employee(self):
        response = client.delete(
            reverse('crud:delete', kwargs={'pk': self.dk.id}),)
        self.assertEqual(response.data, "Deleted successfully")
        self.assertEqual(response.status_code, HTTP_204_NO_CONTENT)

    # test delete invalid single API
    def test_delete_invalid_single_employee(self):
        response = client.delete(
            reverse('crud:delete', kwargs={'pk': 5}),)
        print(response.data.get('detail'))
        self.assertEqual(response.data.get('detail'), "Not found.")
        self.assertEqual(response.status_code, HTTP_404_NOT_FOUND)
