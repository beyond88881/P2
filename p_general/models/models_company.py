from django.db import models

class Company(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    id_associatedcompany = models.PositiveIntegerField(db_column='ID_AssociatedCompany', blank=True, null=True)  # Field name made lowercase.
    roleproperty = models.CharField(db_column='RoleProperty', max_length=255, blank=True, null=True)  # Field name made lowercase.
    property = models.CharField(db_column='Property', max_length=255, blank=True, null=True)  # Field name made lowercase.
    companyname = models.CharField(db_column='companyName', unique=True, max_length=255, blank=True, null=True)  # Field name made lowercase.
    companyname_cn = models.CharField(db_column='companyName_CN', max_length=255, blank=True, null=True)  # Field name made lowercase.
    shortname = models.CharField(db_column='shortName', unique=True, max_length=255, blank=True, null=True)  # Field name made lowercase.
    innerused = models.TextField(db_column='innerUsed', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    basic_currency = models.ForeignKey('Currency', models.DO_NOTHING, db_column='basic_Currency', blank=True, null=True)  # Field name made lowercase.
    language_code = models.CharField(db_column='Language Code', max_length=10, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    date_created = models.DateTimeField(db_column='Date Created', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    timeupdated = models.DateTimeField(db_column='TimeUpdated', blank=True, null=True)  # Field name made lowercase.
    expiry_date = models.DateTimeField(db_column='Expiry Date', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    country = models.ForeignKey('CountryArea', models.DO_NOTHING, db_column='country', blank=True, null=True)
    state = models.CharField(max_length=50, blank=True, null=True)
    city = models.CharField(max_length=50, blank=True, null=True)
    street_address = models.CharField(max_length=255, blank=True, null=True)
    location_type = models.IntegerField(blank=True, null=True)
    id_companyhq = models.IntegerField(db_column='ID_companyHQ', blank=True, null=True)  # Field name made lowercase.
    id_co_oper = models.PositiveIntegerField(db_column='ID_co_oper')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'company'

# class Company(models.Model):
    # id = models.IntegerField(db_column='ID', blank=True, primary_key=True)  # Field name made lowercase.
    # associatedcompanyid = models.IntegerField(db_column='AssociatedCompanyID', blank=True,
    #                                           null=True)  # Field name made lowercase.
    # roleproperty = models.CharField(db_column='RoleProperty', max_length=255, blank=True,
    #                                 null=True)  # Field name made lowercase.
    # property = models.CharField(db_column='Property', max_length=255, blank=True,
    #                             null=True)  # Field name made lowercase.
    # puspartnerno = models.CharField(db_column='PUSpartnerNo', max_length=255, blank=True,
    #                                 null=True)  # Field name made lowercase.
    # pusname = models.CharField(db_column='PUSname', max_length=255, blank=True, null=True)  # Field name made lowercase.
    # companyno = models.CharField(db_column='companyNo', max_length=255, blank=True,
    #                              null=True)  # Field name made lowercase.
    # companyname = models.CharField(db_column='companyName', max_length=255, blank=True,
    #                                null=True)  # Field name made lowercase.
    # companyname_cn = models.CharField(db_column='companyName_CN', max_length=255, blank=True,
    #                                   null=True)  # Field name made lowercase.
    # shortname = models.CharField(db_column='shortName', max_length=255, blank=True,
    #                              null=True)  # Field name made lowercase.
    # innerused = models.CharField(db_column='innerUsed', max_length=5, blank=True,
    #                              null=True)  # Field name made lowercase.
    # currency = models.CharField(db_column='Currency', max_length=255, blank=True,
    #                             null=True)  # Field name made lowercase.
    # language_code = models.CharField(db_column='Language Code', max_length=255, blank=True,
    #                                  null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    # date_created = models.DateTimeField(db_column='Date Created', blank=True,
    #                                     null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    # timeupdated = models.DateTimeField(db_column='TimeUpdated', blank=True, null=True)  # Field name made lowercase.
    # expiry_date = models.DateTimeField(db_column='Expiry Date', blank=True,
    #                                    null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    # original = models.CharField(max_length=255, blank=True, null=True)
    # country = models.CharField(max_length=255, blank=True, null=True)
    # state = models.CharField(max_length=255, blank=True, null=True)
    # city = models.CharField(max_length=255, blank=True, null=True)
    # detailaddress = models.CharField(db_column='detailAddress', max_length=255, blank=True,
    #                                  null=True)  # Field name made lowercase.
    # buyer = models.CharField(db_column='Buyer', max_length=255, blank=True, null=True)  # Field name made lowercase.
    # doc = models.CharField(max_length=255, blank=True, null=True)
    # lastdoc = models.CharField(db_column='lastDoc', max_length=255, blank=True, null=True)  # Field name made lowercase.
    # defaulttask = models.IntegerField(db_column='defaultTask', blank=True, null=True)  # Field name made lowercase.
    # remark = models.TextField(blank=True, null=True)
    # samesupplieridentity = models.CharField(db_column='SameSupplierIdentity', max_length=255, blank=True,
    #                                         null=True)  # Field name made lowercase.
    # quality_approved = models.CharField(db_column='Quality Approved', max_length=255, blank=True,
    #                                     null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    # quality_date = models.DateTimeField(db_column='Quality Date', blank=True,
    #                                     null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    # quality_type = models.CharField(db_column='Quality Type', max_length=255, blank=True,
    #                                 null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    # quality_note_text = models.CharField(db_column='Quality Note Text', max_length=255, blank=True,
    #                                      null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    # taxnumber = models.CharField(db_column='taxNumber', max_length=255, blank=True,
    #                              null=True)  # Field name made lowercase.
    # historictaxnumber = models.CharField(db_column='historicTaxNumber', max_length=255, blank=True,
    #                                      null=True)  # Field name made lowercase.
    # environment_approved = models.CharField(db_column='Environment Approved', max_length=255, blank=True,
    #                                         null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    # environment_date = models.CharField(db_column='Environment Date', max_length=255, blank=True,
    #                                     null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    # environment_type = models.DateTimeField(db_column='Environment Type', blank=True,
    #                                         null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    # environment_note_text = models.CharField(db_column='Environment Note Text', max_length=255, blank=True,
    #                                          null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    # code_of_conduct_approved = models.CharField(db_column='Code of Conduct Approved', max_length=255, blank=True,
    #                                             null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    # code_of_conduct_date = models.DateTimeField(db_column='Code of Conduct Date', blank=True,
    #                                             null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    # code_of_conduct_type = models.CharField(db_column='Code of Conduct Type', max_length=255, blank=True,
    #                                         null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    # code_of_conduct_note_text = models.CharField(db_column='Code of Conduct Note Text', max_length=255, blank=True,
    #                                              null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    # pay_term_id = models.CharField(db_column='Pay Term ID', max_length=255, blank=True,
    #                                null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    # pay_tax = models.CharField(db_column='Pay Tax', max_length=255, blank=True,
    #                            null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    # pay_term_info = models.CharField(db_column='Pay Term Info', max_length=255, blank=True,
    #                                  null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    # pay_tax_info = models.CharField(db_column='Pay Tax Info', max_length=255, blank=True,
    #                                 null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    # rowcreatedtime = models.DateTimeField(db_column='rowCreatedTime', blank=True,
    #                                       null=True)  # Field name made lowercase.
    # rowupdatedtime = models.DateTimeField(db_column='rowUpdatedTime', blank=True,
    #                                       null=True)  # Field name made lowercase.
    # aidselection = models.CharField(db_column='aidSelection', max_length=5, blank=True,
    #                                 null=True)  # Field name made lowercase.
    # ownplant = models.CharField(db_column='ownPlant', max_length=5, blank=True, null=True)  # Field name made lowercase.

