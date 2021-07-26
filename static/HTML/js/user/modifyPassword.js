
    $(function () {
        // while ($("#password2_2").length <= 0){//2、判断循环条件;
        //     // document.write(num+"<br />");//3、执行循环体操作；
        //     // num++;//4、更新循环变量；
        // }
        $('#userNameId2').iTextbox({
            width: 200,
            readonly: true
        });

        $('#userName2').iTextbox({
            width: 200,
            readonly: true
        });
        $('#password2_1').iPasswordbox({
            width: 200,
            required: true,
            validType: 'minLength[6]'
        });
        $('#password2_2').iPasswordbox({
            width: 200,
            required: true,
            validType: "equals['#password']"
        });
        alert("fresh");
    })