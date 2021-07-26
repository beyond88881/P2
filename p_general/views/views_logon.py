import json

from django.db.models import Max, Min
from django.db.models.functions import math
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from p_general.models.models_authUser import AuthUser as User
from static.static.py_public.publicMethod1 import CJsonEncoder
from goto import with_goto
# from projectManagement.models.models_project import Project
import math
from django.core.mail import EmailMessage
from django.template import RequestContext
from django.template import Context, Template
from django.template.loader import get_template
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect
from django.contrib import messages
# from mysite import models, forms
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib import auth
from django.contrib.auth.decorators import login_required


def index(request, pid=None, del_pass=None):
    if request.user.is_authenticated():
        username = request.user.username
        useremail = request.user.email
    messages.get_messages(request)
    template = get_template('index.html')
    request_context = RequestContext(request)
    request_context.push(locals())
    html = template.render(request_context)
    return HttpResponse(html)


@login_required(login_url='/login')
def userinfo(request):
    if request.user.is_authenticated():
        username = request.user.username
        try:
            userinfo = User.objects.get(username=username)
        except:
            pass
    template = get_template('userinfo.html')
    html = template.render(locals())
    return HttpResponse(html)




@login_required(login_url='/login/')
def posting(request):
    if request.user.is_authenticated():
        username = request.user.username
        useremail = request.user.email

    if request.method == 'POST':
        post_form = forms.PostForm(request.POST)
        if post_form.is_valid():
            message = "您的信息已保存，要等管理员启用后才看得到。"
            post_form.save()
            return HttpResponseRedirect('/list/')
        else:
            message = '如要张贴信息，则每一个字段都要填...'
    else:
        post_form = forms.PostForm()
        message = '如要张贴信息，则每一个字段都要填...'

    template = get_template('post2db.html')
    request_context = RequestContext(request)
    request_context.push(locals())
    html = template.render(request_context)

    return HttpResponse(html)


@csrf_exempt
def ax_add(request):
    return _ax_crud(request, "add")

@csrf_exempt
def ax_delete(request):
    return _ax_crud(request, "delete")

@csrf_exempt
def ax_update(request):
    return _ax_crud(request, "update")

@csrf_exempt
def ax_query(request):
    return _ax_crud(request, "query")


