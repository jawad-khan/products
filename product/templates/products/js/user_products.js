function product_html_li(data) {
    return ('\
    <li class="media " id="' + data.id + '"> \
        <div class="media-left "> \
          <a href="#"> \
            <img class="media-object" style="width: 100px; height 1250px; "  src=' + data.image + ' alt="Product image"> \
          </a> \
        </div> \
        <div class="media-body media-middle"> \
            <h4 class="media-heading" >' + data.name + '</h4> \
            <p>' + data.detail + '</p> \
            <span class="badge" style="height:5%;width:5%; font-size:18px;">' + data.price + '$ </span> \
         </div> \
    </li>');
}

function append_product(data) {
    var html_string = product_html_li(data);
    $("#main").append(html_string);

}

function fill() {
    $.ajax({
        type: 'GET',
        url: base_path + 'app/my_products/',
        headers: {"Authorization": "Token " + localStorage.getItem('Token')},
        dataType: 'json',
        success: function (data, status) {
            for (product in data) {
                append_product(data[product]);

            }

        },
        error: error_response
    });
}

$(document).ready(function () {

    fill();
});