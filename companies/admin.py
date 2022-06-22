from django.contrib import admin

# Register your models here.
from .models import Company, Review, Tag

admin.site.register(Company)
admin.site.register(Review)
admin.site.register(Tag)
