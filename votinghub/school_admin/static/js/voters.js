$("#email").keyup(function(){
    $.ajaxSetup({
            headers: {

                "X-CSRFToken": '{{ csrf_token }}'

            }
        })

        $.ajax({

            url : "{% url 'school_admin:check_mail' %}",
            method : 'POST',
            data : {
                "voterEmail" : $(this).val()

            },
            success : function(response){
                let exist = response.email_exist
                if (exist == true){

                    $("#span_mail").html('email already exist').css({"color":"red"})

                }
              
            }



        })
})