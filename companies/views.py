from django.shortcuts import render
from django.http import HttpResponse

def companies(request):
    return render(request,'companies.html')

def company(request, pk):
    return HttpResponse("A company page will be here"+""+ str(pk))
