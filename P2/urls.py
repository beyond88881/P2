"""P2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
import captcha
import django
# import patterns as patterns
from django.contrib import admin
# import captcha.urls
from django.contrib.auth.decorators import login_required
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns
from django.utils.translation import gettext_lazy as _
# from django.urls import url

#  javascript_catalog中使用的是 javascript_catalog，2.x是使用的JavaScriptCatalog
# from django.views.i18n import javascript_catalog
from django.views.generic import TemplateView
from django.views.i18n import JavaScriptCatalog
from . import views as views1
from p_general import views as views2
# import xadmin
from django.urls import NoReverseMatch, reverse

urlpatterns = i18n_patterns(
    # path('rosetta/', include('rosetta.urls')),
    path('admin/', admin.site.urls),
    path('', views1.login, name="login"),
    path('modifyPassword/', views1.modifyPassword, name="modifyPassword"),
    path('main', views1.ax_login, name='ax_login'),
    path('logout', views1.ax_logout, name='ax_logout'),
    # path('admin/', admin.site.urls, name='admin2'),
    path('general/', include('p_general.urls', namespace='p_general')),
    path('accounts/',  include('registration.backends.simple.urls'), name='registration'),
    path('captcha/', include('captcha.urls')),
    path('check_code/', views1.check_code, name='check_code'), #获取验证码
    # path('', login_required.as_views(), name="index")

    # path('example/', include('example.urls', namespace='example')),
    # path('start/', include('category.urls', namespace='category')),
    # path('proMag/', include('projectManagement.urls', namespace='projectManagement_1')),
    # path('purchase/',include('purchase.urls', namespace='purchase')),
    # path('i18n/', include('django.conf.urls.i18n')),
    # path('jsi18n/',JavaScriptCatalog.as_view(packages=['report']),name='javascript-catalog'),
    # path('jsi18n',JavaScriptCatalog.as_view(packages=['jsi18n']),name='javascript-catalog'),
    # 在模板中加入脚本tag：<script type="text/javascript" src="{% url 'javascript-catalog' %}"></script>
    # 其中的jsi18n是app,是settings.py中定义的INSTALLED_APP里当前web应用的名称
    # url(r'^jsi18n/$', JavaScriptCatalog, js_info_dict),
)
# 没有i18n_patterns的pattern则不会在url前增加语言类型来进行指定语言，
# 在网址上输入-- http://localhost:8000/report_normal/report1/
# 则仍为-- http://localhost:8000/zh-hans/report/report1/
# path(r'^jsi18n/(?P<packages>\S+)/$', django.views.i18n.JavaScriptCatalog, name='jsi18n'),
urlpatterns += (
    path('jsi18n/', JavaScriptCatalog.as_view(packages=['report.jscripti18n']), name='jsi18n'),
    path('general/', include('p_general.urls', namespace='report_normal')),
    # path('captcha/', include('captcha.urls')),
    # path('refresh_captcha/', views.refresh_captcha),
    # url(r'^i18n/', include('django.conf.urls.i18n'))
    # path('jsi18n/', django.views.i18n.JavaScriptCatalog, js_info_dict),

)
urlpatterns += [
               ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# js_info_dict = {
#     'domain': 'djangojs',
#     'packages': ('report.jscripti18n',),
# }
# urlpatterns += ['', url(r'^jsi18n/$', JavaScriptCatalog, name="js_info_dict"),
# ]

#
#
# js_info_dict = {
#     'packages': ('jsi18n',),
# }
#
# urlpatterns += ('',
#     path('jsi18n/', django.views.i18n.JavaScriptCatalog, js_info_dict),
# )
# compile your messages like this before internationalized:django-admin.py makemessages -a -d djangojs

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
