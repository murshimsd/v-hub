$(document).ready(function() {
        
    $('#election-title-select').change(function() {
        var selectedTitleId = $(this).val(); // Get the selected title ID

        // Send an AJAX request to fetch the positions for the selected title
        $.ajax({
            url: "{% url 'school_admin:get_positions' %}",  // Replace with the URL for your AJAX endpoint
            method: 'GET',
            data: { title_id: selectedTitleId },
            success: function(response) {
                // Clear the positions select element
                $('#position-select').empty();

                // Append the positions to the positions select element
                response.positions.forEach(function(position) {
                    $('#position-select').append('<option value="' + position.id + '">' + position.position + '</option>');
                });
            },
            error: function(xhr, textStatus, errorThrown) {
                console.error('Error:', errorThrown);
            }
        });
    });
});