(function(){
       if(1>2,2>3)//false,false
       {
          console.log ('1>2,2>3 - true ');
       }
       else
       {
           console.log('1>2,2>3 - false ');
       }

       if(1>2,2<3)//false,true
       {
           console.log("1>2,2<3 - true");
       }
       else{
           console.log('1>2,2<3 - false ');
       }
       if(1<2,2>3)//true,false
       {
           console.log('1<2,2>3 - true ');
       }
       else
       {
           console.log('1<2,2>3 - false ');
       }

       if(1<2,2<3)//true,true
       {
           console.log("1<2,2<3 - true");
       }
       else{
           console.log('1<2,2<3 - false ');
       }

       if(1>2 || 2>3 , 5>2)
       {
           console.log('1>2||2>3, 5>2 - true ');
       }
       else
       {
           console.log('1>2||2>3, 5>2 - false ');
       }

       if(1>2 || 2>3 , 5<2)
       {
           console.log('1>2||2>3, 5<2 - true ');
       }
       else
       {
           console.log('1>2||2>3, 5<2 - false ');
       }
  })()

function test(){
  var a,b = 3;
}
// test();
// b; // b is not defind

function test(){
  var a,b = 3;
  return function(){
     console.log(b); // a = underfind
  }
}
test().call(null); // 3
// 在流程控制语句中
if(a = 3, true) { console.log(a) } //  3

if(a = 3, false) { console.log(a) } // no
console.log(a) // 3
