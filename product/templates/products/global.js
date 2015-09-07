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
            alert("You have successfully logged out");
            window.open("login.html", "_self");

        },
        error: function (error) {
            alert(error.responseText);
        }
    });

}

function error_response(error) {
    alert(error.responseText);
    if (error.status == 401 || error.status == 403) {
        window.open("login.html", "_self");
    }


}

$(document).ready(function () {

    $("#logout").click(logout);


});