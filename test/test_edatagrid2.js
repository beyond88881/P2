// 原文链接：https://blog.csdn.net/zhang18330699274/article/details/52195363
    $(function () {
        //当页面首次刷新的时候执行的事件
        initTable();
    });

    //实现保险信息DataGird控件的绑定操作
    function initTable(queryData) {
        $('#Insurance').iEdatagrid({            //定位到Table标签，Table标签的ID是test
            // fitColumns: true,
            id:'Insurance',
            url: '../static/TopJUI/json/config/config_1.json',  //指向后台的Action来获取当前用户的信息的Json格式的数据
            // title: '添加保险信息',           //表格标题
            // striped: true,               //斑马线效果
            // pagination: true,            //分页工具栏
            // rownumbers: true,            //显示行号
            idField:'uuid',
            reloadAfterSave:true,
            // onClickCell: onClickCell,    //点击单元格触发的事件（重要）
            // onAfterEdit: onAfterEdit,     //编辑单元格之后触发的事件（重要）
            // queryParams: queryData,
            // singleSelect: false,//异步查询的参数
            enableEditing: true,
            columns: [[
                // { field: 'ck', checkbox: true, align: 'left', width: 10 },
                { field: 'uuid', title: 'UUID', align: 'center' },
                { field: 'type', title: '类型',
                    editor:{
                        type:'textbox'
                        },
                        options:{required:true,height:30}
                    },
                { field: 'name', title: '名称', hidden: 'true' },
                { field: 'value', title: '数值', align: 'center' },
                { field: 'degree', title: '学历', sortable: true,
                    editor: {
                       type: 'combobox',
                       options: {
                           valueField: 'text',
                           textField: 'text',
                           // method: 'get',

                           // url: '/FreshQueryInfo/ReturnYears',
                           data:[{id:1,text:'大专'},{id:2,text:'本科'},{id:3,text:'研究生'},{id:4,text:'博士生'}],
                           required: true
                           // onSelect: function (rec) {
                           //     //alert($(this).parent().parent().parent().parent().parent().parent().parent()[0].cells[4].innerText);
                           //     var preNum = $(this).parent().parent().parent().parent().parent().parent().parent()[0].cells[4].innerText; //获得保险金额（元/年）
                           //     var result = rec.text * preNum;    //计算总计
                           //     $(this).parent().parent().parent().parent().parent().parent().parent()[0].cells[6].innerText = result; //给总计赋值（则三步可以不用）
                           // }
                       }
                    }
                },
            //        { field: 'Count', title: '总计', width: 140, align: 'center' },
            // { field: 'insuranceRemark', title: '保险备注', width: 100, hidden: 'true' },
            //     { field: 'Comment', title: '备注', width: 100, hidden: 'true' },
            ]],
            onClickRow: onClickRow,
        });
    }
    // $.extend($.fn.datagrid.methods, {
    //     editCell: function (jq, param) {
    //         return jq.each(function () {
    //             var opts = $(this).datagrid('options');
    //             var fields = $(this).datagrid('getColumnFields', true).concat($(this).datagrid('getColumnFields'));
    //             for (var i = 0; i < fields.length; i++) {
    //                 var col = $(this).datagrid('getColumnOption', fields[i]);
    //                 col.editor1 = col.editor;
    //                 if (fields[i] != param.field) {
    //                     col.editor = null;
    //                 }
    //             }
    //             $(this).datagrid('beginEdit', param.index);
    //             for (var i = 0; i < fields.length; i++) {
    //                 var col = $(this).datagrid('getColumnOption', fields[i]);
    //                 col.editor = col.editor1;
    //             }
    //         });
    //     }
    // });
    //
    // var editIndex = undefined;
    // //判断是否编辑结束
    // function endEditing() {
    //     if (editIndex == undefined) { return true }
    //     if ($('#Insurance').datagrid('validateRow', editIndex)) {
    //         $('#Insurance').datagrid('endEdit', editIndex);
    //         editIndex = undefined;
    //         return true;
    //     } else {
    //         return false;
    //     }
    // }
    //
    // //点击单元格触发的事件
    // function onClickCell(index, field) {
    //
    //     if (endEditing()) {
    //         $('#Insurance').datagrid('selectRow', index)
    //                 .datagrid('editCell', { index: index, field: field });
    //         editIndex = index;
    //     }
    // }
    //
    // //编辑完单元格之后触发的事件
    // function onAfterEdit(index, row, changes) {
    //     var insuranceCost = row.InsuranceCost;
    //     var years = row.Years;
    //     var total = insuranceCost * years;
    //     row.Count = total;
    //     $('#Insurance').datagrid('updateRow', { index: $('#Insurance').datagrid('getRowIndex', row), row: { name: 'Count' } });
    // }
    // //获取表格中的数据
    // function GetDate() {
    //     var rows = $('#Insurance').datagrid('getSelected');
    //     //初始化表单数据
    //     var insuranceCompany = rows.InsuranceCompany;
    //     var insuranceType = rows.InsuranceType;
    //     var insuranceCost = rows.InsuranceCost;
    //     var years = rows.Years;
    //     var Count = years * insuranceCost;
    //
    //     $('#Insurance').datagrid.Count('setValue', Count);
    //     alert(rows.Count);
    // }
    // //下一步
    // function NextStep() {
    //     //判断是否有选中行
    //     var row = $('#Insurance').datagrid('getChecked');
    //     if (!row || row.length == 0) {
    //         alert("请先选择您要购买的年限后选中要购买的保险！")
    //     }
    //     else {
    //         var insuranceCompany = row[0].InsuranceCompany;
    //         var insuranceType = row[0].InsuranceType;
    //         var insuranceCost = row[0].InsuranceCost;
    //         var InsuranceRemark = row[0].insuranceRemark;
    //         var Count = row[0].Count;
    //         var Year = row[0].Years;
    //         var Comment = row[0].Comment;
    //         var ID = row[0].Id;
    //
    //         $.ajax({
    //             type: "POST",
    //             url: "/FreshNewReport/AddInsurance",
    //             data: "InsuranceCompany=" + insuranceCompany + "&InsuranceType=" + insuranceType + "&InsuranceCost=" + insuranceCost + "&insuranceRemark=" + InsuranceRemark + "&UseCount=" + Count + "&Comment=" + Comment + "&ID=" + ID,
    //             success: function (data) {
    //                 if (data == true) {
    //                     window.location.href = "../FreshNewReport/Use"
    //                 }
    //                 else {
    //                     $.messager.alert('提醒', '保险购买失败！请重新购买');
    //                 }
    //             },
    //             error: function () {
    //                 $.messager.alert('提醒', '保险购买失败，请联系管理员！')
    //             }
    //         });
    //     }
    // }
    //
    // function LastStep() {
    //     window.location.href = "../FreshNewReport/StuEducation";
    // }

