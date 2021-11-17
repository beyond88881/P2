$('#cc').iCombobox({
        data:[{id:1,text:'大专'},{id:2,text:'本科'},{id:3,text:'研究生'},{id:4,text:'博士生'}],
        valueField:'id',
        textField:'text',
        limitToList:false,
        editable:true,
        // mode:local,
        // filter: function(q, row){
        //         var opts = $(this).iCombobox('options');
        //         return row[opts.textField].indexOf(q) == 0;
        // }
});

