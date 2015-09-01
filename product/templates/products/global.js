

function logout()
{
    $.ajax({
        type: 'POST',
        url: 'http://localhost:8000/app/logout/',
        headers:{"Authorization": "Token "+ localStorage.getItem('Token')},
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




$(document).ready(function () {

    $("#logout").click(logout)
});