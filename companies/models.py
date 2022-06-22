from email.policy import default
from random import choices
from unittest.util import _MAX_LENGTH
from django.db import models
import uuid
from users.models import Profile

# Create your models here.
class Company(models.Model):
  # employer = models.ForeignKey(Profile, null= True, blank= True)
  name = models.CharField(max_length=200)
  description = models.TextField(null= True, blank= True)
  featured_image = models.ImageField(null= True, blank= True, default= "default.jpg")
  website_link = models.CharField(max_length= 2000, null= True, blank= True)
  tags = models.ManyToManyField('Tag', blank= True)
  vote_total = models.IntegerField(default=0, null = True, blank= True)
  vote_ratio = models.IntegerField(default=0, null = True, blank= True)
  created = models.DateTimeField(auto_now_add= True)
  id = models.UUIDField(default= uuid.uuid4, unique= True, primary_key= True, editable= False)

  def __str__(self):
     return self.name

class Review(models.Model):
  VOTE_TYPE = (
    ('up', 'Up Vote'),
    ('down', 'Down Vote')
  )
  #owner
  comapny= models.ForeignKey(Company, on_delete= models.CASCADE)
  body = models.TextField(null = True,blank = True)
  value = models.CharField(max_length = 200, choices = VOTE_TYPE)
  created = models.DateTimeField(auto_now_add= True)
  id = models.UUIDField(default= uuid.uuid4, unique= True, primary_key= True, editable= False)

  def __str__(self):
    return self.value

class Tag(models.Model):
  name= models.CharField(max_length= 200)
  created = models.DateTimeField(auto_now_add= True)
  id = models.UUIDField(default= uuid.uuid4, unique= True, primary_key= True, editable= False)

  def __str__(self):
    return self.name
     