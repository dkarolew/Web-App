from django.db import models


# Create your models here.


class SystemState(models.Model):
    date = models.DateField()
    temperature = models.FloatField()
    Tpco_1 = models.FloatField()
    Valve_1 = models.FloatField()

    class Meta:
        db_table = 'TABELA_BUDYNEK_1'


class SystemState_2(models.Model):
    date = models.DateField()
    temperature = models.FloatField()
    Tpco_2 = models.FloatField()
    Valve_2 = models.FloatField()

    class Meta:
        db_table = 'TABELA_BUDYNEK_2'


class SystemState_3(models.Model):
    date = models.DateField()
    temperature = models.FloatField()
    Tpco_3 = models.FloatField()
    Valve_3 = models.FloatField()

    class Meta:
        db_table = 'TABELA_BUDYNEK_3'
