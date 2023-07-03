

$(document).ready(function() {
    $('#position').on('blur', function() {
        var position = $(this).val();
        var titleId = $('#title').val();

        if (position && titleId) {
            $.ajax({
                type: 'GET',
                url: "{% url 'school_admin:validate_position' %}",
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