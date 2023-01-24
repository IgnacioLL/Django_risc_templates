from django.db import models
from django.utils import timezone
import datetime
import pytz
from django.core.validators import MaxValueValidator, MinValueValidator
import uuid

# Create your models here.
class tarifas(models.Model):


	id_tarifas = models.UUIDField(primary_key=True, default=uuid.uuid1, editable=False)
	name = models.CharField(max_length=60)
	comision_de_la_tarifa = models.FloatField()


	def __str__(self):
		return self.name