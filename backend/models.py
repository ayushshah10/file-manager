# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from django import forms
from django.core.validators import FileExtensionValidator
# from django.requests import request

ext = FileExtensionValidator(['pdf','mp4'])


class FileUpload(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,default = 'ayush')
    file  = models.FileField(upload_to='files/',validators=[ext],)
