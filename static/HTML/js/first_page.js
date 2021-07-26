    function progressFormatter(value, rowData, rowIndex) {
        var htmlstr = '<div id="p" class="topjui-progressbar progressbar" data-options="value:' + value + '" style="width: 398px; height: 26px;">';
        htmlstr += '<div class="progressbar-text" style="width: 398px; height: 26px; line-height: 26px;">' + value + '%</div>';
        htmlstr += '<div class="progressbar-value" style="width: ' + value + '%; height: 26px; line-height: 26px;">';
        htmlstr += '</div>';
        htmlstr += '</div>';
        return htmlstr;
    }

    function operateFormatter(value, row, index) {
        var htmlstr = '<button class="layui-btn layui-btn-xs" onclick="openEditDiag(\'' + row.uuid + '\')">编辑</button>';
        htmlstr += '<button class="layui-btn layui-btn-xs layui-btn-danger" onclick="deleteRow(\'' + row.uuid + '\')">删除</button>';
        return htmlstr;
    }

    function openEditDiag(uuid) {
        var $editDialog = $('<form id="myDialog"></form>'); // 创建form表单元素

        $editDialog.iDialog({
            title: '编辑数据',
            width: 950,
            height: 550,
            closed: false,
            cache: false,
            href: _ctx + '/html/complex/dialog_edit.html?uuid=' + uuid,
            modal: true,
            fit:true,
            buttons: [{
                text: '保存',
                iconCls: 'fa fa-save',
                btnCls: 'topjui-btn-blue',
                handler: ajaxSubmit // 调用下面自定义方法ajaxSubmit()
            }, {
                text: '关闭',
                iconCls: 'fa fa-close',
                btnCls: 'topjui-btn-red',
                handler: function () {
                    $editDialog.iDialog('close');
                }
            }],
            onLoad: function () {
                //加载表单数据
                $.getJSON(_ctx + 'static/TopJUI/json/datagrid/product-detail.json?uuid=' + uuid, function (data) {
                    $editDialog.form('load', data);
                });
            }
        });
    }
    function ajaxSubmit() {
        // 1. 显示进度条（提交时请使用进度条 或者 禁用'提交'按钮，防止因为网络延迟用户重复提交）
        $.iMessager.progress({'text': '请求中……'});

        // 2. 提交操作
        $('#myDialog').iForm('submit', {
            url: _ctx + '/json/response/success.json',
            onSubmit: function (param) {  /* param.p1 = 'param 用于提交额外的参数';*/
                var isValid = $(this).iForm('validate'); //  提交数据表单数据时进行表单验证
                if (!isValid) {
                    $.iMessager.progress('close');  // 如果表单是无效的则隐藏进度条
                }
                return isValid;    // 返回false终止表单提交
            },
            success: function (res) {
                var data = JSON.parse(res); // 字符串格式JSON 转换成 对象格式JSON
                setTimeout(function () { // 模拟请求延迟3秒（使用的时候请自行去掉）
                    if (data.statusCode == 200) { // 后台返回状态值
                        $.iMessager.show({title: '我的消息', msg: data.message, timeout: 5000, showType: 'slide'});// '消息窗口'组件
                        $("#productDg").iDatagrid('reload');// 刷新下表格数据
                        $('#myDialog').dialog('destroy');// 销毁dialog面板
                    } else {
                        $.iMessager.show({title: '我的消息', msg: data.message, timeout: 5000, showType: 'slide'});// '消息窗口'组件
                    }
                    $.iMessager.progress('close');  // 如果提交完成则隐藏进度条
                }, 3000);
            }
        });
    }

    function deleteRow(uuid) {
        $.iMessager.alert('操作提示', '请根据具体情况编写代码，如ajax删除请求，请求失败提示，请求成功提示，请求成功后刷新表格等！', 'messager-info');
    }

    $(function () {
        var productDg = {
            type: 'datagrid',
            id: 'productDg'
        };

        $("#productDg").iDatagrid({
            url: '/general/json/productList/',
            // fitColumns:true,
            // remoteSort:false,
            fit:true,
            frozenColumns: [[
                {field: 'name', title: '商品名称', sortable: true},
                {field: 'code', title: '商品编号', sortable: true}
            ]],
            columns: [[
                {field: 'uuid', title: 'UUID', checkbox: true},
                {field: 'spec', title: '规格型号', sortable: true},
                {field: 'sale_price', title: '销售单价', sortable: true},
                {field: 'rate', title: '完成率', sortable: true, formatter: progressFormatter},
                {field: 'operate', title: '操作', formatter: operateFormatter}
            ]],
            filter: [{
                field: 'name',
                type: 'textbox',
                op: ['contains', 'equal', 'notequal', 'less', 'greater']
            }, {
                field: 'code',
                type: 'combobox',
                options: {
                    valueField: 'label',
                    textField: 'value',
                    data: [{
                        label: '2103',
                        value: '2103'
                    }, {
                        label: '5103',
                        value: '5103'
                    }, {
                        label: '1204',
                        value: '1204'
                    }]
                },
                op: ['contains', 'equal', 'notequal', 'less', 'greater']
            }, {
                field: 'spec',
                type: 'combobox',
                options: {
                    valueField: 'label',
                    textField: 'value',
                    multiple: true,
                    data: [{
                        label: 'KC-W200SW',
                        value: 'KC-W200SW'
                    }, {
                        label: '白色LR-1688BY-2',
                        value: '白色LR-1688BY-2'
                    }, {
                        label: '银灰色BCD-339WBA 339',
                        value: '银灰色BCD-339WBA 339'
                    }]
                },
                op: ['contains', 'equal', 'notequal', 'less', 'greater']
            }]
        });

        $("#add").iMenubutton({
            method: 'openDialog',
            extend: '#productDg-toolbar',
            iconCls: 'fa fa-plus',
            dialog: {
                id: 'userAddDialog',
                title: '多选项卡布局的表单',
                href: _ctx + '/html/complex/dialog_add.html',
                buttonsGroup: [
                    {
                        text: '保存',
                        url: _ctx + '/json/response/success.json',
                        iconCls: 'fa fa-plus',
                        handler: 'ajaxForm',
                        btnCls: 'topjui-btn-brown'
                    }
                ]
            }
        });

        $("#edit").iMenubutton({
            method: 'openDialog',
            extend: '#productDg-toolbar',
            iconCls: 'fa fa-pencil',
            btnCls: 'topjui-btn-green',
            grid: productDg,
            dialog: {
                title: '普通布局的表单',
                height: 550,
                href: _ctx + '/html/complex/dialog_edit.html?uuid={uuid}',
                url: _ctx + '/json/datagrid/product-detail.json?uuid={uuid}',
                buttonsGroup: [
                    {
                        text: '更新',
                        url: _ctx + '/json/response/success.json',
                        iconCls: 'fa fa-save',
                        handler: 'ajaxForm',
                        btnCls: 'topjui-btn-green'
                    }
                ]
            }
        });

        $("#batchUpdate").iMenubutton({
            method: 'doAjax',
            extend: '#productDg-toolbar',
            iconCls: 'fa fa-cog',
            btnCls: 'topjui-btn-red',
            grid: {
                type: 'datagrid',
                id: 'productDg',
                param: 'uuid:uuid,code',
                uncheckedMsg: '请先勾选你要批量操作的数据'
            },
            confirmMsg:'您确认执行该操作？',
            url:_ctx + '/json/response/success.json'
        });

        $("#delete").iMenubutton({
            method: 'doAjax',
            extend: '#productDg-toolbar',
            iconCls: 'fa fa-trash',
            btnCls: 'topjui-btn-brown',
            confirmMsg: '这个是勾选复选框实现多条数据的Ajax删除提交操作，提交grid.param中指定的参数值',
            grid: {
                type: 'datagrid',
                id: 'productDg',
                uncheckedMsg: '请先勾选要删除的数据',
                param: 'uuid:uuid,code:code'
            },
            url: _ctx + '/json/response/success.json'
        });

        $("#filter").iMenubutton({
            method: 'filter',
            extend: '#productDg-toolbar',
            btnCls: 'topjui-btn-black',
            grid: productDg
        });

        $("#search").iMenubutton({
            method: 'search',
            extend: '#productDg-toolbar',
            btnCls: 'topjui-btn-blue',
            grid: productDg
        });

        $("#import").iMenubutton({
            method: 'import',
            extend: '#productDg-toolbar',
            btnCls: 'topjui-btn-orange',
            uploadUrl: _ctx + '/json/response/upload.json',
            url: _ctx + '/json/response/success.json'
        });

        $("#export").iMenubutton({
            method: 'export',
            extend: '#productDg-toolbar',
            btnCls: 'topjui-btn-red',
            url: _ctx + '/json/response/export.html'
        });

        $("#openTab").iMenubutton({
            method: 'openTab',
            btnCls: 'topjui-btn-purple',
            tab: {
                title: '这是新的Tab窗口',
                href: _ctx + '/html/complex/panel_add.html'
            },
            grid: productDg
        });

        $("#openWindow").iMenubutton({
            method: 'openWindow',
            extend: '#productDg-toolbar',
            btnCls: 'topjui-btn-green',
            href: 'http://www.topjui.com?uuid={uuid}',
            grid: productDg
        });

        $('#request').iMenubutton({
            method: 'request',
            btnCls: 'topjui-btn-brown',
            url: _ctx + '/json/response/success.json'
        });

        $('#myFun').iMenubutton({
            btnCls: 'topjui-btn-black',
            onClick: myQuery
        });

        $('#queryBtn').iMenubutton({
            method: 'query',
            iconCls: 'fa fa-search',
            btnCls: 'topjui-btn-blue',
            form: {id: 'queryForm'},
            grid: {type: 'datagrid', 'id': 'productDg'}
        });
    });

    // 自定义方法
    function myQuery() {
        // 提示信息
        $.iMessager.alert('自定义方法', '自定义方法被执行了！', 'messager-info');

        var checkedRows = $('#productDg').iDatagrid('getChecked');
        console.log(checkedRows);

        var selectedRow = $('#productDg').iDatagrid('getSelected');
        console.log(selectedRow);

        // 提交参数查询表格数据
        $('#productDg').iDatagrid('reload', {
            name: $('#name').iTextbox('getValue'),
            code: $('#code').iTextbox('getValue')
        });
    }
