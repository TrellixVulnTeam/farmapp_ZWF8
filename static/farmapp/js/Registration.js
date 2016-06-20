
function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

var csrftoken = getCookie('csrftoken');

function SaveUserDetails(){
    var Data={first_name:$("#inputUsername").val(),
            last_name:$("#inputUsername").val(),username:$("#inputUsername").val()
        ,password:$("#password").val(),email:$("#email").val()};
    $.ajax({
            url: "/api/accounts/",
            type: "POST",
            data: Data,
            dataType: "json",
            headers: { "X-CSRFToken": csrftoken},
            success:function(data, textStatus, jqXHR)
            {
                alert("Sucessfully created user details.");
            },
            error: function (jqXHR, textStatus, errorThrown) {
                alert('Error occurred while  saving user details.\n Please Contact Appssupport.' );
            }
    });
// $.post('/api/accounts/', data).done(function(data){
//     console.log(data);
// });
}


/**
 * Created by kanuru.sagar on 02/29/16.
 */
