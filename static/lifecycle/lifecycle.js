/**
 * Created by kanuru.sagar on 01-05-2017.
 */

var g_LifeCycleData={};
$(document).ready(function(){
GetLifeCycleData();
});

function GetLifeCycleData(){
     $.ajax({
            url: "http://urconnected.in/root/lifecycle/?format=json",
            type: "GET",
            dataType: "json",
            success:function(data, textStatus, jqXHR)
            {
                g_LifeCycleData=data;
                PrepareDomEleToDisplay();
            },
            error: function (jqXHR, textStatus, errorThrown) {
                alert('Error occurred while Retriving lifecycle details.\n Please Contact Appssupport.' );
            }
    });
}

function PrepareDomEleToDisplay(){
    var tbl=$("#tblLifeCycleData");
for(var i=0;i<g_LifeCycleData.length;i++)
$("#tblLifeCycleData").append("<tr><td><img src="+g_LifeCycleData[i].image+" alt='No Image Exist'</td></tr>");
}