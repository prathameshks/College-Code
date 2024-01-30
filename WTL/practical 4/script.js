var i = document.getElementById("input");
i.value = '';

function btnFunction(s){
    if(s == 'c'){
        i.value = '';
    }else if(s == '='){
        try {
            i.value = eval(i.value);
        } catch (error) {
            i.style.border = "1px solid red"; 
            return;
        }
    }else if(s== '^'){
        i.value += '**';
    }
    i.style.border = "none"; 
}

function btnClick(s){
    // console.log(s);
    i.value += s;
}