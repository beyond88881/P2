// https://blog.csdn.net/HUXU981598436/article/details/17577637?locationNum=2
$(function(){

            try{
                $(".datagrid-body").scroll(function(){
                      var sheight = $(this)[0].scrollHeight;
                      var top=$(this)[0].scrollTop;
                      var height=$(this).height();
                      //判断是否到达底部
                      document.title='top:'+(top+height)+' heigth:'+(sheight-20);
                      if((top+height)+20==sheight){
                            document.title=datagrid.datagrid('options').url;
                            //请求json
                            //page;// 当前页
                            //rows;// 每页显示记录数
                            //拼接表单的值
                            var url=datagrid.datagrid('options').url;
                            url+='?params=xxx';
                            var params='';
                            $("#searchForm").find('input').each(function(index){
                                var obj=$(this);
                                if(obj.prop('name')!=''&&obj.val()!=''){
                                    params+='&'+obj.prop('name')+'='+obj.val();
                                }
                            });
                            //获取页码、每次默认加载10条
                            var num=10;
                            //获取行数
                            var row=datagrid.datagrid('getRows').length;

                            var page=(row/num)+1; //求出下一页
                            //$.post();
                            url+=params+'&page='+page+'&rows=10';

                            //请求数据
                            $.post(url,function(data){
                                var json=$.parseJSON(data).rows;

                                for(var i=0;i<json.length;i++){
                                    //自动拼接字段和赋值

                                    var row='';
                                    for(var item in json[i]){
                                        row+='"'+item+'":'+'"'+json[i][item]+'",';
                                    }
                                    row=row.substring(0,row.length-1);
                                    row='{'+row+'}';
                                    row=$.parseJSON(row);
                                    datagrid.datagrid("appendRow",row);
                                }
                            });

                        }else{
                            document.title='滚动条没有到达底部';
                        }
                });
            }
            catch(e){
                alert(e);
            }
        });