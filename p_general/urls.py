from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView

from . import views
from django.utils.translation import gettext_lazy as _
from django.views.i18n import JavaScriptCatalog
from .views import views_category
from .views import views_company, views_test
from .views import views_logon
from .views import views
from P2 import views as views1
from .views import views_person

app_name = 'p_general'

urlpatterns = [
    path('modifyPassword/', views1.modifyPassword, name="modifyPassword"),
    path("", views1.main_page, name="p_general.main_page"),
    path("p1/", views1.first_page, name="p_general.first_page"),
    path("p1_test/", views1.test_first_page, name="p_general.first_page"),
    path("json/menu/", views1.jsonInfo_menu1, name="p_general.jsonInfo_menu1"),
    # path("json/menu/", views1.jsonInfo_menu1, name="p_general.jsonInfo_menu1_1"),
    path("json/menu/(\d+)", views1.jsonInfo_menu2, name="p_general.jsonInfo_menu2"),
    path("json/productList/", views1.jsonInfo_productList, name="p_general.productList"),
    path("treeInfo/", views_category.categoryTreeList, name="category1"),
    # 验证登录
    path("logon/", views1.ax_login, name="p_general.logon"),
    path("logon/c1/", views_logon.ax_add, name="p_general.logon"),
    path("logon/c2/", views_logon.ax_delete, name="p_general.logon"),
    path("logon/c3/", views_logon.ax_update, name="p_general.logon"),
    path("logon/c4/", views_logon.ax_query, name="p_general.logon"),
    # 展现company的数据
    path("company/data/", views_company.data, name="p_general.company.data"),
    path("company/data2/", views_company.scrollView_data, name="p_general.company.scrollView_data"),
    path('company/c1/', views_company.ax_add, name='p_general.company.add'),
    path('company/c2/', views_company.ax_delete, name='p_general.company.delete'),
    path('company/c3', views_company.ax_update, name='p_general.company.update'),
    path('company/c4/', views_company.ax_query, name='p_general.company.query'),
    path('area_combo_list/', views.area_combo_list, name='area_combo_list'),
    path('test/', views_test.page_test, name='page_test'),
    # path('main/', views.page_main, name='example.page_main'),

]
