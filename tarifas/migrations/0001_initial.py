# Generated by Django 4.1.5 on 2023-01-23 16:05

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("encargo", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="tarifas",
            fields=[
                (
                    "id_tarifas",
                    models.UUIDField(
                        default=uuid.uuid1,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("name", models.CharField(max_length=60)),
                ("comision_prescriptor", models.IntegerField(blank=True, null=True)),
                ("descuento_aplicar", models.FloatField(blank=True, null=True)),
                ("valor_presupuestado", models.FloatField(blank=True, null=True)),
                ("provision_de_fondos", models.FloatField(blank=True, null=True)),
                ("importe_de_la_provision", models.FloatField(blank=True, null=True)),
                (
                    "referencia_catastral",
                    models.CharField(blank=True, max_length=80, null=True),
                ),
                (
                    "ID_encargo",
                    models.ForeignKey(
                        default="7b1f8f5a-7353-4683-b4ea-5c8e2c1f91bd",
                        on_delete=django.db.models.deletion.SET_DEFAULT,
                        to="encargo.encargo",
                    ),
                ),
            ],
        ),
    ]
