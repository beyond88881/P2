// <script src="/static/TopJUI/static/plugins/jquery/jquery.min.js"></script>
// document.write(" <script language=\"javascript\" src=\"../z_ref_source/jquery-1.6.4/jquery.js\"> </script>");
var i = 0;
function outerFn(){
  function innnerFn(){
       i++;
       console.log(i);
  }
  return innnerFn;
}
var inner1 = outerFn();
var inner2 = outerFn();
inner1();
inner2();
inner1();
inner2();

var a = [1,2,3]; //定义并初始化数组
for(i in a){ //遍历数组
     a[i] = function(){ //通过闭包改变数组元素的值，使每个数组元素的值为该元素下标的平方值
          return i*i; } }
console.log(a[0]()); //返回4
console.log(a[1]()); //返回4
console.log(a[2]()); //返回4

function Point(x,y){                                                 //构造对象
this.x = x;
this.y = y;
}
Point.name = "类属性"                                   //构造对象的属性
var p1 = new Point(100,200);                   //实例化对象
var p2 = new Point(300,400);                   //实例化对象
console.log(Point.name);                                               //直接读取构造对象的属性
console.log(p1.name);                                                    //但是不能够通过实例对象来读取构造对象的

function Point(x,y){                                                 //构造对象
this.x = x;                                                    //对象属性
this.y = y;                                                                 //对象属性
}
var point = new Point(100,200); //实例构造对象
console.log(point.x);

function Point(x, y){                                               //构造函数
    this.x = x;                                                    //对象属性
    this.y = function(){                                      //对象方法
    return y;
    }
}


Point.prototype.x = "a";                                      //原型属性
Point.prototype.y = function(){              //原型方法
return "b";
}
var p1 = new Point();
var p1 = new Point(1, 2);
p1.x = true;                                                         //自定义实例属性
p1.y = function(){                                               //自定义实例方法
return false;
}
console.log(p1.x);
console.log(p1.y());

var p1 = new Point(1, 2);
p1.x = true;

p1.y = function(){

return false;
}
delete p1.x;  //删除属性 x
delete p1.y;  //删除属性 y
console.log(p1.x);  //返回原型属性值
console.log(p1.y()); //调用原型方法


(function($){
    $.extend($.fn,{

    parent : function(options){

    var arr = [];
    $.each(this, function(index, value){
    arr.push(value.parentNode);
    });
    arr = $.unique(arr);
    return this.pushStack(arr); //返回新创建的 jQuery 对象，而不是修 改后的当前 jQuery 对象
    }
    })
})(jQuery);

elem.attr('title')
elem.attr('data-toggle')
