


$(document).ready(function() {
    $("#upload_image").click(function (e) {
        e.preventDefault();
        form_data =new FormData($("#image_form").get(0));

        $.ajax({
            type: 'POST',
            url: base_path+'app/upload_image/',
            data: form_data,
            cache: false,
            headers:{"Authorization": "Token "+ localStorage.getItem('Token')},
            processData: false, // Don't process the files
            contentType: false,
            success: function (data) {

                alert("Profile picture has been saved successfully");
            },
            error: function (error) {
                alert(error.responseText);
            }
        });
    });
});
