    $(function () {

        $('#password').keyup(function (event) {
            if (event.keyCode == "13") {
                $("#login").trigger("click");
                return false;
            }
        });

        $("#login").on("click", function () {
            submitForm();
        });

        function submitForm() {
            if (navigator.appName == "Microsoft Internet Explorer" &&
                    (navigator.appVersion.split(";")[1].replace(/[ ]/g, "") == "MSIE6.0" ||
                    navigator.appVersion.split(";")[1].replace(/[ ]/g, "") == "MSIE7.0" ||
                    navigator.appVersion.split(";")[1].replace(/[ ]/g, "") == "MSIE8.0")
            ) {
                alert("您的浏览器版本过低，请使用360安全浏览器的极速模式或IE9.0以上版本的浏览器");
            } else {
                var formData = {
                    username: $('#username').val(),
                    password: $('#password').val(),
                    check_code: $('#check_code').val(),
                    referer: $('#referer').val()
                };
                // 获取 token
                //var token = $("input[name='_csrf']").val();
                //var headers = {"X-CSRF-TOKEN": token}

                $.ajax({
                    type: 'POST',
                    url: '/general/logon/',
                    contentType: "application/json; charset=utf-8",
                    data: JSON.stringify(formData),
                    //headers:headers,
                    success: function (data) {
                        if (data.statusCode == 200) {
                            //location.href = '/system/index/index?portal=${portal}';
                            location.href = data.referer;
                        } else if(data.statusCode == 300) {
                            $('#myModal3').modal();
                            //alert("用户名或密码错误！");
                            $('#check_code1').trigger("click")
                        }else if(data.statusCode == 400) {
                            $('#myModal4').modal();
                            //alert("Account is not actived！Please contact admintration！");
                            $('#check_code1').trigger("click")
                        }else if(data.statusCode == 500) {
                            $('#myModal5').modal();
                            //alert("Validation Code is not correct！");
                            $('#check_code1').trigger("click")
                        }
                    },
                    error: function () {
                        $('#check_code').click()
                    }
                });
            }
        }

        $("#reset").on("click", function () {
            $("#username").val("");
            $("#password").val("");
        });
    });


    function modifyPwd2(){
        window.open ("/modifyPassword", "newwindow", "height=100, width=400, top=0, left=0, toolbar=no, menubar=no, scrollbars=no, resizable=no,location=no, status=no")
    }
    //修改密码 弹窗
    function modifyPwd() {
        var opts = {
            id: 'pwdDialog',
            title: 'Change Pass Word',
            width: 400,
            height: 300,
            iconCls: 'fa fa-key',
            //href:'//',
            href: 'modifyPassword/',//"./user/modifyPassword.html",//
            //content: content1,//$('#pwdDialog').load("/static/HTML/html/user/modifyPassword.html"),
            // href:'/static/HTML/html/user/modifyPassword.html',
            //onLoadSuccess:alert("ok"),
            onLoad: function(){
                  alert("onLoad");
                //$('#pwdDialog').html(content)
                //$('#pwdDialog').form.html("modifyPassword/");
                //$('#pwdDialog').HTML("/static/HTML/html/user/modifyPassword.html");
                //$('#t_modifyPassword').load("/static/HTML/html/user/modifyPassword.html");
            },
            //afterUpdate:alert("update"),
            //onMouseMove:function(){alert()} ,
            //content:"<iframe scrolling='auto' frameborder='0' src='modifyPassword/' style='width:100%; height:100%; display:block;'></iframe>",
            buttons: [{
                text: '确定',
                iconCls: 'fa fa-save',
                btnCls: 'topjui-btn-green',
                handler: function () {
                    if ($('#pwdDialog').form('validate')) {
                        if ($("#password").val().length < 6) {
                            $.iMessager.alert('警告', '密码长度不能小于6位', 'messager-warning');
                        } else {
                            var formData = $("#pwdDialog").serialize();
                            $.ajax({
                                url: '/static/HTML/json/response/success.json',
                                type: 'post',
                                cache: false,
                                data: formData,
                                beforeSend: function () {
                                    $.iMessager.progress({
                                        text: '正在操作...'
                                    });
                                },
                                success: function (data, response, status) {
                                    $.iMessager.progress('close');
                                    if (data.statusCode == 200) {
                                        $.iMessager.show({
                                            title: '提示',
                                            msg: '操作成功'
                                        });
                                        $("#pwdDialog").iDialog('close').form('reset');

                                    } else {
                                        $.iMessager.alert('操作失败！', '未知错误或没有任何修改，请重试！', 'messager-error');
                                    }
                                }
                            });
                        }
                    }
                }
            }, {
                text: '关闭',
                iconCls: 'fa fa-close',
                btnCls: 'topjui-btn-red',
                handler: function () {
                    $("#pwdDialog").iDialog('close');
                }
            }, {
                text: 'test',
                iconCls: 'fa fa-close',
                btnCls: 'topjui-btn-red',
                handler: function () {
                        alert("fresh");
                        $('#userNameId2').iTextbox({
                            width: 200,
                            readonly: true
                        });

                        $('#userName2').iTextbox({
                            width: 200,
                            readonly: true
                        });
                        $('#password2').iPasswordbox({
                            width: 200,
                            required: true,
                            validType: 'minLength[6]'
                        });
                        $('#password21').iPasswordbox({
                            width: 200,
                            required: true,
                            validType: "equals['#password']"
                        });
                    }
            }]
        };

        $('#' + opts.id).iDialog('openDialog',opts);
        //此两行是 重新设置title和href 解决二次打开dialog加载旧界面的问题
        //$('#' + opts.id).dialog('setTitle', _title);
        // $('#' + opts.id).dialog('options').href = './user/modifyPassword.html'//"/static/HTML/html/user/modifyPassword.html"//'modifyPassword/';

        // $('#' + opts.id).dialog('refresh','modifyPassword/');
        //$('#' + opts.id).Dialog("refresh");
        // modifyPassword();
};

    function readHTML(urlInfo){
        $.ajax({
        async:false,
        url : urlInfo,//"aa.html“,
        success : function(result){
        alert(result);
        }
        });
        }
    //注册新用户 弹窗
    function regist() {
        var opts = {
            id: 'registDialog',
            title: '修改密码',
            width: 400,
            height: 300,
            iconCls: 'fa fa-key',
            href: '/modifyPassword',
            buttons: [{
                text: '确定',
                iconCls: 'fa fa-save',
                btnCls: 'topjui-btn-green',
                handler: function () {
                    if ($('#registDialog').form('validate')) {
                        if ($("#password").val().length < 6) {
                            $.iMessager.alert('警告', '密码长度不能小于6位', 'messager-warning');
                        } else {
                            var formData = $("#registDialog").serialize();
                            $.ajax({
                                url: '/static/HTML/json/response/success.json',
                                type: 'post',
                                cache: false,
                                data: formData,
                                beforeSend: function () {
                                    $.iMessager.progress({
                                        text: '正在操作...'
                                    });
                                },
                                success: function (data, response, status) {
                                    $.iMessager.progress('close');
                                    if (data.statusCode == 200) {
                                        $.iMessager.show({
                                            title: '提示',
                                            msg: '操作成功'
                                        });
                                        $("#registDialog").iDialog('close').form('reset');

                                    } else {
                                        $.iMessager.alert('操作失败！', '未知错误或没有任何修改，请重试！', 'messager-error');
                                    }
                                }
                            });
                        }
                    }
                }
            }, {
                text: '关闭',
                iconCls: 'fa fa-close',
                btnCls: 'topjui-btn-red',
                handler: function () {
                    $("#registDialog").iDialog('close');
                }
            }]
        };
        $('#' + opts.id).iDialog('openDialog', opts);
        // 验证开始需要向网站主后台获取id，challenge，success（是否启用failback）
        $.ajax({
        url: "/accounts/pc-geetest/register?t=" + (new Date()).getTime(), // 加随机数防止缓存
        type: "get",
        dataType: "json",
        success: function (data) {
            // 使用initGeetest接口
            // 参数1：配置参数
            // 参数2：回调，回调的第一个参数验证码对象，之后可以使用它做appendTo之类的事件
            initGeetest({
                gt: data.gt,
                challenge: data.challenge,
                product: "popup", // 产品形式，包括：float，embed，popup。注意只对PC版验证码有效
                offline: !data.success // 表示用户后台检测极验服务器是否宕机，一般不需要关注
                // 更多配置参数请参见：http://www.geetest.com/install/sections/idx-client-sdk.html#config
            }, handlerPopup);
        }
    });
};
    //滑动验证
    var handlerPopup = function (captchaObj) {
        // 成功的回调
        captchaObj.onSuccess(function () {
            var validate = captchaObj.getValidate();
            var username = $('#username').val();
            var password = $('#password').val();
            console.log(username, password);
            $.ajax({
                url: "/accounts/login2/", // 进行二次验证
                type: "post",
                dataType: 'json',
                data: {
                    username: username,
                    password: password,
                    csrfmiddlewaretoken: $("[name='csrfmiddlewaretoken']").val(),
                    geetest_challenge: validate.geetest_challenge,
                    geetest_validate: validate.geetest_validate,
                    geetest_seccode: validate.geetest_seccode
                },
                success: function (data) {
                    console.log(data);
                    if (data.status) {
                        // 有错误，在页面上显示
                        $('.login-error').text(data.msg);
                    } else {
                        // 登录成功
                        location.href = data.msg;
                    }
                }
            });
        }) ;

        // 当点击登录按钮时，弹出滑动验证码窗口
        $("#login-button").click(function () {
            captchaObj.show();
        });

        // 将验证码加到id为captcha的元素里
        captchaObj.appendTo("#popup-captcha");
        // 更多接口参考：http://www.geetest.com/install/sections/idx-client-sdk.html
    };

    function changeImg(ths) {
        // 硬编码
        ths.src = 'check_code/?temp=' + Math.random();
        // $(ths).attr('src', 'check_code/?temp=' + Math.random());
        // $('#check_code1').attr('src', 'check_code/?temp=' + Math.random());
        // 使用命名空间，发送请求
        // ths.src = '{% url 'accounts:check_code' %}' + '?temp=' + Math.random();
    }

    $('#username, #password').focus(function () {
        // 将之前的错误清空
        $('.login-error').text('');
    });

    function modifyPwd3() {
        var opts = {
            id: 'box',
            title: 'Change Pass Word',
            width: 400,
            height: 300,
            iconCls: 'fa fa-key',
            href: 'modifyPassword/',
            buttons: [{
                text: '确定',
                iconCls: 'fa fa-save',
                btnCls: 'topjui-btn-green',
                handler: function () {
                    if ($('#box').form('validate')) {
                        if ($("#password2").val().length < 6) {
                            $.iMessager.alert('警告', '密码长度不能小于6位', 'messager-warning');
                        } else {
                            var formData = $("#box").serialize();
                            $.ajax({
                                url: '/static/HTML/json/response/success.json',
                                type: 'post',
                                cache: false,
                                data: formData,
                                beforeSend: function () {
                                    $.iMessager.progress({
                                        text: '正在操作...'
                                    });
                                },
                                success: function (data, response, status) {
                                    $.iMessager.progress('close');
                                    if (data.statusCode == 200) {
                                        $.iMessager.show({
                                            title: '提示',
                                            msg: '操作成功'
                                        });
                                        $("#box").iDialog('close').form('reset');

                                    } else {
                                        $.iMessager.alert('操作失败！', '未知错误或没有任何修改，请重试！', 'messager-error');
                                    }
                                }
                            });
                        }
                    }
                }
            }, {
                text: '关闭',
                iconCls: 'fa fa-close',
                btnCls: 'topjui-btn-red',
                handler: function () {
                    $("#box").iDialog('close');
                }
            }]
        };

        $('#' + opts.id).iDialog('openDialog', opts);
        //$('#' + opts.id).Dialog("refresh");
        // modifyPassword();
};