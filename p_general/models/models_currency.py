from django.db import models


class Currency(models.Model):
    currency = models.CharField(primary_key=True, max_length=10)
    curr_description = models.CharField(max_length=255, blank=True, null=True)
    factor = models.FloatField(db_column='Factor')  # Field name made lowercase.
    base_currency = models.CharField(max_length=10)
    active_status = models.CharField(max_length=11)
    id_co_oper = models.PositiveIntegerField(db_column='ID_co_oper')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'currency'
