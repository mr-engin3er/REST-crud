from django.urls import path
from .api.views import (
    IndexView,
    CreateView,
    DetailView,
    UpdateView,
    DeleteView,
)

app_name = "crud"

urlpatterns = [
    path('', IndexView.as_view(), name="index"),
    path('create', CreateView.as_view(), name="create"),
    path('detail/<int:pk>/', DetailView.as_view(), name="detail"),
    path('update/<int:pk>/', UpdateView.as_view(), name="update"),
    path('delete/<int:pk>/', DeleteView.as_view(), name="delete"),
]
