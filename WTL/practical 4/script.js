var i = document.getElementById("input");
i.value = '';
var reset = false;

function btnFunction(s) {
    if (reset) {
        i.value = '';
        i.style.border = "none";
        reset = false;
    }
    if (s == 'c') {
        i.value = '';
    } else if (s == '=') {
        try {
            i.value = eval(i.value);
            if (i.value == 'Infinity' || i.value == '-Infinity' || i.value == 'NaN') {
                i.style.border = "1px solid red";
                reset = true;
                throw 1;
            } else {
                reset = false;
            }
        } catch (error) {
            i.style.border = "1px solid red";
            reset = true;
            return;
        }
    } else if (s == 'back') {
        i.value = i.value.slice(0, -1);
    }
    i.style.border = "none";
}

function btnClick(s) {
    if (reset) {
        i.value = '';
        i.style.border = "none";
        reset = false;
    }
    i.value += s;
}