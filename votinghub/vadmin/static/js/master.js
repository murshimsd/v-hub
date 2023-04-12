
function addcollege_validation(){
var college_name = document.getElementById("college_name")
var valid_college_name = document.getElementById("valid_college_name")
var email_address = document.getElementById("email_address")
var valid_email_address = document.getElementById("valid_email_address")
var password = document.getElementById("password")
var valid_password = document.getElementById("valid_password")
status=1


if (college_name.value == "") {
    status = 0
    valid_college_name.innerHTML = "Enter Name"
    valid_college_name.style.color = "red"
    valid_college_name.style.display = "block"
}
else {
    status = 1
    valid_college_name.style.display = "none"

}
if (email_address.value.match(/^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/)==null) {
    status = 0
    valid_email_address.innerHTML = "Enter Valid E-mail"
    valid_email_address.style.color = "red"
    valid_email_address.style.display = "block"
}
else {
    status = 1
    valid_email_address.style.display = "none"
}
if (password.value.match(/^[A-Za-z]\w{7,14}$/)==null) {
    status = 0
    valid_password.innerHTML = "Invalid Password"
    valid_password.style.color = "red"
    valid_password.style.display = "block"
}
else {
    status = 1
    valid_password.style.display = "none"
}
if(status==0){
    return false
}
}
