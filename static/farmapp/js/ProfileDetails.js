/**
 * Created by kanuru.sagar on 06/01/16.
 */

function FillProfileDetails(){
 $.ajax({
         type: "GET",
        async: "false",
        url: "http://" + farmAppUrl + "/composite/get_scenarios?companyid=" + companyId + "&callback=?",
        data: {},
        contentType: "application/json; charset=utf-8",
        dataType: "jsonp",
        jsonp: 'callback',
            success: function (jsonObj) {
                FillProfileDetailsDomEle(getMain(jsonObj));
            },
            error: function (data, textStatus) {
                alert("Failed to load  Currency.");
            }
        });
}

function FillProfileDetailsDomEle(profileData){

    var trEleToAdd="";
}
