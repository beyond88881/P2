# ('D:\\spaceApache\\www\\dpy\\project\\locale', 'D:\\spaceApache\\www\\dpy\\project\\report/locale')
# # This is an auto-generated Django model module.
# # You'll have to do the following manually to clean this up:
# #   * Rearrange models' order
# #   * Make sure each model has one field with primary_key=True
# #   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
# #   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# # Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.utils.translation import gettext_lazy as _

from .models_person import Persons


class Project(models.Model):
    id = models.IntegerField(db_column='id', blank=True, primary_key=True)  # Field name made lowercase.
    no = models.IntegerField(db_column='No', blank=True, null=True)  # Field name made lowercase.
    defaulttask = models.IntegerField(db_column='defaultTask', blank=True, null=True)  # Field name made lowercase.
    isproductproject = models.BooleanField(db_column='isProductProject', blank=True,
                                           null=True)  # Field name made lowercase.
    activestatus = models.CharField(db_column='activeStatus', max_length=255, blank=True,
                                    null=True)  # Field name made lowercase.
    bu = models.CharField(db_column='BU', max_length=255, blank=True, null=True)  # Field name made lowercase.
    customer_name = models.CharField(db_column='customer name', max_length=255, blank=True,
                                     null=True)  # Field renamed to remove unsuitable characters.
    customer_name2 = models.CharField(db_column='customer name2', max_length=255, blank=True,
                                      null=True)  # Field renamed to remove unsuitable characters.
    project_name = models.CharField(db_column='project name', max_length=255, blank=True,
                                    null=True)  # Field renamed to remove unsuitable characters.
    bu_product_type = models.IntegerField(db_column='BU Product Type', blank=True,
                                          null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    bu_product_type_description = models.CharField(db_column='BU Product Type Description', max_length=255, blank=True,
                                                   null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    producttype_l1 = models.IntegerField(db_column='productType_L1', blank=True,
                                         null=True)  # Field name made lowercase.
    product_name = models.CharField(db_column='product name', max_length=255, blank=True,
                                    null=True)  # Field renamed to remove unsuitable characters.
    huf_projectno = models.CharField(db_column='Huf_projectNo', max_length=255, blank=True,
                                     null=True)  # Field name made lowercase.
    subno = models.CharField(db_column='subNo', max_length=255, blank=True, null=True)  # Field name made lowercase.
    submain = models.BooleanField(db_column='subMain', blank=True, null=True)  # Field name made lowercase.
    project_info_received_date = models.DateTimeField(db_column='project info received date', blank=True,
                                                      null=True)  # Field renamed to remove unsuitable characters.
    project_info_released_by = models.CharField(db_column='project info released by', max_length=255, blank=True,
                                                null=True)  # Field renamed to remove unsuitable characters.
    sysstatus = models.IntegerField(db_column='sysStatus', blank=True, null=True)  # Field name made lowercase.
    sysstatus_remark = models.CharField(db_column='sysStatus_remark', max_length=255, blank=True,
                                        null=True)  # Field name made lowercase.
    project_status = models.IntegerField(db_column='project status', blank=True,
                                         null=True)  # Field renamed to remove unsuitable characters.
    projectidforclassify = models.IntegerField(db_column='projectIDForClassify', blank=True,
                                               null=True)  # Field name made lowercase.
    remark = models.TextField(blank=True, null=True)
    selfremark = models.TextField(db_column='selfRemark', blank=True, null=True)  # Field name made lowercase.
    pm = models.CharField(db_column='PM', max_length=255, blank=True, null=True)  # Field name made lowercase.
    pa = models.CharField(db_column='PA', max_length=255, blank=True, null=True)  # Field name made lowercase.
    pc = models.CharField(db_column='PC', max_length=255, blank=True, null=True)  # Field name made lowercase.
    account_manager = models.CharField(db_column='account manager', max_length=255, blank=True,
                                       null=True)  # Field renamed to remove unsuitable characters.
    project_type = models.CharField(db_column='project type', max_length=255, blank=True,
                                    null=True)  # Field renamed to remove unsuitable characters.
    project_developing_phase = models.CharField(db_column='project developing phase', max_length=255, blank=True,
                                                null=True)  # Field renamed to remove unsuitable characters.
    actual_project_developing_phase = models.CharField(db_column='actual project developing phase', max_length=255,
                                                       blank=True,
                                                       null=True)  # Field renamed to remove unsuitable characters.
    development_location = models.CharField(db_column='Development location', max_length=255, blank=True,
                                            null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    production_location = models.CharField(db_column='Production location', max_length=255, blank=True,
                                           null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    release_location = models.CharField(db_column='Release location', max_length=255, blank=True,
                                        null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sop_customer = models.DateTimeField(db_column='SOP customer', blank=True,
                                        null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    eop_customer = models.DateTimeField(db_column='EOP customer', blank=True,
                                        null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    life_time = models.CharField(db_column='life time', max_length=255, blank=True,
                                 null=True)  # Field renamed to remove unsuitable characters.
    annual_average_volume_bycar = models.IntegerField(db_column='annual average volume(car)', blank=True,
                                                      null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    max_volume_bycar = models.IntegerField(db_column='max volume(car)', blank=True,
                                           null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    total_volume_bycar = models.IntegerField(db_column='Total Volume(car)', blank=True,
                                             null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    year_1_volume_bycar = models.IntegerField(db_column='year 1 volume(car)', blank=True,
                                              null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    year_2_volume_bycar = models.IntegerField(db_column='year 2 volume(car)', blank=True,
                                              null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    year_3_volume_bycar = models.IntegerField(db_column='year 3 volume(car)', blank=True,
                                              null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    year_4_volume_bycar = models.IntegerField(db_column='year 4 volume(car)', blank=True,
                                              null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    year_5_volume_bycar = models.IntegerField(db_column='year 5 volume(car)', blank=True,
                                              null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    year_6_volume_bycar = models.IntegerField(db_column='year 6 volume(car)', blank=True,
                                              null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    year_7_volume_bycar = models.IntegerField(db_column='year 7 volume(car)', blank=True,
                                              null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    year_8_volume_bycar = models.IntegerField(db_column='year 8 volume(car)', blank=True,
                                              null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    year_9_volume_bycar = models.IntegerField(db_column='year 9 volume(car)', blank=True,
                                              null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    year_10_volume_bycar = models.IntegerField(db_column='year 10 volume(car)', blank=True,
                                               null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    year_11_volume_bycar = models.IntegerField(db_column='year 11 volume(car)', blank=True,
                                               null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    year_12_volume_bycar = models.IntegerField(db_column='year 12 volume(car)', blank=True,
                                               null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    year_13_volume_bycar = models.IntegerField(db_column='year 13 volume(car)', blank=True,
                                               null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    year_14_volume_bycar = models.IntegerField(db_column='year 14 volume(car)', blank=True,
                                               null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    year_15_volume_bycar = models.IntegerField(db_column='year 15 volume(car)', blank=True,
                                               null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    volumeremark = models.CharField(db_column='volumeRemark', max_length=255, blank=True,
                                    null=True)  # Field name made lowercase.
    pu_buyer = models.CharField(db_column='PU buyer', max_length=255, blank=True,
                                null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    pu_aid = models.CharField(db_column='PU aid', max_length=255, blank=True,
                              null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    lta = models.CharField(db_column='LTA', max_length=255, blank=True, null=True)  # Field name made lowercase.
    design = models.DateTimeField(db_column='Design', blank=True, null=True)  # Field name made lowercase.
    detailed_design = models.DateTimeField(db_column='Detailed Design', blank=True,
                                           null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    prtyp_qualf = models.DateTimeField(db_column='PrTyp qualf', blank=True,
                                       null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    verifiled_detailed_design = models.DateTimeField(db_column='verifiled detailed design', blank=True,
                                                     null=True)  # Field renamed to remove unsuitable characters.
    first_off_production_parts = models.DateTimeField(db_column='1#(st)off production parts', blank=True,
                                                      null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    first_production_trial_run = models.DateTimeField(db_column='1#(st)production trial run', blank=True,
                                                      null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    second_production_trial_run = models.DateTimeField(db_column='2#(nd)production trial run', blank=True,
                                                       null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    qualification_serial_part_completed = models.DateTimeField(db_column='qualification serial part completed',
                                                               blank=True,
                                                               null=True)  # Field renamed to remove unsuitable characters.
    ppap_customer_submission = models.DateTimeField(db_column='PPAP customer submission', blank=True,
                                                    null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    ppap_customer_release = models.DateTimeField(db_column='PPAP customer release', blank=True,
                                                 null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    profitability_analysis1 = models.DateTimeField(db_column='profitability analysis1', blank=True,
                                                   null=True)  # Field renamed to remove unsuitable characters.
    gateway_review1 = models.DateTimeField(db_column='Gateway review1', blank=True,
                                           null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    profitability_analysis2 = models.DateTimeField(db_column='profitability analysis2', blank=True,
                                                   null=True)  # Field renamed to remove unsuitable characters.
    gateway_review2 = models.DateTimeField(db_column='Gateway review2', blank=True,
                                           null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    profitability_analysis3 = models.DateTimeField(db_column='profitability analysis3', blank=True,
                                                   null=True)  # Field renamed to remove unsuitable characters.
    gateway_review3 = models.DateTimeField(db_column='Gateway review3', blank=True,
                                           null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    profitability_analysis4 = models.DateTimeField(db_column='profitability analysis4', blank=True,
                                                   null=True)  # Field renamed to remove unsuitable characters.
    gateway_review4 = models.DateTimeField(db_column='Gateway review4', blank=True,
                                           null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    profitability_analysis5 = models.DateTimeField(db_column='profitability analysis5', blank=True,
                                                   null=True)  # Field renamed to remove unsuitable characters.
    gateway_review5 = models.DateTimeField(db_column='Gateway review5', blank=True,
                                           null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    design_review1 = models.DateTimeField(db_column='design review1', blank=True,
                                          null=True)  # Field renamed to remove unsuitable characters.
    design_review2 = models.DateTimeField(db_column='design review2', blank=True,
                                          null=True)  # Field renamed to remove unsuitable characters.
    design_review3 = models.DateTimeField(db_column='design review3', blank=True,
                                          null=True)  # Field renamed to remove unsuitable characters.
    projectlifestatus = models.CharField(db_column='projectLifeStatus', max_length=25, blank=True,
                                         null=True)  # Field name made lowercase.
    createdtime = models.DateTimeField(db_column='createdTime', blank=True, null=True)  # Field name made lowercase.
    updatedtime = models.DateTimeField(db_column='updatedTime', blank=True, null=True)  # Field name made lowercase.
    docid = models.IntegerField(db_column='docID', blank=True, null=True)  # Field name made lowercase.
    docmob = models.CharField(db_column='docMOB', max_length=255, blank=True, null=True)  # Field name made lowercase.
    doctargetprice = models.CharField(db_column='docTargetPrice', max_length=255, blank=True,
                                      null=True)  # Field name made lowercase.
    docpartriskevaluation = models.CharField(db_column='docPartRiskEvaluation', max_length=255, blank=True,
                                             null=True)  # Field name made lowercase.
    docsuppliernomination = models.CharField(db_column='docSupplierNomination', max_length=255, blank=True,
                                             null=True)  # Field name made lowercase.
    docothers = models.CharField(db_column='docOthers', max_length=255, blank=True,
                                 null=True)  # Field name made lowercase.
    docgeneral = models.CharField(db_column='docGeneral', max_length=255, blank=True,
                                  null=True)  # Field name made lowercase.
    docoil = models.CharField(db_column='docOIL', max_length=255, blank=True, null=True)  # Field name made lowercase.
    docmeeting = models.CharField(db_column='docMeeting', max_length=255, blank=True,
                                  null=True)  # Field name made lowercase.
    docrelatedproject = models.CharField(db_column='docRelatedProject', max_length=255, blank=True,
                                         null=True)  # Field name made lowercase.
    doctech = models.CharField(db_column='docTech', max_length=255, blank=True, null=True)  # Field name made lowercase.
    docspecialrequirement = models.CharField(db_column='docSpecialRequirement', max_length=255, blank=True,
                                             null=True)  # Field name made lowercase.
    doccustomerltaandrelated = models.CharField(db_column='docCustomerLTAandRelated', max_length=255, blank=True,
                                                null=True)  # Field name made lowercase.
    docprojectvolume = models.CharField(db_column='docProjectVolume', max_length=255, blank=True,
                                        null=True)  # Field name made lowercase.
    doctoolfixture = models.CharField(db_column='docToolFixture', max_length=255, blank=True,
                                      null=True)  # Field name made lowercase.
    # purprojectaid = models.IntegerField(db_column='purProjectAid', blank=True, null=True)  # Field name made lowercase.
    purprojectaid = models.ForeignKey(Persons, db_column='purProjectAid', blank=True, null=True,
                                      on_delete=models.PROTECT, related_name='buyerAid')  # Field name made lowercase.
    # purprojectbuyermain = models.IntegerField(db_column='purProjectBuyerMain', blank=True, null=True)  # Field name made lowercase.
    purprojectbuyermain = models.ForeignKey(Persons, db_column='purProjectBuyerMain', blank=True,
                                            null=True, on_delete=models.PROTECT,
                                            related_name='buyer')  # Field name made lowercase.
    assembly_no = models.CharField(db_column='assembly No', max_length=255, blank=True,
                                   null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    teamid = models.IntegerField(db_column='teamID', blank=True, null=True)  # Field name made lowercase.
    doc = models.CharField(max_length=255, blank=True, null=True)
    lastdoc = models.CharField(db_column='lastDoc', max_length=255, blank=True, null=True)  # Field name made lowercase.
    statistic_sop = models.DateTimeField(db_column='Statistic_SOP', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'project'
        # # app_label用于把models文件下的相关models_***.py定义到多个文件中去
        app_label = 'projectManagement'
