import json

from django.db.models import Max, Min
from django.db.models.functions import math
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from p_general.models import models_company
from static.static.py_public.publicMethod1 import CJsonEncoder
from goto import with_goto
# from projectManagement.models.models_project import Project
import math


def scrollView_data(request, info=''):
    # page = isset(_POST['page']) ? intval(_POST['page']): 1
    # rows = isset(_POST['rows']) ? intval(_POST['rows']): 50
    page_thePage = int(request.POST.get('page'))
    page_rows = int(request.POST.get('rows'))
    eaList = []
    # date_default_timezone_set('UTC')
    project = list(models_company.objects.all())
    for row in project:
        eaList.append({
            "id": row.id,
            "id_associatedcompany": row.id_associatedcompany,
            "roleproperty": row.roleproperty,
            "property": row.property,
            "companyname": row.companyname,
            "companyname_cn": row.companyname_cn,
            "shortname": row.shortname,
            "innerused": row.innerused,
            "basic_currency": row.basic_currency,
            "language_code": row.language_code,
            "date_created": row.date_created,
            "timeupdated": row.timeupdated,
            "expiry_date": row.expiry_date,
            "country": row.country,
            "state": row.state,
            "city": row.city,
            "street_address": row.street_address,
            "location_type": row.location_type,
            "id_companyhq": row.id_companyhq,
            "id_co_oper": row.id_co_oper
        })
    total = len(eaList)

    for i in range(1, page_rows, 1):
        index = i + (page_thePage - 1) * rows

        json_data_list = {'rows': eaList, 'total': total, 'page_Number': 1, 'info': info}

    easyList = json.dumps(json_data_list, cls=CJsonEncoder)
    # easyList=easyList.join('[]')
    # return HttpResponse(easyList)
    if info == '':
        return HttpResponse(easyList, content_type="application/json; charset=utf-8")


@csrf_exempt
def data(request, info=''):
    hasPOSTinfo = False
    page_rows = 50
    if 'page' in request.POST and 'rows' in request.POST:
        page_thePage = int(request.POST.get('page'))
        # page_thePage += page_thePage
        page_rowsStr = float(request.POST.get('rows'))
        if math.isnan(page_rowsStr) == False:
            page_rows = int(request.POST.get('rows'))
        hasPOSTinfo = True
    # *****change point
    company = list(models_company.objects.all().order_by('id'))
    # model_to_dict(Project.objects.all())
    # paginator = Paginator(areas, page_rows)

    eaList = []
    # projectInfo = json.loads(project.information)
    for row in company:
        # *****change point
        eaList.append({
            "id": row.id,
            "id_associatedcompany": row.id_associatedcompany,
            "roleproperty": row.roleproperty,
            "property": row.property,
            "companyname": row.companyname,
            "companyname_cn": row.companyname_cn,
            "shortname": row.shortname,
            "innerused": row.innerused,
            "basic_currency": row.basic_currency,
            "language_code": row.language_code,
            "date_created": row.date_created,
            "timeupdated": row.timeupdated,
            "expiry_date": row.expiry_date,
            "country": row.country,
            "state": row.state,
            "city": row.city,
            "street_address": row.street_address,
            "location_type": row.location_type,
            "id_companyhq": row.id_companyhq,
            "id_co_oper": row.id_co_oper
        })
    total = len(eaList)
    # json_data_list = {'rows':eaList,'total':total}

    # eaList_len=json.dumps(paginator.count)
    # json_data_list = {'rows':eaList,'total':eaList_len}

    # 分页处理
    #  存储分页数据：一个页面的数据
    # rowPageList = []
    if hasPOSTinfo == True:
        page_newPage = page_thePage + 1

        if page_thePage == 1:  #  第1页
            if page_rows >= len(eaList):  # 第1页  数据未达到1页行数
                json_data_list = {'rows': eaList, 'total': total, 'page_Number': page_newPage, 'info': info}
            else:  # 第1页数据超到1页行数
                rowPageList = eaList[:page_rows]
                # for s in range(page_thePage * ):
                #     rowPageList.append(eaList[s])
                json_data_list = {'rows': rowPageList, 'total': total, 'page_Number': page_newPage, 'info': info}
        else:  #  非第1页
            ss = eaList[page_thePage * page_rows:]
            if len(ss) < page_rows:  #  非第1页  剩余数据未达到1页行数 
                json_data_list = {'rows': ss, 'total': total, 'page_Number': page_newPage, 'info': info}
            else:  # 剩余数据超过1页行数
                rowPageList = eaList[page_thePage * page_rows:page_newPage * page_rows]
                # for i in range(page_thePage * page_rows):
                #     rowPageList.append(ss[i])
                json_data_list = {'rows': rowPageList, 'total': total, 'page_Number': page_newPage, 'info': info}
    else:
        json_data_list = {'rows': eaList, 'total': total, 'page_Number': 1, 'info': info}

    easyList = json.dumps(json_data_list, cls=CJsonEncoder)
    # easyList=easyList.join('[]')
    # return HttpResponse(easyList)
    if info == '':
        return HttpResponse(easyList, content_type="application/json; charset=utf-8")
    else:
        return easyList
    # return render(request,
    #             'datagrid.html',{'data':easyList})


def ax_add(request):
    return _ax_crud(request, "add")


def ax_delete(request):
    return _ax_crud(request, "delete")


def ax_update(request):
    return _ax_crud(request, "update")


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
            models_company.objects.get(id=int(x)).delete()
    elif (type_case == 'update'):
        info = 'EDIT_OK'
        # *****change point
        dic = {
            'id': obj_POST.get('row[id]'),
            'id_associatedcompany': obj_POST.get('row[id_associatedcompany]'),
            'roleproperty': obj_POST.get('row[roleproperty]'),
            'property': obj_POST.get('row[property]'),
            'companyname': obj_POST.get('row[companyname]'),
            'companyname_cn': obj_POST.get('row[companyname_cn]'),
            'shortname': obj_POST.get('row[shortname]'),
            'innerused': obj_POST.get('row[innerused]'),
            'basic_currency': obj_POST.get('row[basic_currency]'),
            'language_code': obj_POST.get('row[language_code]'),
            'date_created': obj_POST.get('row[date_created]'),
            'timeupdated': obj_POST.get('row[timeupdated]'),
            'expiry_date': obj_POST.get('row[expiry_date]'),
            'country': obj_POST.get('row[country]'),
            'state': obj_POST.get('row[state]'),
            'city': obj_POST.get('row[city]'),
            'street_address': obj_POST.get('row[street_address]'),
            'location_type': obj_POST.get('row[location_type]'),
            'id_companyhq': obj_POST.get('row[id_companyhq]'),
            'id_co_oper': obj_POST.get('row[id_co_oper]')
        }
        obj_id = obj_POST.get('id')
        models_company.objects.filter(id=obj_id).update(**dic)
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
            models_company.objects.create(**dic)
        else:
            print(" is null_!")
    else:
        info = 'QUERY_OK'

    models_company.objects.update()
    page_thePage = int(request.POST.get('page')) - 1
    if 'rows' in request.POST:
        page_rows = int(request.POST.get('rows'))
    else:
        page_rows = int(request.POST.get('rows'))
    areas = models_company.objects.all().order_by('id')
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
