/**
 * Created by kanuru.sagar on 06/25/16.
 */

function GetMetaData(){
     $.ajax({
            url: "http://urconnected.in/root/getmeta",
            type: "POST",
            data: Data,
            dataType: "json",
            headers: { "X-CSRFToken": csrftoken},
            success:function(data, textStatus, jqXHR)
            {
                tempData=data;
            },
            error: function (jqXHR, textStatus, errorThrown) {
                alert('Error occurred while Retriving map details.\n Please Contact Appssupport.' );
            }
    });
}
