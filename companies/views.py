from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Company
from .forms import CompanyForm
from django.contrib.auth.decorators import login_required

def companies(request):
    companies = Company.objects.all()
    context = { 'companies' : companies}
    return render(request,'companies/companies.html', context)

def company(request, pk):
    companyObj = Company.objects.get(id = pk)
    return render(request,'companies/single-company.html', {'company': companyObj})

@login_required(login_url= "login")
def createCompany(request):
    form = CompanyForm()
    if request.method == 'POST':
        form = CompanyForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('companies')

    context = {'form': form}
    return render(request, "companies/company_form.html", context)

@login_required(login_url= "login")
def updateCompany(request, pk):
    company = Company.objects.get(id=pk)
    form = CompanyForm(instance= company)
    if request.method == 'POST':
        form = CompanyForm(request.POST, request.FILES, instance=company)
        if form.is_valid():
            form.save()
            return redirect('companies')
            
    context = {'form': form}
    return render(request, "companies/company_form.html", context)
    
@login_required(login_url= "login")
def deleteCompany(request, pk):
    company = Company.objects.get(id=pk)
    context = {'object': company}
    if request.method == 'POST':
        company.delete()
        return redirect('companies')
    
    return render(request, 'companies/delete_template.html', context)

