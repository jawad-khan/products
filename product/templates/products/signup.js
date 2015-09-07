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

            $("#username").val("");
            $("#email").val("");
            $("#password").val("");
            $("#phone").val("");
            alert("User created successfully")
            window.open("login.html", "_self");
        },
        error: function (error) {
            alert(error.responseText);
        }
    });

}
$(document).ready(function () {

    $("#signup").click(signup);

});