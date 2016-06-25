/**
 * Created by kanuru.sagar on 06/25/16.
 */



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

function GetMetaData(){
     $.ajax({
            url: "http://urconnected.in/root/getmeta/?format=json",
            type: "GET",
            dataType: "json",
            headers: { "X-CSRFToken": csrftoken},
            success:function(data, textStatus, jqXHR)
            {
                tempData=data.result;

            },
            error: function (jqXHR, textStatus, errorThrown) {
                alert('Error occurred while Retriving map details.\n Please Contact Appssupport.' );
            }
    });
}
var g_UserDetails={};
function GetMetaData(){
     $.ajax({
            url: "http://urconnected.in/root/getmeta/?format=json",
            type: "GET",
            dataType: "json",
            headers: { "X-CSRFToken": csrftoken},
            success:function(data, textStatus, jqXHR)
            {
                g_UserDetails=data.result;

            },
            error: function (jqXHR, textStatus, errorThrown) {
                alert('Error occurred while Retriving map details.\n Please Contact Appssupport.' );
            }
    });
}