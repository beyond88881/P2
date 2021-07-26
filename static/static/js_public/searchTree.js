//树形菜单搜索方法
// https://www.cnblogs.com/cuijj/p/5867354.html
    function searchTree(treeObj,parentNode,searchCon){
        var children;
        for(var i=0;i<parentNode.length;i++){ //循环顶级 node
            children = $(treeObj).tree('getChildren',parentNode[i].target);//获取顶级node下所有子节点
            if(children){ //如果有子节点
                for(var j=0;j<children.length;j++){ //循环所有子节点
                    if($(treeObj).tree('isLeaf',children[j].target)){ //判断子级是否为叶子节点,即不是父节点
                        if(children[j].text.indexOf(searchCon)>=0){ //判断节点text是否包含搜索文本                    
                            selectNode(treeObj,children[j]); //设置此节点为选择状态
                            expandParent(treeObj,children[j]); //设置此节点所有父级展开
                            break;
                        }
                    }
                }
            }else{
                if(parentNode[i].text.indexOf(searchCon)>=0){
                    selectNode(treeObj,parentNode[i]);pinmupingm
                    expandParent(treeObj,parentNode[i]);
                    break;
                }
            }
        }
    };

    // 然后是 标记为选择状态 和 展开所有父级 的两个方法 selectNode , expandParent
    function selectNode(treeObj,node){
        $(treeObj).tree('select',node.target);           
    };

    function expandParent(treeObj,node){
        var parent = node;
        var t = true;
        do {
            parent = $(treeObj).tree('getParent',parent.target); //获取此节点父节点
            if(parent){ //如果存在
            t=true;
            $(treeObj).tree('expand',parent.target);
        }else{
            t=false;
        }
        }while (t);           
    };

//调用搜索方法

function sysTextSearch(){
    var search_content = $('#sysText').val(); //得到搜索的文件
//            if(search_content == ''){
//                $('#treelist').tree('expandAll'); //展开所有
//            }else{
        var roots=$('#treelist').tree('getRoots'); //得到tree顶级node
        searchTree($('#treelist'),roots, search_content);
//            }
}