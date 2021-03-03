from rest_framework.serializers import ModelSerializer
from crud.models import Employee


class EmployeeSerializer(ModelSerializer):
    class Meta:
        model = Employee
        fields = ['id', 'name', 'age', 'city']
