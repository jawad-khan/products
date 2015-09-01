function product_html(data) {
    return ('<tr id=' + data.id + '>' +
    '<td><input class = "name" type="text" readonly value=' + data.Name + '></td> ' +
    '<td><input class="detail" type="text" readonly value=' + data.Detail + '></td>' +
    '<td><input class="price" type="text" readonly value=' + data.Price + '></td>' +
    '</tr>');
}
function append_product(data, append) {
    var html_string = product_html(data);
    append == undefined ? $("#main").append(html_string) : $("#main").html(html_string);

}


function fill() {
    if ($("#user").val()) {
        $.ajax({
            type: 'GET',
            url: 'http://localhost:8000/app/my_products/' + $("#user").val() + '/',
            dataType: 'json',
            success: function (data, status) {
                for (product in data) {
                    append_product(data[product]);

                }

            },
            error: function (error) {
                alert(error.responseText);
            }
        });
    }
    else {
        alert("Enter a valid user id to view addresses");
    }

}

$(document).ready(function () {

});