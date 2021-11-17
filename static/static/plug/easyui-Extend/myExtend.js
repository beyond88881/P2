	// easyui的combobox扩展--默认选择第一行
    $.extend($.fn.combobox.methods, {
		selectedIndex: function (jq, index) {
			if (!index) {
				index = 0;
			}
			$(jq).combobox({
				onLoadSuccess: function () {
					var opt = $(jq).combobox('options');
					var data = $(jq).combobox('getData');

					for (var i = 0; i < data.length; i++) {
						if (i == index) {
							$(jq).combobox('setValue', eval('data[index].' + opt.valueField));
							break;
						}
					}
				}
			});
		},
		getFocus:function (jq,caller) {
			$(jq).bind('focus',caller);
			return jq.each(function () {
				var that=this;
				return $(jq);
			})
			// return this;
		}
	});

// (function($){
// 	$.parser.plugins.push("combobox");
// 	$.fn.editgrid=function(options,param){
//         //如果传入的options为字符串，则调用的是组件的方法
// 		if(typeof options == "string"){
// 			var method = $.fn.editgrid.methods[options];
// 			if(method){//判断方法是否存在
// 				return method(this,param);//如果方法存在，则调用方法
// 			} else {
//                 //如果方法不存在，可在此处提示或输出
//             }
// 		}
//         //通过代码定义组件
// 		options = options || {};
// 		return this.each(function(){//可能存在多个组件，需对每一个组件进行定义
// 			var opts = $.extend({},$.fn.datagrid.parseOptions(this),options);//获得父级组件的options并与传入的配置整合
// 			$.fn.datagrid.call($(this),$.extend(true,{
//                 //一下为自定义属性\事件等
// 				onDblClickRow:function(index){
// 					var records = $(this).editgrid('getRows');
// 					for(var i = 0;i<records.length;i++){
// 						if(i==index){
// 							$(this).editgrid('beginEdit',i);
// 							var editors = $(this).editgrid('getEditors',index);
// 							if(editors && editors.length > 0){
// 								editors[0].target.focus();
// 							}
// 						} else {
// 							$(this).editgrid('endEdit',i);
// 						}
// 					}
// 				},
// 				onAfterEdit:function(index){
// 					$(this).editgrid('updateRow',{index:index,row:{}});
// 				},
// 				getFocus:function () {
//
// 				}
// 			},opts));
// 		});
// 	};
// 	$.fn.editgrid.methods = $.extend({},$.fn.datagrid.methods,{//继承父级组件的方法，并增加或修改
// 		//完成编辑
// 		finishEdit:function(grid){
// 			var records = grid.editgrid('getRows');
// 			for(var i = 0;i<records.length;i++){
// 				grid.editgrid('endEdit',i);
// 			}
// 		},
// 		//新增记录
// 		addRecord:function(grid,record){
// 			var records = grid.editgrid("getRows");
// 			if(records){
// 				for(var i = 0;i<records.length;i++){
// 					grid.editgrid('endEdit',i);
// 				}
// 			}
// 			var index = records.length;
// 			grid.editgrid('insertRow',{
// 				index:index,
// 				row:record||{}
// 			});
// 			grid.editgrid('beginEdit',index);
// 			var editors = grid.editgrid('getEditors',index);
// 			if(editors && editors.length > 0){
// 				editors[0].target.focus();
// 			}
//
// 		},
// 		//删除选定的记录
// 		removeSelectedRecords:function(grid){
// 			while(true){
// 				var record = grid.editgrid('getSelected');
// 				if(record == null){
// 					return;
// 				}
// 				grid.editgrid("deleteRow",grid.editgrid('getRowIndex',record));
// 			}
// 		}
// 	});
// })(jQuery);