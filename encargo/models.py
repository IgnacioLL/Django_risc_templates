import sys


from django.db import models
from django.utils import timezone
import datetime
import pytz
from django.core.validators import MaxValueValidator, MinValueValidator
import uuid
from prescriptor.models import Prescriptor
from clientes.models import Cliente



# Create your models here.
class Encargo(models.Model):



	Castellano = 'Castellano'
	Catalan = 'Catalan'
	Ingles = 'Ingles'
	Frances = 'Frances'
	OTRO = 'OTRO'
	opciones = [(Castellano, 'Castellano'),(Catalan, 'Catalan'), (Ingles, 'Ingles'),(Frances,'Frances'),(OTRO,'OTRO'),]

	numero_expediente = models.UUIDField(primary_key=True, default=uuid.uuid1, editable=False)
	name = models.CharField(max_length=100)
	timestamp = models.DateTimeField(auto_now_add = True)
	idioma_encargo = models.CharField(max_length=10, choices=opciones, default=Castellano,blank=True,null=True)
	via_encargo = models.CharField(max_length = 30,blank=True,null=True)
	ID_prescriptor = models.ForeignKey(Prescriptor, on_delete=models.SET_DEFAULT, default="7b1f8f5a-7353-4683-b4ea-5c8e2c1f91bd")
	ID_cliente = models.ForeignKey(Cliente, on_delete=models.SET_DEFAULT, default="7b1f8f5a-7353-4683-b4ea-5c8e2c1f91bd")

	objetivo_tasacion = models.CharField(max_length = 100,blank=True,null=True)
	numero_de_elementos = models.IntegerField(blank=True,null=True)

	documentacion = models.CharField(max_length = 500,blank=True,null=True)
	def __str__(self):
		return self.name