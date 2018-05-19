//global variables
let debuglog;


// let t=setInterval(timer,1000)
// function timer(){
//   test()
// }

// function test(){
// 	var xhttp = new XMLHttpRequest();
//   	xhttp.onreadystatechange = function() {
//     if (this.readyState == 4 && this.status == 200) {
//       callback(this.responseText);
//     }  
//   };
//   xhttp.open("GET", "/get",true);
//   xhttp.send();
  
//   xhttp.onerror = function(error) {
//     console.error('error')
//     rewritelabel(null,false)
// };
  

//   function callback(result){
//     r=JSON.parse(result);
//     if (debuglog){
//       console.log(r);  
//     }
    
//     rewritelabel(r,true)


//   }
  


function rewritelabel(data,flag){
    let ullist=document.getElementById("variableslist");
    let listI=ullist.getElementsByTagName("li")
    let listItem="item";
    for (let i=0;i<listI.length;i++){
      tempitem=document.getElementById(listItem+i.toString())
      if (flag){
      tempitem.innerHTML=data[i].toString()
      }
      else{
        tempitem.innerHTML='###'
      }
    }

}

function debugcheck(){
  debuglog=document.form1.Checkbox1.checked;
}

// window.onload=load;

// function load() {
//     var body = document.body,
//         tbl  = document.createElement('table');
//     // tbl.style.width  = '100px';
//     // tbl.style.border = '1px solid black';
//     tbl.setAttribute('id','VariblesTable')
//     tbl.setAttribute('class','w3-table w3-striped w3-bordered')
//     for(var i = 0; i < 8; i++){
//         var tr = tbl.insertRow();
//         for(var j = 0; j < 3; j++){
//                 var td = tr.insertCell();
//                 td.appendChild(document.createTextNode('Cell'));
//                 td.style.border = '1px solid black';
//         }
//     }
//     body.appendChild(tbl);
// }


function stationDelete(action){
    //create a form
    var form = document.createElement("form");

    form.action="stationCreate"
    form.setAttribute("method", "post");

//    for (var j in action){
//        var input = document.createElement("input");
//        input.setAttribute('type','hidden')
//        input.setAttribute('value',String(j))
//        input.setAttribute('name',action[j])
//        form.appendChild(input)
//
//    }

    var input =document.createElement("input");
    input.setAttribute('type','hidden')
    input.setAttribute('value',action[0])
    input.setAttribute('name',action[1])
    form.appendChild(input)

    form.style.display="none"
    document.body.appendChild(form)

    form.submit('del')

    document.body.removeChild(form)

    console.log(action)

}