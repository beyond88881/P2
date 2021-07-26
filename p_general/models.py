# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group_id = models.IntegerField()
    permission_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group_id', 'permission_id'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type_id = models.IntegerField()
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type_id', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUser1(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()
    id_co_oper = models.PositiveIntegerField(db_column='ID_co_oper')  # Field name made lowercase.
    rowupdatedtime = models.DateTimeField(db_column='rowUpdatedTime', blank=True, null=True)  # Field name made lowercase.
    rowcreated = models.DateTimeField(db_column='rowCreated', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'auth_user1'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user_id = models.IntegerField()
    group_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user_id', 'group_id'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user_id = models.IntegerField()
    permission_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user_id', 'permission_id'),)


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


class CompanyLocation(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    company_loc_desc = models.CharField(max_length=255)
    id_company = models.ForeignKey(Company, models.DO_NOTHING, db_column='ID_company', blank=True, null=True)  # Field name made lowercase.
    country = models.ForeignKey('CountryArea', models.DO_NOTHING, db_column='country', blank=True, null=True)
    state = models.CharField(max_length=50, blank=True, null=True)
    city = models.CharField(max_length=50, blank=True, null=True)
    street_address = models.CharField(max_length=50, blank=True, null=True)
    location_type = models.IntegerField(blank=True, null=True)
    remark = models.TextField(blank=True, null=True)
    id_co_oper = models.PositiveIntegerField(db_column='ID_co_oper')  # Field name made lowercase.
    roleproperty = models.CharField(db_column='RoleProperty', max_length=255, blank=True, null=True)  # Field name made lowercase.
    property = models.CharField(db_column='Property', max_length=255, blank=True, null=True)  # Field name made lowercase.
    puspartnerno = models.CharField(db_column='PUSpartnerNo', max_length=255, blank=True, null=True)  # Field name made lowercase.
    pusname = models.CharField(db_column='PUSname', max_length=255, blank=True, null=True)  # Field name made lowercase.
    companyno = models.CharField(db_column='companyNo', max_length=255, blank=True, null=True)  # Field name made lowercase.
    companyname = models.CharField(db_column='companyName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    companyname_cn = models.CharField(db_column='companyName_CN', max_length=255, blank=True, null=True)  # Field name made lowercase.
    shortname = models.CharField(db_column='shortName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    innerused = models.TextField(db_column='innerUsed', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    basic_currency = models.ForeignKey('Currency', models.DO_NOTHING, db_column='basic_Currency', blank=True, null=True)  # Field name made lowercase.
    language_code = models.CharField(db_column='Language Code', max_length=10, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    expiry_date = models.DateTimeField(db_column='Expiry Date', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    original = models.CharField(max_length=255, blank=True, null=True)
    buyer = models.PositiveIntegerField(db_column='Buyer', blank=True, null=True)  # Field name made lowercase.
    doc = models.CharField(max_length=255, blank=True, null=True)
    lastdoc = models.CharField(db_column='lastDoc', max_length=255, blank=True, null=True)  # Field name made lowercase.
    defaulttask = models.IntegerField(db_column='defaultTask', blank=True, null=True)  # Field name made lowercase.
    samesupplieridentity = models.CharField(db_column='SameSupplierIdentity', max_length=255, blank=True, null=True)  # Field name made lowercase.
    quality_approved = models.CharField(db_column='Quality Approved', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    quality_date = models.DateTimeField(db_column='Quality Date', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    quality_type = models.CharField(db_column='Quality Type', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    quality_note_text = models.CharField(db_column='Quality Note Text', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    taxnumber = models.CharField(db_column='taxNumber', max_length=255, blank=True, null=True)  # Field name made lowercase.
    historictaxnumber = models.CharField(db_column='historicTaxNumber', max_length=255, blank=True, null=True)  # Field name made lowercase.
    environment_approved = models.CharField(db_column='Environment Approved', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    environment_date = models.CharField(db_column='Environment Date', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    environment_type = models.DateTimeField(db_column='Environment Type', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    environment_note_text = models.CharField(db_column='Environment Note Text', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    code_of_conduct_approved = models.CharField(db_column='Code of Conduct Approved', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    code_of_conduct_date = models.DateTimeField(db_column='Code of Conduct Date', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    code_of_conduct_type = models.CharField(db_column='Code of Conduct Type', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    code_of_conduct_note_text = models.CharField(db_column='Code of Conduct Note Text', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    pay_term_id = models.CharField(db_column='Pay Term ID', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    pay_tax = models.CharField(db_column='Pay Tax', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    pay_term_info = models.CharField(db_column='Pay Term Info', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    pay_tax_info = models.CharField(db_column='Pay Tax Info', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    aidselection = models.TextField(db_column='aidSelection', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    ownplant = models.TextField(db_column='ownPlant', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    rowupdatedtime = models.DateTimeField(db_column='rowUpdatedTime', blank=True, null=True)  # Field name made lowercase.
    rowcreated = models.DateTimeField(db_column='rowCreated', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'company_location'
        unique_together = (('id_company', 'country', 'state', 'city', 'street_address', 'location_type'),)


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

    class Meta:
        managed = False
        db_table = 'country_area'


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


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type_id = models.IntegerField(blank=True, null=True)
    user_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Uom(models.Model):
    uom = models.CharField(db_column='UoM', primary_key=True, max_length=10, db_collation='utf8_bin')  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=255, blank=True, null=True)  # Field name made lowercase.
    factor = models.CharField(db_column='Factor', max_length=20)  # Field name made lowercase.
    constant = models.CharField(db_column='Constant', max_length=20, blank=True, null=True)  # Field name made lowercase.
    base_uom = models.CharField(db_column='Base UoM', max_length=10)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    uom_type = models.CharField(db_column='UoM Type', max_length=20)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    user_defined_uom = models.CharField(db_column='User Defined UoM', max_length=5)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    id_co_oper = models.PositiveIntegerField(db_column='ID_co_oper')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'uom'
