from django.db import models
from django.utils import timezone
import datetime
import pytz
from django.core.validators import MaxValueValidator, MinValueValidator
import uuid
from tarifas.models import tarifas

# Create your models here.
class Prescriptor(models.Model):

	id_prescriptor = models.UUIDField(primary_key=True, default=uuid.uuid1, editable=False)
	name = models.CharField(max_length=60)
	id_tarifas = models.ForeignKey(tarifas, on_delete=models.SET_DEFAULT, default="7b1f8f5a-7353-4683-b4ea-5c8e2c1f91bd")
	empresa = models.CharField(max_length=50,blank=True,null=True)
	telefono = models.CharField(max_length=50,blank=True,null=True)
	correo_electronico = models.CharField(max_length=50,blank=True,null=True)
	movil = models.CharField(max_length=50,blank=True,null=True)


	def __str__(self):
		return self.name