function create(event) {
    event.preventDefault();
    if ($("#address").val()) {
        $.ajax({
            type: 'POST',
            url: base_path + 'app/address/',
            dataType: 'json',
            headers: {"Authorization": "Token " + localStorage.getItem('Token')},
            data: {"address": $("#address").val(), "country": $("#country").val()},
            success: function (data, status) {
                $("#address").val("");
                append_address(data);
            },
            error: show_alerts
        });


    }
    else {
        show_alerts({"Error": "please Enter all the fields"});
    }

}

function append_address(data) {
    $("#main").append('<tr><td><input class = "address" type="text" readonly value=' + data.address + '></td> ' +
    '<td><input class = "country" type="text" readonly value=' + data.country + '></td>' +
    '</tr>')

}

function fill() {

    $.ajax({
        type: 'GET',
        url: base_path + 'app/address/',
        headers: {"Authorization": "Token " + localStorage.getItem('Token')},
        dataType: 'json',
        success: function (data, status) {
            for (address in data) {
                append_address(data[address]);

            }

        },
        error: error_response
    });

}


$(document).ready(function () {

    $("#create").click(create);
    fill();

});