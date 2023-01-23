from django.db import models
from django.utils import timezone
import datetime
import pytz
from django.core.validators import MaxValueValidator, MinValueValidator
import uuid

# Create your models here.
class Cliente(models.Model):

	id_cliente = models.UUIDField(primary_key=True, default=uuid.uuid1, editable=False)
	name = models.CharField(max_length=60)
	empresa = models.CharField(max_length=50,blank=True,null=True)
	telefono = models.CharField(max_length=50,blank=True,null=True)
	correo_electronico = models.CharField(max_length=50,blank=True,null=True)
	movil = models.CharField(max_length=50,blank=True,null=True)


	def __str__(self):
		return self.name