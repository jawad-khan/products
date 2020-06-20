function signup(e) {

    e.preventDefault();
    $.ajax({
        type: 'POST',
        url: base_path + 'app/signup/',
        dataType: 'json',
        data: {
            "username": $("#username").val(),
            "email": $("#email").val(),
            "password": $("#password").val(),
            "phone": $("#phone").val()
        },
        success: function (data, status) {
            localStorage.setItem("Token", data.token);
            window.open("profile.html", "_self");
        },
        error: fields_error_response
    });

}
$(document).ready(function () {

    $("#signup").click(signup);

});