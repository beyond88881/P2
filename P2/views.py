from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate
from django.contrib import auth
from django.contrib import messages
from django.template import RequestContext
# Create your views here.
from django.template.loader import get_template
from django.views.decorators.csrf import csrf_exempt
from static.static.py_public.publicMethod1 import CJsonEncoder
from django.http import HttpResponse
import json

# 验证码所需的引用
from django.shortcuts import render, redirect, HttpResponse
from P2.check_code import create_validate_code
from io import BytesIO
from django.contrib import auth
from django.http import JsonResponse


def login(request):
    return render(request, "html/login.html")


@login_required
@csrf_exempt
def main_page(request):
    # template = get_template('TMPL_main.html')
    request_context = RequestContext(request)
    request_context.push(locals())
    # html = template.render()
    return render(request, "html/TMPL_main.HTML")


@login_required
@csrf_exempt
def test_first_page(request):
    return render(request, "html/test_first_page.HTML")


@login_required
@csrf_exempt
def first_page(request):
    return render(request, "html/first_page.HTML")


@login_required
@csrf_exempt
def jsonInfo_menu1(request):
    menuID = request.GET.get('menu')
    levelid = request.GET.get('levelid')
    return render(request, "json/menu/menu_" + menuID + ".json")


@login_required
@csrf_exempt
def jsonInfo_menu2(request, menuID):
    return render(request, "json/menu/menu_" + menuID + ".json")


@csrf_exempt
def jsonInfo_productList(request):
    return render(request, "json/data/product-list.json")

@csrf_exempt
def modifyPassword(request):
    template = get_template('html/user/modifyPassword.html')
    html = template.render({})
    return HttpResponse(html, content_type=" text/html")
    # return render(request, "html/user/modifyPassword.html")
    # return render_to_response(request, "html/user/modifyPassword.html")

@csrf_exempt
def ax_login(request):
    # if request.method == 'POST':
    #     login_form = forms.LoginForm(request.POST)
    #     if login_form.is_valid():
    # login_name = request.POST['username'].strip()
    # login_password = request.POST['password']
    info = json.loads(request.body.decode('utf-8'))
    login_name = info['username']
    login_password = info['password']
    code = info['check_code']
    # login_name = request.POST.get('username')
    # login_password = request.POST.get('password')
    # 用户输入的验证码与 session 中取出的验证码比较
    if code.upper() == request.session.get('valid_code').upper():
        user = authenticate(username=login_name, password=login_password)
        if user is not None:
            if user.is_active:
                auth.login(request, user)
                json_data_list = {'username': login_name, 'password': login_password, 'referer': 'general/p1/',
                                  'statusCode': 200}
                messages.add_message(request, messages.SUCCESS, '成功登录了')
            else:
                json_data_list = {'username': 'login_name', 'password': 'login_password', 'referer': '',
                                  'statusCode': 300}
                messages.add_message(request, messages.WARNING, '账号尚未启用')
        else:
            json_data_list = {'username': 'login_name', 'password': 'login_password', 'referer': '',
                              'statusCode': 400}
            messages.add_message(request, messages.WARNING, '登录失败')
    else:
        json_data_list = {'username': 'login_name', 'password': 'login_password', 'referer': '',
                          'statusCode': 500}
        messages.add_message(request, messages.WARNING, '验证码输入错误')
    easyList = json.dumps(json_data_list, cls=CJsonEncoder)
    return HttpResponse(easyList, content_type="application/json; charset=utf-8")
    #     else:
    #         messages.add_message(request, messages.INFO, '请检查输入的字段内容')
    # else:
    #     login_form = forms.LoginForm()
    # return redirect('index.html')
    # template = get_template('index.html')
    # request_context = RequestContext(request)
    # request_context.push(locals())
    # html = template.render(request_context)
    # return HttpResponse(html)
    # return HttpResponse(request, content_type="application/json; charset=utf-8")

@csrf_exempt
def ax_logout(request):
    auth.logout(request)
    messages.add_message(request, messages.INFO, "成功注销了")
    return redirect('/')


"""
验证码
"""
def check_code(request):
    """
    获取验证码
    :param request:
    :return:
    """
    stream = BytesIO()
    # 生成图片 img、数字代码 code，保存在内存中，而不是 Django 项目中
    img, code = create_validate_code()
    img.save(stream, 'PNG')

    # 写入 session
    request.session['valid_code'] = code
    print(code)
    return HttpResponse(stream.getvalue())


def login2(request):
    """
    登录视图
    :param request:
    :return:
    """
    if request.method == 'POST':
        ret = {'status': False, 'message': None}
        username = request.POST.get('username')
        password = request.POST.get('password')

        # 获取用户输入的验证码
        code = request.POST.get('check_code')
        p = request.POST.get('p')


        # 用户输入的验证码与 session 中取出的验证码比较
        if code.upper() == request.session.get('valid_code').upper():
            # 验证码正确，验证用户名密码是否正确
            user_obj = auth.authenticate(username=username, password=password)
            if user_obj:
                # 验证通过，则进行登录操作
                # 封装到 request.user 中
                auth.login(request, user_obj)
                return redirect('accounts:home')
            else:
                ret['status'] = True
                ret['message'] = '用户名或密码错误'
                return render(request, 'accounts/login.html', ret)
        else:
            ret['status'] = True
            ret['message'] = '验证码错误'
        return render(request, 'accounts/login.html', ret)

    return render(request, 'accounts/login.html')
