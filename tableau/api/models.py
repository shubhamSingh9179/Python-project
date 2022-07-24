# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Employee(models.Model):
    name = models.CharField(max_length=10, blank=True, null=True)
    dob = models.DateField(blank=True, null=True)
    dotime = models.TimeField(blank=True, null=True)
    product_name = models.CharField(max_length=10, blank=True, null=True)
    price = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'employee'
