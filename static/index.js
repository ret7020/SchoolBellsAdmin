const openBellManager = (url) => {
    let api_endpoint = `${url}/api/login`;
    var formData = new FormData();
    formData.append("password", "12345")
    sendForm(api_endpoint, formData).then(function(resp){
        if (resp["status"]){
            console.log("OK");
        }else{
            //document.getElementById("invalid_password").style.display = "block";
            console.log("FAIL");
        }
    })
    //window.open(url, '_blank').focus();
}