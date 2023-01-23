from django.shortcuts import render
from django.db import models
from django.http import HttpResponse
import django_tables2 as tables
import datetime
import pytz
from django_tables2.config import RequestConfig
import itertools
from django.db import connection
from djqscsv import render_to_csv_response
import psycopg2
import uuid




##### Modify with your database here #####
db = psycopg2.connect(
    host="0.0.0.0",
    database="expedientes",
    user="admin",
    password="RiscValor331")


cursor = db.cursor()



class news(models.Model):
    numero_expediente = models.UUIDField(primary_key=True, default=uuid.uuid1, editable=False)
    name = models.CharField(max_length = 100,blank=True,null=True)
    timestamp = models.DateTimeField(auto_now_add = True)
    idioma_encargo = models.CharField(max_length=10)
    via_encargo = models.CharField(max_length = 30,blank=True,null=True)
    ID_prescriptor_id = models.CharField(max_length = 100,blank=True,null=True)
    ID_cliente_id = models.CharField(max_length = 100,blank=True,null=True)
    objetivo_tasacion = models.CharField(max_length = 100,blank=True,null=True)
    documentacion = models.CharField(max_length = 500,blank=True,null=True)

    class Meta:
        db_table = "encargo_encargo"
        managed = False


class newsTable(tables.Table):
    numero_expediente = tables.Column(verbose_name="ID Expediente")
    name = tables.Column(verbose_name="Descripcion")
    timestamp = tables.Column(verbose_name="Timestamp")
    idioma_encargo = tables.Column(verbose_name="Idioma Encargo")
    via_encargo = tables.Column(verbose_name="Via Encargo")
    ID_prescriptor_id = tables.Column(verbose_name="ID prescriptor")
    ID_cliente_id = tables.Column(verbose_name="ID cliente")
    objetivo_tasacion = tables.Column(verbose_name="Objetivo tasacion")
    documentacion = tables.Column(verbose_name="Documentacion")


    class Meta:
        model = news
        attrs = {
            "class": "info-table",
        }
        fields = ( "numero_expediente","name","timestamp","idioma_encargo","via_encargo","ID_prescriptor_id","ID_cliente_id","objetivo_tasacion","documentacion")


def to_render(html_render, data, table):
    html_render['table'] = table


def table_show(request):
    data = news.objects.all()
    data = data.values( "numero_expediente","name","timestamp","idioma_encargo","via_encargo","ID_prescriptor_id","ID_cliente_id","objetivo_tasacion","documentacion")

    table = newsTable(data)  # , row_attrs={'id': lambda record: record['sn']}, order_by="-updated_time")
    RequestConfig(request, paginate={'per_page': 100}).configure(table)

    html_render = {}
    to_render(html_render, data, table)
    return render(request, "index.html", html_render)


# rendering "Search by Title"
def news_search(request):
    data = news.objects.all()
    html_render = {}

    data = data.filter(models.Q(name__icontains=request.GET['keywd_input']))
    data = data.values("numero_expediente","name","timestamp","idioma_encargo","via_encargo","ID_prescriptor_id","ID_cliente_id","objetivo_tasacion","documentacion")
    table = newsTable(data)  # , order_by="-time")
    RequestConfig(request, paginate={'per_page': 100}).configure(table)
    to_render(html_render, data, table)
    html_render['keywd_input'] = request.GET['keywd_input']

    return render(request, "index.html", html_render)


def download_excel(requst):
    data = news.objects.all()
    print(type(data))
    data = data.values( "numero_expediente","name","timestamp","idioma_encargo","via_encargo","ID_prescriptor_id","ID_cliente_id","objetivo_tasacion","documentacion")
    print(type(data))
    return render_to_csv_response(data, filename="table_download.csv")
