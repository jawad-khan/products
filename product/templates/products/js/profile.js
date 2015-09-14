function load_profile() {
    $.ajax({
        type: 'GET',
        headers: {"Authorization": "Token " + localStorage.getItem('Token')},
        url: base_path + 'app/profile/',
        dataType: 'json',
        success: function (data, status) {
            $("#name").text(data.user.username);
            $("#email").text(data.user.email);
            $("#phone").text(data.phone);
            $("#image").attr("src", data.image);
            $("#cover").attr("src", data.cover);


        },
        error: error_response
    });
}

function upload_profile_image(e) {
    e.preventDefault();
    form_data = new FormData($("#image_form").get(0));

    $.ajax({
        type: 'POST',
        url: base_path + 'app/upload_image/',
        data: form_data,
        cache: false,
        headers: {"Authorization": "Token " + localStorage.getItem('Token')},
        processData: false, // Don't process the files
        contentType: false,
        success: function (data) {
            $("#image").attr("src", data.image);
            $("#profile_image_popup").hide();
        },
        error: error_response
    });
}

function upload_cover_image(e) {
    e.preventDefault();
    form_data = new FormData($("#cover_form").get(0));

    $.ajax({
        type: 'POST',
        url: base_path + 'app/upload_cover/',
        data: form_data,
        cache: false,
        headers: {"Authorization": "Token " + localStorage.getItem('Token')},
        processData: false, // Don't process the files
        contentType: false,
        success: function (data) {
            $("#cover").attr("src", data.cover);
            $("#cover_image_popup").hide();
        },
        error: error_response
    });
}


function toggle_profile_popup() {
    $("#profile_image_popup").toggle();
}


function toggle_cover_popup() {
    $("#cover_image_popup").toggle();
}

$(document).ready(function () {
    load_profile();
    $("#upload_image").click(upload_profile_image);
    $("#upload_cover").click(upload_cover_image);
    $("#change_profile_link").click(toggle_profile_popup);
    $("#change_cover_link").click(toggle_cover_popup);
    $("#close_popup").click(toggle_profile_popup);
    $("#local_image").change(function () {
        readURL(this, "#page_display");

    });
    $("#local_cover").change(function () {
        readURL(this, "#cover_display");

    });

});