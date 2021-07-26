import json

from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.db import connection

from static.static.py_public.publicMethod1 import CJsonEncoder


@csrf_exempt
def page_test(request):
    return render(request, 'projectManagement/proMag/test.html')