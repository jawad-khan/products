/**
 * Created by hafizmuhammadjawadkhan on 8/5/15.
 */

var staff = 0
function create() {
    if ($("#name").val() && $("#detail").val() && $("#price").val()) {
        $.ajax({
            type: 'POST',
            url: base_path + 'app/add_product/',
            dataType: 'json',
            headers: {"Authorization": "Token " + localStorage.getItem('Token')},
            data: {"name": $("#name").val(), "detail": $("#detail").val(), "price": $("#price").val()},
            success: function (data, status) {

                $("#name").val("");
                $("#detail").val("");
                $("#price").val("");

                append_user(data);
            },
            error: show_alerts
        });


    }
    else {
        show_alerts({"Error": "please Enter all the fields"})
    }

}


function toggle_product_popup() {

    id = $(this).parentsUntil("li").parent().attr("id");
    popup = $("#product_image_popup");
    $("#product-id").val(parseInt(id));

    popup.toggle();

}


function product_html_for_staff() {
    return ('<button class="btn  btn-primary edit_class" style=" margin-top:-5%;margin-left:4final px; width:16%; ">Edit</button> \
    <button class="btn  btn-primary delete_class" style=" margin-top:-5%;width:16%; ">Delete</button');

}

function product_html_li(data) {
    html = '<li class="media " id="' + data.id + '"> \
        <div class="media-left "> \
          <a href="#"> \
            <img class="media-object" style="width: 100px; height: 150px; "  src=' + data.image + ' alt="Product image"> \
          </a> ';
    if (staff) {
        html += '<input type="button" class="show_image_popup" value="change image" >'
    }

    html += ' </div> \
        <div class="media-body "> \
            <h4 class="media-heading name" style="width:14%;" >' + data.name + '</h4> \
            <p class="detail" style="width:14%;" >' + data.detail + '</p> \
            <span class="badge price"  style="height:5%;width:16%; font-size:18px;">' + data.price + '<span contentEditable="false">$</span> </span> ';
    return html;
}


function append_user(data, is_bought) {
    is_bought = typeof is_bought !== 'undefined' ? is_bought : 0;
    var html_string = product_html_li(data);
    if (is_bought) {
        html_string += '<button class="btn  btn-default buy_class" style="margin-left:10%; margin-top:-5%;width:16%; ">Buy</button>';
    }
    else {
        html_string += '<button class="btn  btn-primary buy_class" style="margin-left:10%; margin-top:-5%;width:16%; ">Buy</button>'
    }
    if (staff) {
        html_string += product_html_for_staff();
    }
    html_string += "</div> </li>"
    $("#main").append(html_string);
    $(".buy_class").unbind('click');
    $(".buy_class").click(buy_me);
    if (staff) {
        $(".delete_class").unbind('click');
        $(".edit_class").unbind('click');
        $(".show_image_popup").unbind('click');
        $(".delete_class").click(deleter);
        $(".edit_class").click(editor);
        $(".show_image_popup").click(toggle_product_popup);

    }
}

function deleter() {
    var id = $(this).parentsUntil("li").parent().attr("id");
    $.ajax({
        type: "GET",
        headers: {"Authorization": "Token " + localStorage.getItem('Token')},
        url: base_path + 'app/delete_product/' + id + '/',
        dataType: "json",
        success: function (data, status) {
            if (status == "nocontent") {
                $("#" + id).remove();
            }
        },
        error: show_alerts
    });
}
function editor() {
    product = $('#' + $(this).parentsUntil("li").parent().attr("id"))
    product.find(".name").attr("contentEditable", true);
    product.find(".price").attr("contentEditable", true);
    product.find(".detail").attr("contentEditable", true);
    $(this).text("Save");
    $(this).unbind('click');
    $(this).click(update);
}

function update() {
    var id = $(this).parentsUntil("li").parent().attr("id");
    var name = $('#' + id).find(".name").text();
    var detail = $('#' + id).find(".detail").text();
    var price = parseInt($('#' + id).find(".price").contents().get(0).nodeValue);
    if (name && detail && price) {
        $.ajax({
            type: 'POST',
            url: base_path + 'app/edit_product/' + id + '/',
            dataType: 'json',
            headers: {"Authorization": "Token " + localStorage.getItem('Token')},
            data: {"id": id, "name": name, "detail": detail, "price": price},
            success: function (data, status) {
                product = $('#' + id);
                product.find(".name").attr("contentEditable", false);
                product.find(".price").attr("contentEditable", false);
                product.find(".detail").attr("contentEditable", false);
                $('#' + id).find(".edit_class").text("Edit");
                $('#' + id).find(".edit_class").unbind('click');
                $('#' + id).find(".edit_class").click(editor);

            },
            error: show_alerts
        });


    }
    else {
        show_alerts({"Error": "please Enter all the fields"});
    }

}
function buy_me() {

    var id = $(this).parentsUntil("li").parent().attr("id");
    $.ajax({
        type: 'POST',
        url: base_path + 'app/my_products/',
        dataType: 'json',
        headers: {"Authorization": "Token " + localStorage.getItem('Token')},
        data: {"product": id, "user": $("#user").val()},
        success: function (data, status) {
            show_alerts(data);

        },
        error: show_alerts
    });

}
function fill() {

    $.ajax({
        type: 'GET',
        url: base_path + 'app/products/',
        headers: {"Authorization": "Token " + localStorage.getItem('Token')},

        success: function (data, status) {
            staff = data.staff;

            for (product in data.products) {
                append_user(data.products[product]);
            }
            for (product in data.bought) {
                append_user(data.bought[product], 1);
            }
        },
        error: error_response

    });


}
function upload_product_image(event) {
    event.preventDefault();
    form_data = new FormData($("#image_form").get(0));

    $.ajax({
        type: 'POST',
        url: base_path + 'app/change_product_image/',
        data: form_data,
        cache: false,
        headers: {"Authorization": "Token " + localStorage.getItem('Token')},
        processData: false, // Don't process the files
        contentType: false,
        success: function (data) {
            $("#" + data.id).find("img").attr("src", data.image);
            $("#product_image_popup").hide();
        },
        error: show_alerts
    });
}

$(document).ready(function () {

    $("#create").click(create);
    $("#close_popup").click(toggle_product_popup);
    $("#upload_image").click(upload_product_image);

    $("#local_image").change(function () {
        readURL(this, "#page_display");

    });
    fill();


});