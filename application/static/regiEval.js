function regiEval() {
    let pwd1 = document.getElementById("registerPwd1");
    let pwd2 = document.getElementById("registerPwd2");
    const submitBtn = document.getElementById("registerSubmit");
    const labelBtn = document.getElementById("not-match");
    if (pwd2.value && pwd1.value != pwd2.value) {
        //Password not confirmed - disable submit
        submitBtn.style.display = "none";
        labelBtn.style.display = "inline-block";
        // changing colors
        pwd2.style.backgroundColor = "#FFA77B";
    } else {
        submitBtn.style.display = "inline-block";
        labelBtn.style.display = "none";
        pwd2.style.backgroundColor = "#FFFFFF";
    }}