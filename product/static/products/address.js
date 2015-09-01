function create() {
    if ($("#address").val()) {
        $.ajax({
            type: 'POST',
            url: 'http://localhost:8000/app/address/',
            dataType: 'json',
            data: {"address": $("#address").val()},
            success: function (data, status) {
                $("#address").val("");
                $("#main").append('<td><input class = "address" type="text" readonly value=' + data.address + '></td> ')
            },
            error: function (error) {
                alert("Sorry,your request can not be completed ..  Try again!")
            }
        });


    }
    else {
        alert("Please enter the field");
    }

}


$(document).ready(function () {

    $("#create").click(create);

});