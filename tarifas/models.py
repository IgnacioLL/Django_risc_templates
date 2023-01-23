from django.db import models
from django.utils import timezone
import datetime
import pytz
from django.core.validators import MaxValueValidator, MinValueValidator
import uuid
from encargo.models import Encargo

# Create your models here.
class tarifas(models.Model):


	id_tarifas = models.UUIDField(primary_key=True, default=uuid.uuid1, editable=False)
	name = models.CharField(max_length=60)
	ID_encargo = models.ForeignKey(Encargo, on_delete=models.SET_DEFAULT, default="7b1f8f5a-7353-4683-b4ea-5c8e2c1f91bd")
	comision_prescriptor = models.IntegerField(blank=True,null=True)
	descuento_aplicar = models.FloatField(blank=True,null=True)
	valor_presupuestado = models.FloatField(blank=True,null=True)
	provision_de_fondos = models.FloatField(blank=True,null=True)
	importe_de_la_provision = models.FloatField(blank=True,null=True)
	referencia_catastral = models.CharField(max_length=80,blank=True,null=True)


	def __str__(self):
		return self.name