@with_goto
@csrf_exempt
def _ax_crud(request, type_case, id=0):
    # type_case = str(request.POST.get('type'))
    obj_POST = request.POST
    print("POST")
    print(request.POST)
    if (type_case == 'delete'):
        info = 'REMOVE'
        us_id = str(request.POST.get('row'))
        for x in us_id.split(','):
            # Project.objects.filter(id=int(x)).delete()
            # *****change point
            User.objects.get(id=int(x)).delete()
    elif (type_case == 'update'):
        info = 'EDIT_OK'
        # *****change point
        dic = {
            'id': obj_POST.get('row[id]'),
            'password': obj_POST.get('row[password]'),
            'last_login': obj_POST.get('row[last_login]'),
            'id': obj_POST.get('row[id]'),
            'password': obj_POST.get('row[password]'),
            'last_login': obj_POST.get('row[last_login]'),
            'is_superuser': obj_POST.get('row[is_superuser]'),
            'username': obj_POST.get('row[username]'),
            'first_name': obj_POST.get('row[first_name]'),
            'last_name': obj_POST.get('row[last_name]'),
            'email': obj_POST.get('row[email]'),
            'is_staff': obj_POST.get('row[is_staff]'),
            'is_active': obj_POST.get('row[is_active]'),
            'date_joined': obj_POST.get('row[date_joined]'),
            'id_co_oper': obj_POST.get('row[id_co_oper]'),
            'rowupdatedtime': obj_POST.get('row[rowupdatedtime]'),
            'rowcreated': obj_POST.get('row[rowcreated]')
        }
        obj_id = obj_POST.get('id')
        User.objects.filter(id=obj_id).update(**dic)
        # return HttpResponse("Edit_OK")
    elif (type_case == 'add'):
        info = 'ADD_NEW_OK'
        # add_save_user
        if request.method == "POST":
            Area_email = obj_POST['row[email]']
            Area_dt = obj_POST['row[dt]']
            Area_mark = obj_POST['row[mark]']
            # Area_email=request.POST.get('email')
            # Area_dt=request.POST.get('dt')
            # Area_mark=request.POST.get('mark')
            dic = {'email': Area_email, 'dt': Area_dt, 'mark': Area_mark}
            User.objects.create(**dic)
        else:
            print(" is null_!")
    else:
        if User.objects.count()>1:
            info = 'QUERY_OK'
        else:
            info = 'QUERY_NONE'

    if (type_case != 'query'):
        User.objects.update()
    page_thePage = int(request.POST.get('page')) - 1
    if 'rows' in request.POST:
        page_rows = int(request.POST.get('rows'))
    else:
        page_rows = int(request.POST.get('rows'))
    areas = User.objects.all().order_by('id')
    # total=areas.count
    basic_info1 = areas.aggregate(Max('id'), Min('id'))
    id_max = basic_info1['id__max']
    id_min = basic_info1['id__min']
    # paginator = Paginator(areas, page_rows)
    eaList = []
    n = 0
    for row in areas:
        eaList.append({
            'id': row.id,
            'id_associatedcompany': row.id_associatedcompany,
            'roleproperty': row.roleproperty,
            'property': row.property,
            'companyname': row.companyname,
            'companyname_cn': row.companyname_cn,
            'shortname': row.shortname,
            'innerused': row.innerused,
            'basic_currency': row.basic_currency,
            'language_code': row.language_code,
            'date_created': row.date_created,
            'timeupdated': row.timeupdated,
            'expiry_date': row.expiry_date,
            'country': row.country,
            'state': row.state,
            'city': row.city,
            'street_address': row.street_address,
            'location_type': row.location_type,
            'id_companyhq': row.id_companyhq,
            'id_co_oper': row.id_co_oper
        })
        n = n + 1
        if row.id == id_max:
            new_line_poisition = n
    total = json.dumps(len(eaList))
    # 分页处理
    #  存储分页数据：一个页面的数据
    rowPageList = []
    if (info == 'ADD_NEW_OK'):  # 如果是插入方式，则需要把新插入的记录最后一页进行确认
        page_newPage = math.ceil(new_line_poisition / page_rows)
        page_thePage = page_newPage - 1
    else:
        page_newPage = page_thePage + 1

    row_Number = 0
    if (page_thePage == 0) and (page_rows >= len(eaList)):  #  第1页且数据未达到1页行数
        row_Number = new_line_poisition
        json_data_list = {'rows': eaList, 'total': total, 'page_Number': page_thePage, 'row_Number': row_Number,
                          'info': info}
        # else:
        #     goto .end
        #     row_Number = new_line_poisition
        #     rowPageList = eaList[:page_rows]
        #     # for s in range(page_thePage * ):
        #     #     rowPageList.append(eaList[s])
        #     json_data_list = {'rows': rowPageList, 'total': total, 'page_Number': page_newPage, 'info': info}
    else:  #  非第1页或第1页数据超到1页行数
        # label .end
        ss = eaList[page_thePage * page_rows:]
        if (len(ss) < page_rows):  #  非第1页  剩余数据未达到1页行数 
            json_data_list = {'rows': ss, 'total': total, 'page_Number': page_newPage, 'info': info}
        else:  # 非第1页
            rowPageList = eaList[page_thePage * page_rows:page_newPage * page_rows]
            # for i in range(page_thePage * page_rows):
            #     rowPageList.append(ss[i])
            json_data_list = {'rows': rowPageList, 'total': total, 'page_Number': page_newPage, 'info': info}
    easyList = json.dumps(json_data_list, cls=CJsonEncoder)
    return HttpResponse(easyList, content_type="application/json; charset=utf-8")
