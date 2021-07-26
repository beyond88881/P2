# ('D:\\spaceApache\\www\\dpy\\project\\locale', 'D:\\spaceApache\\www\\dpy\\project\\report/locale')
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.utils.translation import gettext_lazy as _


class Persons(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    id2 = models.IntegerField(db_column='ID2', blank=True, null=True)  # Field name made lowercase.
    id3 = models.IntegerField(db_column='ID3', blank=True, null=True)  # Field name made lowercase.
    identity = models.CharField(db_column='Identity', max_length=255, blank=True,
                                null=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=255, blank=True, null=True)  # Field name made lowercase.
    gender = models.CharField(db_column='Gender', max_length=255, blank=True, null=True)  # Field name made lowercase.
    employeeno = models.CharField(db_column='employeeNo', max_length=255, blank=True,
                                  null=True)  # Field name made lowercase.
    user_id = models.CharField(db_column='User ID', max_length=255, blank=True,
                               null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    enfirstname = models.CharField(db_column='EnFirstName', max_length=255, blank=True,
                                   null=True)  # Field name made lowercase.
    enmiddlename = models.CharField(db_column='EnmiddleName', max_length=255, blank=True,
                                    null=True)  # Field name made lowercase.
    ensurname = models.CharField(db_column='EnSurname', max_length=255, blank=True,
                                 null=True)  # Field name made lowercase.
    ensub = models.CharField(db_column='EnSub', max_length=255, blank=True, null=True)  # Field name made lowercase.
    enappelation = models.CharField(db_column='EnAppelation', max_length=255, blank=True,
                                    null=True)  # Field name made lowercase.
    cnsurname = models.CharField(db_column='CnSurName', max_length=255, blank=True,
                                 null=True)  # Field name made lowercase.
    cnfirstname = models.CharField(db_column='CnFirstName', max_length=255, blank=True,
                                   null=True)  # Field name made lowercase.
    cnappelation = models.CharField(db_column='CnAppelation', max_length=255, blank=True,
                                    null=True)  # Field name made lowercase.
    position = models.CharField(db_column='Position', max_length=255, blank=True,
                                null=True)  # Field name made lowercase.
    administrative_post = models.IntegerField(db_column='Administrative_post', blank=True,
                                              null=True)  # Field name made lowercase.
    default_language = models.CharField(db_column='Default Language', max_length=255, blank=True,
                                        null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    country = models.CharField(db_column='Country', max_length=255, blank=True, null=True)  # Field name made lowercase.
    creation_date = models.DateTimeField(db_column='Creation Date', blank=True,
                                         null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    contact_customers = models.CharField(db_column='Contact customers', max_length=255, blank=True,
                                         null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    contact_suppliers = models.CharField(db_column='Contact suppliers', max_length=255, blank=True,
                                         null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    original = models.CharField(max_length=255, blank=True, null=True)
    createdtime = models.DateTimeField(db_column='createdTime', blank=True, null=True)  # Field name made lowercase.
    timeupdated = models.DateTimeField(db_column='TimeUpdated', blank=True, null=True)  # Field name made lowercase.
    type = models.CharField(db_column='Type', max_length=255, blank=True, null=True)  # Field name made lowercase.
    companyid = models.IntegerField(db_column='companyID', blank=True, null=True)  # Field name made lowercase.
    department = models.CharField(max_length=255, blank=True, null=True)
    e_mail = models.CharField(db_column='e-mail', max_length=255, blank=True,
                              null=True)  # Field renamed to remove unsuitable characters.
    mobile = models.CharField(max_length=255, blank=True, null=True)
    addressformail = models.CharField(db_column='addressForMail', max_length=255, blank=True,
                                      null=True)  # Field name made lowercase.
    phone = models.CharField(max_length=255, blank=True, null=True)
    fax = models.CharField(max_length=255, blank=True, null=True)
    aidselection = models.BooleanField(db_column='aidSelection', blank=True, null=True)  # Field name made lowercase.
    remark = models.TextField(blank=True, null=True)
    rowcreatedtime = models.DateTimeField(db_column='rowCreatedTime', blank=True,
                                          null=True)  # Field name made lowercase.
    availability = models.BooleanField(blank=True, null=True)
    expireddate = models.DateTimeField(db_column='expiredDate', blank=True, null=True)  # Field name made lowercase.
    expirereason = models.CharField(db_column='expireReason', max_length=255, blank=True,
                                    null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PersonsInfo'
        #app_label用于把models文件下的相关models_***.py定义到多个文件中去
        app_label = 'projectManagement'

