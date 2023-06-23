// email check
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





//  search_voter
 $(document).ready(function () {
    // Get the search input element
    const $searchInput = $('#search-input');

    // Event listener for input change
    $searchInput.on('input', function () {
        // Get the search query
        const searchQuery = $searchInput.val();

        // Create and send the AJAX request
        $.ajax({
            url: "{% url 'school_admin:search_voters' %}",
            type: 'GET',
            data: { search: searchQuery },
            dataType: 'json',
            success: function (results) {
                // Process the results and update the table or perform other actions
                console.log(results);

                // Example: Update the table with search results
                const $tableBody = $('.data_table tbody');
                $tableBody.empty();

                results.forEach(function (voter) {
                    const $row = $('<tr>');
                    $row.append('<td>' + voter.f_name + '</td>');
                    $row.append('<td>' + voter.l_name + '</td>');
                    $row.append('<td><img src="' + voter.photo_url + '" alt="" style="height: 40px;width: 40px;"></td>');
                    $row.append('<td>' + voter.password + '</td>');
                    $row.append('<td>' +
                        '<button type="button" class="btn btn-secondary" style="box-sizing: border-box; border: 1px solid black;" data-bs-toggle="modal" data-bs-target="#exampleModal2"><i class="fa fa-edit"></i>edit</button>' +
                        '<div class="modal fade" id="exampleModal2" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">' +
                        '<div class="modal-dialog">' +
                        '<div class="modal-content mbody">' +
                        '<div class="modal-header">' +
                        '<h1 class="modal-title fs-5" id="exampleModalLabel" style="margin-left: 15px;">update password</h1>' +
                        '<button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>' +
                        '</div>' +
                        '<div class="modal-body">' +
                        '<table>' +
                        '<tr>' +
                        '<td><label for="">Name : </label></td>' +
                        '<td><span name="namess">' + voter.f_name + '</span><br></td>' +
                        '</tr>' +
                        '<tr>' +
                        '<td><label for="">Password : </label></td>' +
                        '<td><input type="text" name="passwrds" value="password"></td>' +
                        '</tr>' +
                        '</table>' +
                        '</div>' +
                        '<div class="modal-footer">' +
                        '<button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>' +
                        '<button type="button" class="btn btn-primary">Save changes</button>' +
                        '</div>' +
                        '</div>' +
                        '</div>' +
                        '</div>' +
                        '<span>' +
                        '<a href="/remove-voter/' + voter.id + '"><button type="button" class="btn table_delet" data-bs-dismiss="modal"><i class="fa fa-trash"></i>delete</button></a>' +
                        '</span>' +
                        '</td>');

                    $tableBody.append($row);
                });
            }
        });
    });
});