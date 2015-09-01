/**
 * Created by hafizmuhammadjawadkhan on 8/5/15.
 */

function create() {
    if ($("#name").val() && $("#detail").val() && $("#price").val()) {
        $.ajax({
            type: 'POST',
            url: 'http://localhost:8000/app/products/',
            dataType: 'json',
            data: {"Name": $("#name").val(), "Detail": $("#detail").val(), "Price": $("#price").val()},
            success: function (data, status) {

                $("#name").val("");
                $("#detail").val("");
                $("#price").val("");
                append_user(data);
            },
            error: function (error) {
                alert("Sorry,your request can not be completed ..  Try again!")
            }
        });


    }
    else {
        alert("Please enter all the fields");
    }

}


function product_html(data) {
    return ('<tr id=' + data.id + '>' +
    '<td><input class = "name" type="text" readonly value=' + data.Name + '></td> ' +
    '<td><input class="email" type="text" readonly value=' + data.Detail + '></td>' +
    '<td><input class="password" type="text" readonly value=' + data.Price + '></td>' +
    '<td><button class="delete_class"  >Delete</button></td>' +
    '<td><button class="edit_class" >Edit</button></td>' +
    '</tr>');
}
function append_user(data, append) {
    var html_string = product_html(data);
    append == undefined ? $("#main").append(html_string) : $("#main").html(html_string);
    $(".delete_class").click(deleter);
    $(".edit_class").click(editor);
}

function deleter() {
    var id = $(this).parentsUntil("tr").parent().attr("id");
    $.ajax({
        type: "GET",
        url: 'http://localhost:8000/app/delete_product/' + id,
        dataType: "json",
        success: function (data, status, xhr) {
            if (status == "nocontent") {
                $("#" + id).remove();
            }
        },
        error: function () {
            alert("Sorry the product can not be deleted");
        }
    });
}
function editor() {
    $('#' + $(this).parentsUntil("tr").parent().attr("id")).find("input").attr("readonly", false);
    $(this).text("Save");
    $(this).unbind('click');
    $(this).click(update);
}

function update() {
    var id = $(this).parentsUntil("tr").parent().attr("id");
    var name = $('#' + id).find(".name").val();
    var detail = $('#' + id).find(".detail").val();
    var price = $('#' + id).find(".price").val();
    if (name && detail && price) {
        $.ajax({
            type: 'POST',
            url: 'http://localhost:8000/app/edit_product/' + id + '/',
            dataType: 'json',
            data: {"id": id, "Name": name, "Detail": detail, "Price": price},
            success: function (data, status) {
                $('#' + id).find("input").attr("readonly", true);
                $('#' + id).find(".edit_class").text("Edit");
                $('#' + id).find(".edit_class").unbind('click');
                $('#' + id).find(".edit_class").click(editor);

            },
            error: function (error) {
                alert("Sorry,your request can not be completed ..  Try again!")
            }
        });


    }
    else {
        alert("Please enter all the fields");
    }

}
function buy_me() {
    var id = $(this).parentsUntil("tr").parent().attr("id");
    $.ajax({
        type: 'POST',
        url: 'http://localhost:8000/app/my_products/',
        dataType: 'json',
        data: {"product_id": id},
        success: function (data, status) {
            alert("you have successfully bought the item");

        },
        error: function (error) {
            alert("Sorry,your request can not be completed ..  Try again!")
        }
    });
}

$(document).ready(function () {

    $("#create").click(create);
    $(".delete_class").click(deleter);
    $(".edit_class").click(editor);
    $(".buy_class").click(buy_me);

});