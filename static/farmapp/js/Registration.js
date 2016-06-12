function SaveUserDetails(){
    var data=JSON.stringify({first_name:$("#inputUsername").val(),
            last_name:$("#inputUsername").val(),username:$("#inputUsername").val()
        ,password:$("#password").val(),email:$("#email").val()});
 $.ajax({
            url: "http://urconnected.in/api/accounts/",
            type: "POST",
            async: false,
            data:  {
            'content': data,
            'csrfmiddlewaretoken': '{{ csrf_token }}',
            },
            dataType: "json",
            contenttype: "application/json; charset=utf-8",
            success: function (jsonData) {
                alert("Sucessfully created user details.");
            },
            error: function (jqXHR, textStatus, errorThrown) {
                alert('Error occurred while  saving user details.\n Please Contact Appssupport.' + jqXHR.statusText);
            }
        });
// $.post('/api/accounts/', data).done(function(data){
//     console.log(data);
// });
}


/**
 * Created by kanuru.sagar on 02/29/16.
 */
