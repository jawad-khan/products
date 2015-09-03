function product_html(data) {
    return ('<tr id=' + data.id + '>' +
    '<td><input class = "name" type="text" readonly value=' + data.Name + '></td> ' +
    '<td><input class="detail" type="text" readonly value=' + data.Detail + '></td>' +
    '<td><input class="price" type="text" readonly value=' + data.Price + '></td>' +
    '</tr>');
}
function append_product(data) {
    var html_string = product_html(data);
    $("#main").append(html_string) ;

}


function fill() {
    $.ajax({
        type: 'GET',
        url: base_path+'app/my_products/',
        headers:{"Authorization": "Token "+ localStorage.getItem('Token')},
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

$(document).ready(function () {

    fill();
});