function form_validation(){
    var college_name = document.getElementById("college_name1")
var valid_college_name = document.getElementById("s_college")
var email_address = document.getElementById("emails")
var valid_email_address = document.getElementById("s_emails")
// var password = document.getElementById("password1")
// var valid_password = document.getElementById("valid_password1")
var username = document.getElementById("user_name")
var valid_username = document.getElementById("valid_username")
var city = document.getElementById("city")
var valid_city = document.getElementById("s_city")
var state1 = document.getElementById("state1")
var state2 = document.getElementById("state2")


valid_status=1
console.log(college_name.value)

if (college_name.value == "") {
    console.log('inside')
    valid_status = 0
    valid_college_name.innerHTML = "Enter Name"
    valid_college_name.style.color = "red"
    valid_college_name.style.display = "block"
   
    
}
else {
    valid_status = 1
    valid_college_name.style.display = "none"

}
if (email_address.value.match(/^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/)==null) {
    valid_status = 0
    valid_email_address.innerHTML = "Enter Valid E-mail"
    valid_email_address.style.color = "red"
    valid_email_address.style.display = "block"
    
}
else {
    valid_status = 1
    valid_email_address.style.display = "none"
}
// if (password.value.match(/^[A-Za-z]\w{7,14}$/)==null) {
//     valid_status = 0
//     valid_password.innerHTML = "Invalid Password"
//     valid_password.style.color = "red"
//     valid_password.style.display = "block"
   
// }
// else {
//     valid_status = 1
//     valid_password.style.display = "none"
// }
if (username.value == "") {
    valid_status = 0
    valid_username.innerHTML = "enter user-name"
    valid_username.style.color = "red"
    valid_username.style.display = "block"
    
}
else {
    valid_status = 1
    valid_username.style.display = "none"
}
if (city.value == "") {
    valid_status = 0
    valid_city.innerHTML = "enter your-city"
    valid_city.style.color = "red"
    valid_city.style.display = "block"
    
}
else {
    valid_status = 1
    valid_city.style.display = "none"
}
if (state1.value == "") {
    valid_status = 0
    state2.innerHTML = "enter your-city"
    state2.style.color = "red"
    state2.style.display = "block"
    
}
else {
    valid_status = 1
    state2.style.display = "none"
}
if(valid_status==0){
    return false
}
}