var base_path = 'http://localhost:8000/';
function logout(e) {
    e.preventDefault();
    $.ajax({
        type: 'POST',
        url: base_path + 'app/logout/',
        headers: {"Authorization": "Token " + localStorage.getItem('Token')},
        dataType: 'json',
        success: function (data, status) {
            localStorage.removeItem("Token");
            window.open("login.html", "_self");

        },
        error: function (error) {
            alert(error.responseText);
        }
    });

}

function error_response(error) {
    if (error.status == 401 || error.status == 403) {
        window.open("login.html", "_self");
    }


}

function set_errors(errors) {
    for (var key in errors) {
        if (errors.hasOwnProperty(key) && key.length > 1) {
            $("#" + key + "_error").text(errors[key]);
            set_errors(errors[key]);
        }
    }
}

function show_alerts(error) {
    var data= error.responseJSON;
    var text = ''
    for (var key in data) {

        if (data.hasOwnProperty(key) && key.length > 2) {
            text = text + '<strong>' + key + ':</strong>' + data[key] + '</br>';
        }
        $("#alert-message").html(text);
        $("#alert").show(100)
    }
}

function fields_error_response(error) {
    if (error.status == 401 || error.status == 403) {
        window.open("login.html", "_self");
    }
    var errors = error.responseJSON;
    set_errors(errors);

}


function readURL(input, name) {

    if (input.files && input.files[0]) {
        var reader = new FileReader();

        reader.onload = function (e) {
            $(name).attr('src', e.target.result);
        }

        reader.readAsDataURL(input.files[0]);
    }
}
function close_alert() {
    $("#alert").hide();
}


$(document).ready(function () {

    $("#logout").click(logout);
    $("#alert_cross").click(close_alert);

});