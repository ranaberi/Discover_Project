from django.urls import path
from . import views

urlpatterns = [
  path('companies/', views.companies, name="companies"),
  path('company/<str:pk>/', views.company, name="company"),
]