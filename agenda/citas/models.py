from django.db import models

# Create your models here.
class macs(models.Model):
    direccionMac=models.CharField(max_length=20,default='0')
    estado=models.CharField(max_length=1,default='A')

 