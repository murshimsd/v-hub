function form_validation(){
var title = document.getElementById("title")
var s_title = document.getElementById("s_title")
var position = document.getElementById("position")
var s_position = document.getElementById("s_position")
var votes = document.getElementById("votes")
var s_votes = document.getElementById("s_votes")


valid_status=1


if (title.value == "") {
    valid_status = 0
    s_title.innerHTML = "Enter title"
    s_title.style.color = "red"
    s_position.style.display = "block"
   
    
}
else {
    valid_status = 1
    s_title.style.display = "none"

}

if (position.value == "") {
    valid_status = 0
    s_position.innerHTML = "enter position"
    s_position.style.color = "red"
    s_position.style.display = "block"
    
}
else {
    valid_status = 1
    s_position.style.display = "none"
}

if (votes.value == "") {
    valid_status = 0
    s_votes.innerHTML = "enter your-city"
    s_votes.style.color = "red"
    s_votes.style.display = "block"
    
}
else {
    valid_status = 1
    s_votes.style.display = "none"
}
if(valid_status==0){
    return false
}
}






$(document).ready(function() {
    $('#position').on('blur', function() {
        var position = $(this).val();
        var titleId = $('#title').val();

        if (position && titleId) {
            $.ajax({
                type: 'GET',
                url: '/validate_position/',
                data: {
                    'position': position,
                    'title_id': titleId
                },
                success: function(response) {
                    if (!response.valid) {
                        $('#s_position').text(response.message).css({"color":"red"});
                    } else {
                        $('#s_position').empty();
                    }
                }
            });
        }
    });
});