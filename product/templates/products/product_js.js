/**
 * Created by hafizmuhammadjawadkhan on 8/5/15.
 */

function create() {
    if ($("#name").val() && $("#detail").val() && $("#price").val()) {
        $.ajax({
            type: 'POST',
            url: 'http://localhost:8000/app/products/',
            dataType: 'json',
            headers:{"Authorization": "Token "+ localStorage.getItem('Token')},
            data: {"Name": $("#name").val(), "Detail": $("#detail").val(), "Price": $("#price").val()},
            success: function (data, status) {

                $("#name").val("");
                $("#detail").val("");
                $("#price").val("");
                append_user(data);
            },
            error: function (error) {
                alert(error.responseText);
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
    '<td><input class="detail" type="text" readonly value=' + data.Detail + '></td>' +
    '<td><input class="price" type="text" readonly value=' + data.Price + '></td>' +
    '<td><button class="delete_class"  >Delete</button></td>' +
    '<td><button class="edit_class" >Edit</button></td>' +
    '<td><button class="buy_class" >Buy</button></td>' +
    '</tr>');
}
function append_user(data, append) {
    var html_string = product_html(data);
    append == undefined ? $("#main").append(html_string) : $("#main").html(html_string);
    $(".delete_class").unbind('click');
    $(".edit_class").unbind('click');
    $(".buy_class").unbind('click');
    $(".delete_class").click(deleter);
    $(".edit_class").click(editor);
    $(".buy_class").click(buy_me);
}

function deleter() {
    var id = $(this).parentsUntil("tr").parent().attr("id");
    $.ajax({
        type: "GET",
        headers:{"Authorization": "Token "+ localStorage.getItem('Token')},
        url: 'http://localhost:8000/app/delete_product/' + id+'/',
        dataType: "json",
        success: function (data, status) {
            if (status == "nocontent") {
                $("#" + id).remove();
            }
        },
        error: function () {
            alert(error.responseText);
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
            headers:{"Authorization": "Token "+ localStorage.getItem('Token')},
            data: {"id": id, "Name": name, "Detail": detail, "Price": price},
            success: function (data, status) {
                $('#' + id).find("input").attr("readonly", true);
                $('#' + id).find(".edit_class").text("Edit");
                $('#' + id).find(".edit_class").unbind('click');
                $('#' + id).find(".edit_class").click(editor);

            },
            error: function (error) {
                alert(error.responseText);
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
      headers:{"Authorization": "Token "+ localStorage.getItem('Token')},
      data: {"product": id, "user": $("#user").val()},
      success: function (data, status) {
          alert("you have successfully bought the item");

      },
      error: function (error) {
          alert(error.responseText);
      }
  });

}
function fill() {

    $.ajax({
        type: 'GET',
        url: 'http://localhost:8000/app/products/',
        headers:{"Authorization": "Token "+ localStorage.getItem('Token')},

        success: function (data, status) {
            for (product in data) {
                append_user(data[product]);

            }
        },
        error: function (error) {
            alert(error.responseText);
        }

    });


}

$(document).ready(function () {

    $("#create").click(create);
    fill();
    $(".delete_class").click(deleter);
    $(".edit_class").click(editor);
    $(".buy_class").click(buy_me);

});