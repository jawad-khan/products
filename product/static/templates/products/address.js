function create() {
    if ($("#address").val() && $("#user").val()) {
        $.ajax({
            type: 'POST',
            url: 'http://localhost:8000/app/address/' + $("#user").val() + '/',
            dataType: 'json',
            data: {"address": $("#address").val(), "user": $("#user").val()},
            success: function (data, status) {
                $("#address").val("");
                append_address(data);
            },
            error: function (error) {
                alert(error.responseText);
            }
        });


    }
    else {
        alert("Please enter the required fields");
    }

}

function append_address(data) {
    $("#main").append('<tr><td><input class = "address" type="text" readonly value=' + data.address + '></td> </tr>')

}

function fill() {
    if ($("#user").val()) {

        $.ajax({
            type: 'GET',
            url: 'http://localhost:8000/app/address/' + $("#user").val() + '/',
            dataType: 'json',
            success: function (data, status) {
                for (address in data) {
                    append_address(data[address]);

                }

            },
            error: function (error) {
                alert(error.responseText);
            }
        });
    }
    else {
        alert("Enter a valid user id")
    }

}


$(document).ready(function () {

    $("#create").click(create);

});