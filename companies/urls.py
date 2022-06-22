from unicodedata import name
from django.urls import path
from . import views

urlpatterns = [
  path('', views.companies, name="companies"),
  path('company/<str:pk>/', views.company, name="company"),
  path("create-company/", views.createCompany, name="create-company"),
  path("update-company/<str:pk>/", views.updateCompany, name= "update-company"),
  path("delete-company/<str:pk>/", views.deleteCompany, name= "delete-company"),
]