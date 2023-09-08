# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Municipios(models.Model):
    muni_codigo = models.DecimalField(unique=True, max_digits=6, decimal_places=0)
    muni_nome = models.CharField(max_length=40, blank=True, null=True)
    muni_uf = models.CharField(max_length=2, blank=True, null=True)
    muni_regi_codigo = models.CharField(max_length=3, blank=True, null=True)
    muni_codigodfc = models.CharField(max_length=5, blank=True, null=True)
    muni_codigorais = models.CharField(max_length=7, blank=True, null=True)
    muni_codigogia = models.CharField(max_length=5, blank=True, null=True)
    muni_codigoibge = models.DecimalField(max_digits=8, decimal_places=0, blank=True, null=True)
    muni_codigopais = models.CharField(max_length=4, blank=True, null=True)
    muni_iss = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    muni_rotas = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'municipios'
