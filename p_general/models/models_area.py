from django.db import models
from django.utils.translation import gettext_lazy as _


class CountryArea(models.Model):
    id_upper = models.PositiveIntegerField(db_column='ID_upper', blank=True, null=True)  # Field name made lowercase.
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    region = models.CharField(max_length=255, blank=True, null=True)
    area = models.CharField(max_length=255, blank=True, null=True)
    no = models.IntegerField(db_column='No', blank=True, null=True)  # Field name made lowercase.
    en_name = models.CharField(db_column='EN_name', max_length=255, blank=True, null=True)  # Field name made lowercase.
    cn_name = models.CharField(db_column='CN_name', max_length=255, blank=True, null=True)  # Field name made lowercase.
    remark = models.CharField(max_length=255, blank=True, null=True)
    country_code = models.CharField(db_column='Country Code', max_length=5, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    system_defined = models.CharField(db_column='System Defined', max_length=1, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    id_co_oper = models.PositiveIntegerField(db_column='ID_co_oper')  # Field name made lowercase.


    def __str__(self):
        # str1=self.area
        # str2=self.city
        # seq=(str1,  str2)
        # str='{}/{}'
        # return str.join(seq)
        # return '{}/{}'.format(str1,str2)
        # return self.area
        return '{}/{}'.format(self.area, self.city)

    class Meta:
        managed = False
        db_table = 'country_cn_area'
