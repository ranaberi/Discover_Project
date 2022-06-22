from dataclasses import field
from django.forms import ModelForm 
from django.forms import widgets
from django import forms
from .models import Company

class CompanyForm(ModelForm):
  class Meta:
    model = Company
    fields = ['name', 'featured_image' , 'description', 'website_link', 'tags']
    widgets = {'tags': forms.CheckboxSelectMultiple()}

  def __init__(self, *args, **kwargs):
    super(CompanyForm,self).__init__(*args, **kwargs)

    for name,field in self.fields.items():
      field.widget.attrs.update({'class': 'input'})


    # self.fields['name'].widget.attrs.update({'class': 'input', 'placeholder': 'Add Title'})