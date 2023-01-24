
from django.contrib import admin
from django.urls import path
from encargo import views as encargo
from prescriptor import views as prescriptor
from clientes import views as cliente
from elementos import views as elementos
from tarifas import views as tarifas

from django.urls import path
from django.urls import include, re_path
from table_example_con import views as table_example




urlpatterns = [
    path('admin/', admin.site.urls),
    path("accounts/", include("django.contrib.auth.urls")),  # new

    path('summary/', table_example.table_show),
    re_path(r'^news_search$', table_example.news_search),
    re_path(r'^download_excel', table_example.download_excel),
    # app_1
    #FBV
    path('encargos', encargo.encargoPage),
    path('encargos/ajax/encargo', encargo.postEncargo, name = 'encargo_submit'),
    path('encargos/encargo_cbv', encargo.EncargoAjax.as_view(), name = 'encargo_submit_cbv'),

    path('prescriptores', prescriptor.prescriptorPage),
    path('prescriptores/ajax/prescriptor', prescriptor.postPrescriptor, name = 'prescriptor_submit'),
    path('prescriptores/prescriptor_cbv', prescriptor.PrescriptorAjax.as_view(), name = 'prescriptor_submit_cbv'),

    path('clientes', cliente.clientePage),
    path('clientes/ajax/cliente', cliente.postCliente, name = 'cliente_submit'),
    path('clientes/cliente_cbv', cliente.ClienteAjax.as_view(), name = 'cliente_submit_cbv'),

    path('elementos', elementos.elementosPage),
    path('elementos/ajax/elementos', elementos.postelementos, name = 'elementos_submit'),
    path('elementos/elementos_cbv', elementos.elementosAjax.as_view(), name = 'elementos_submit_cbv'),


    path('tarifas', tarifas.tarifasPage),
    path('tarifas/ajax/tarifas', tarifas.posttarifas, name = 'tarifas_submit'),
    path('tarifas/tarifas_cbv', tarifas.tarifasAjax.as_view(), name = 'tarifas_submit_cbv'),

]
