from rest_framework.generics import (
    ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView)
from rest_framework.response import Response
from rest_framework.status import HTTP_204_NO_CONTENT
from crud.models import Employee
from .serializers import EmployeeSerializer


class IndexView(ListAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class CreateView(CreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


# We can also use RetriveUpdateAPIView for both DetailView and UpdateView


class DetailView(RetrieveAPIView):
    lookup_field = 'pk'
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class UpdateView(UpdateAPIView):
    lookup_field = 'pk'
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class DeleteView(DestroyAPIView):
    serializer_class = EmployeeSerializer

    def get_queryset(self):
        queryset = Employee.objects.filter(id=self.kwargs['pk'])
        return queryset

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response("Deleted successfully", status=HTTP_204_NO_CONTENT)
