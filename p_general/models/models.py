# ('D:\\spaceApache\\www\\dpy\\project\\locale', 'D:\\spaceApache\\www\\dpy\\project\\report/locale')
# # This is an auto-generated Django model module.
# # You'll have to do the following manually to clean this up:
# #   * Rearrange models' order
# #   * Make sure each model has one field with primary_key=True
# #   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
# #   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# # Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
#
#
# class AuthGroup(models.Model):
#     name = models.CharField(unique=True, max_length=150)
#
#     class Meta:
#         managed = False
#         db_table = 'auth_group'
#
#
# class AuthGroupPermissions(models.Model):
#     group_id = models.IntegerField()
#     permission_id = models.IntegerField()
#
#     class Meta:
#         managed = False
#         db_table = 'auth_group_permissions'
#         unique_together = (('group_id', 'permission_id'),)
#
#
# class AuthPermission(models.Model):
#     name = models.CharField(max_length=255)
#     content_type_id = models.IntegerField()
#     codename = models.CharField(max_length=100)
#
#     class Meta:
#         managed = False
#         db_table = 'auth_permission'
#         unique_together = (('content_type_id', 'codename'),)
#
#
# class AuthUser(models.Model):
#     password = models.CharField(max_length=128)
#     last_login = models.DateTimeField(blank=True, null=True)
#     is_superuser = models.IntegerField()
#     username = models.CharField(unique=True, max_length=150)
#     first_name = models.CharField(max_length=30)
#     last_name = models.CharField(max_length=150)
#     email = models.CharField(max_length=254)
#     is_staff = models.IntegerField()
#     is_active = models.IntegerField()
#     date_joined = models.DateTimeField()
#
#     class Meta:
#         managed = False
#         db_table = 'auth_user'
#
#
# class AuthUserGroups(models.Model):
#     user_id = models.IntegerField()
#     group_id = models.IntegerField()
#
#     class Meta:
#         managed = False
#         db_table = 'auth_user_groups'
#         unique_together = (('user_id', 'group_id'),)
#
#
# class AuthUserUserPermissions(models.Model):
#     user_id = models.IntegerField()
#     permission_id = models.IntegerField()
#
#     class Meta:
#         managed = False
#         db_table = 'auth_user_user_permissions'
#         unique_together = (('user_id', 'permission_id'),)
#
#
# class DjangoAdminLog(models.Model):
#     action_time = models.DateTimeField()
#     object_id = models.TextField(blank=True, null=True)
#     object_repr = models.CharField(max_length=200)
#     action_flag = models.PositiveSmallIntegerField()
#     change_message = models.TextField()
#     content_type_id = models.IntegerField(blank=True, null=True)
#     user_id = models.IntegerField()
#
#     class Meta:
#         managed = False
#         db_table = 'django_admin_log'
#
#
# class DjangoContentType(models.Model):
#     app_label = models.CharField(max_length=100)
#     model = models.CharField(max_length=100)
#
#     class Meta:
#         managed = False
#         db_table = 'django_content_type'
#         unique_together = (('app_label', 'model'),)
#
#
# class DjangoMigrations(models.Model):
#     app = models.CharField(max_length=255)
#     name = models.CharField(max_length=255)
#     applied = models.DateTimeField()
#
#     class Meta:
#         managed = False
#         db_table = 'django_migrations'
#
#
# class DjangoSession(models.Model):
#     session_key = models.CharField(primary_key=True, max_length=40)
#     session_data = models.TextField()
#     expire_date = models.DateTimeField()
#
#     class Meta:
#         managed = False
#         db_table = 'django_session'
#
#
# class Employee(models.Model):
#     first_name = models.CharField(db_column='FIRST_NAME', max_length=20)  # Field name made lowercase.
#     last_name = models.CharField(db_column='LAST_NAME', max_length=20, blank=True,
#                                  null=True)  # Field name made lowercase.
#     age = models.IntegerField(db_column='AGE', blank=True, null=True)  # Field name made lowercase.
#     sex = models.CharField(db_column='SEX', max_length=1, blank=True, null=True)  # Field name made lowercase.
#     income = models.FloatField(db_column='INCOME', blank=True, null=True)  # Field name made lowercase.
#
#     class Meta:
#         managed = False
#         db_table = 'employee'
#
#
# class MainCategory(models.Model):
#     id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
#     category = models.CharField(max_length=255, blank=True, null=True)
#     description = models.CharField(max_length=255, blank=True, null=True)
#     type = models.CharField(max_length=255, blank=True, null=True)
#     sourcetype = models.CharField(db_column='sourceType', max_length=255, blank=True,
#                                   null=True)  # Field name made lowercase.
#     objectname = models.CharField(db_column='objectName', max_length=255, blank=True,
#                                   null=True)  # Field name made lowercase.
#     remark = models.CharField(max_length=255, blank=True, null=True)
#     type2 = models.CharField(max_length=255, blank=True, null=True)
#     available = models.TextField(blank=True, null=True)  # This field type is a guess.
#     usedfrequency = models.IntegerField(db_column='usedFrequency', blank=True, null=True)  # Field name made lowercase.
#     rowcreatedtime = models.DateTimeField(db_column='rowCreatedTime', blank=True,
#                                           null=True)  # Field name made lowercase.
#     doc = models.CharField(max_length=255, blank=True, null=True)
#     lastdoc = models.CharField(db_column='lastDoc', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     upper = models.IntegerField(db_column='Upper', blank=True, null=True)  # Field name made lowercase.
#
#     class Meta:
#         managed = False
#         db_table = 'main_category'
#
#
# class MainCategoryTier(models.Model):
#     id_main_category_tier = models.AutoField(db_column='ID_main_category_tier',
#                                              primary_key=True)  # Field name made lowercase.
#     id_main_category = models.IntegerField(db_column='ID_main_category')  # Field name made lowercase.
#     id_main_category_sub = models.IntegerField(db_column='ID_main_category_sub')  # Field name made lowercase.
#     main = models.IntegerField()
#
#     class Meta:
#         managed = False
#         db_table = 'main_category_tier'
#         unique_together = (('id_main_category', 'id_main_category_sub'),)
#
#
# class MainCategoryTierexpand(models.Model):
#     id_main_category_tierexpand = models.AutoField(db_column='ID_main_category_tierExpand',
#                                                    primary_key=True)  # Field name made lowercase.
#     tier_id = models.IntegerField(db_column='Tier_ID')  # Field name made lowercase.
#     id_main_category = models.IntegerField(db_column='ID_main_category')  # Field name made lowercase.
#     id_main_category_sub = models.IntegerField(db_column='ID_main_category_sub')  # Field name made lowercase.
#     category = models.CharField(max_length=255)
#     mynode = models.IntegerField(db_column='myNode')  # Field name made lowercase.
#     levelno = models.CharField(db_column='levelNo', max_length=255)  # Field name made lowercase.
#
#     class Meta:
#         managed = False
#         db_table = 'main_category_tierexpand'


class UserType(models.Model):
    id = models.AutoField('id', primary_key=True)
    name = models.CharField(max_length=32)

    def __str__(self):
        return self.name

    class Meta:
        managed = False
        db_table = 'UserType'
