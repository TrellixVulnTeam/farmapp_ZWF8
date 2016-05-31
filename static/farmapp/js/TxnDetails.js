/**
 * Created by kanuru.sagar on 05/31/16.
 */

function GetTxnDetails(){
    $.ajax({
         type: "GET",
        async: "false",
        url: "http://" + farmAppUrl + "/composite/get_scenarios?companyid=" + companyId + "&callback=?",
        data: {},
        contentType: "application/json; charset=utf-8",
        dataType: "jsonp",
        jsonp: 'callback',
            success: function (jsonObj) {
                FillTxnDetais(getMain(jsonObj));
            },
            error: function (data, textStatus) {
                alert("Failed to load  Currency.");
            }
        });

}
/**
 * To do check whether returned jsonobj having d property ,if it's then we will remove it from json object
 * @param dObj
 * @returns {*}
 */

function getMain(dObj) {
    if (dObj.hasOwnProperty('d'))
        return dObj.d;
    else
        return dObj;
}


function FillTxnDetais(objOfTxnDetails){
    var seedDomEle=$("#divSeedTxnDetails").find("ul"),fruitDomEle=$("#divFruitTxnDetails").find("ul");
    for(var iTxnType in objOfTxnDetails){
if(iTxnType.toLowerCase().indexOf("seed")!=-1)
   FillTxnDetailsIntoPage(objOfTxnDetails[iTxnType],seedDomEle);
    else
   FillTxnDetailsIntoPage(objOfTxnDetails[iTxnType],fruitDomEle);

    }
    if(seedDomEle.find("li").length>0)
    $("#divSeedTxnDetails").show();
    if(fruitDomEle.find("li").length>0)
    $("#divFruitTxnDetails").show();
}

function FillTxnDetailsIntoPage(txnTypeData,seedDomEle){
    for(var iTxnDetail in txnTypeData){
        var txnData=txnTypeData[iTxnDetail];
        var domEleCreation="<li id="+txnData.id+">" +txnData.name
            "txnDate :" +txnData.txnDt+"txnTime:"+txnData.time+"</li>";
        seedDomEle.append(domEleCreation);
    }
}