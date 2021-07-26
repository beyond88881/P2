import json


from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.db import connection
from static.static.py_public.publicMethod1 import CJsonEncoder




@csrf_exempt
def area_combo_list(request):
    eaList = []
    # for p in Area.objects.raw('SELECT id, area FROM area '):
    #     eaList.append({
    #         "area":p.area
    #     })
    cursor = connection.cursor()
    cursor.execute('SELECT id,CONCAT(area,"-",city) AS area_name FROM area ORDER BY area, city')
    # cursor.execute('SELECT area.id, area.area FROM area GROUP BY area.id, area.area')
    # row = cursor.fetchone()
    for p in cursor.fetchall():
        eaList.append({
            "id": p[0],
            "area_name": p[1]
        })
    # total = json.dumps(len(eaList))
    # json_data_list = {'rows': eaList, 'total': total}
    # easyList = json.dumps(json_data_list, cls=CJsonEncoder)
    easyList = json.dumps(eaList, cls=CJsonEncoder)
    # return HttpResponse(easyList, content_type="application/json; charset=utf-8")
    return HttpResponse(easyList, content_type="application/json; charset=utf-8")
