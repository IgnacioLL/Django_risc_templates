
from django.contrib import admin
from django.urls import path
from encargo import views as encargo
from prescriptor import views as prescriptor
from clientes import views as cliente
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
    path('paso1', encargo.encargoPage),
    path('paso1/ajax/encargo', encargo.postEncargo, name = 'encargo_submit'),
    path('paso1/encargo_cbv', encargo.EncargoAjax.as_view(), name = 'encargo_submit_cbv'),

    path('paso2', prescriptor.prescriptorPage),
    path('paso2/ajax/prescriptor', prescriptor.postPrescriptor, name = 'prescriptor_submit'),
    path('paso2/prescriptor_cbv', prescriptor.PrescriptorAjax.as_view(), name = 'prescriptor_submit_cbv'),

    path('paso3', cliente.clientePage),
    path('paso3/ajax/cliente', cliente.postCliente, name = 'cliente_submit'),
    path('paso3/cliente_cbv', cliente.ClienteAjax.as_view(), name = 'cliente_submit_cbv'),

    path('paso4', tarifas.tarifasPage),
    path('paso4/ajax/tarifas', tarifas.posttarifas, name = 'tarifas_submit'),
    path('paso4/tarifas_cbv', tarifas.tarifasAjax.as_view(), name = 'tarifas_submit_cbv'),

]
