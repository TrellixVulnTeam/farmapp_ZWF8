

/**
 * Created by kanuru.sagar on 03/26/16.
 */



// This example requires the Places library. Include the libraries=places
// parameter when you first load the API. For example:
// <script src="https://maps.googleapis.com/maps/api/js?key=YOUR_API_KEY&libraries=places">
var infowindow = null, marker = null, markers = [];
/* $(document).ready(function () {
   initMap();
});*/
function placeMarker(location, map) {
    marker = new google.maps.Marker({
        position: location,
        map: map,
    });
    markers.push(marker);
    var lDetails = "", latitude = location.lat(), langitude = location.lng();
    for (var ifarm in tempData) {
        if (ifarm > 0)
            continue;
        var cropData = tempData[ifarm];
        if (parseInt(cropData.land_details.latitude) == parseInt(latitude) && parseInt(cropData.land_details.longitude) == parseInt(langitude))
            lDetails = lDetails + "<br>CROP : " + cropData.crop + "<br>CROP_TYPE : " + cropData.crop_type + "<br>expected_end_date : " + cropData.expected_end_date
                + "<br>land_details: <br> Lat:" + cropData.land_details.latitude + "<br> Lang:" + cropData.land_details.longitude + "<input type='button' value='More' onclick='GetMoreDetails(" + ifarm + ")'>"
        ;
    }

    if (lDetails == "") {
        lDetails = "<br>No Data Avaliable";
        /*  var newLocFound = tempData[0];
          newLocFound.land_details.latitude = latitude;
          newLocFound.land_details.longitude = langitude;
          tempData.push(newLocFound);*/
    }
    infowindow = new google.maps.InfoWindow({
        content: lDetails
    });
    infowindow.open(map, marker);
}
var tempData = {};

function initMap() {
    GetMetaData();
   var map = new google.maps.Map(document.getElementById('map'), {
          zoom: 12,
          center: {lat: 17.705245, lng: 78.22386}});
    var input = /** @type {!HTMLInputElement} */(
        document.getElementById('pac-input'));


    //var types = document.getElementById('type-selector');
    map.controls[google.maps.ControlPosition.TOP_LEFT].push(input);
    //map.controls[google.maps.ControlPosition.TOP_LEFT].push(types);
    infoWindow = new google.maps.InfoWindow({ map: map });


    function handleLocationError(browserHasGeolocation, infoWindow, pos) {
        infoWindow.setPosition(pos);
        infoWindow.setContent(browserHasGeolocation ?
                              'Error: The Geolocation service failed.' :
                              'Error: Your browser doesn\'t support geolocation.');
    }
    google.maps.event.addListener(map, 'click', function (event) {
        $("#map").width(self.innerWidth);
        if (infowindow) {
            //infowindow.close();
            setMapOnAll(null);
        }

        placeMarker(event.latLng, map);
    });

    var autocomplete = new google.maps.places.Autocomplete(input);
    autocomplete.bindTo('bounds', map);

    /* var infowindow = new google.maps.InfoWindow();
     var marker = new google.maps.Marker({
       map: map,
       anchorPoint: new google.maps.Point(0, -29)
     }); */

    autocomplete.addListener('place_changed', function () {

        if (infowindow)
            //infowindow.close();
            if (marker == null)
                marker = new google.maps.Marker({
                    position: location,
                    map: map,
                });

        marker.setVisible(false);
        var place = autocomplete.getPlace();
        if (!place.geometry) {
            window.alert("Autocomplete's returned place contains no geometry");
            return;
        }

        // If the place has a geometry, then present it on a map.
        if (place.geometry.viewport) {
            map.fitBounds(place.geometry.viewport);
        } else {
            map.setCenter(place.geometry.location);
            map.setZoom(17);  // Why 17? Because it looks good.
        }
        marker.setIcon(/** @type {google.maps.Icon} */({
            url: place.icon,
            size: new google.maps.Size(71, 71),
            origin: new google.maps.Point(0, 0),
            anchor: new google.maps.Point(17, 34),
            scaledSize: new google.maps.Size(35, 35)
        }));
        marker.setPosition(place.geometry.location);
        marker.setVisible(true);

        var address = '';
        if (place.address_components) {
            address = [
              (place.address_components[0] && place.address_components[0].short_name || ''),
              (place.address_components[1] && place.address_components[1].short_name || ''),
              (place.address_components[2] && place.address_components[2].short_name || '')
            ].join(' ');
        }

        infowindow.setContent('<div><strong>' + place.name + '</strong><br>' + address);
        infowindow.open(map, marker);
    });

    // Sets a listener on a radio button to change the filter type on Places
    // Autocomplete.
    function setupClickListener(id, types) {
        var radioButton = document.getElementById(id);
        radioButton.addEventListener('click', function () {
            autocomplete.setTypes(types);
        });
    }

    setupClickListener('changetype-all', []);
    setupClickListener('changetype-address', ['address']);
    setupClickListener('changetype-establishment', ['establishment']);
    setupClickListener('changetype-geocode', ['geocode']);

    var markerA = new google.maps.Marker({
        map: map,
        position: new google.maps.LatLng(0, 0),
        customInfo: "Marker A"
    });
    google.maps.event.addListener(markerA, 'click', function () {
        alert(this.customInfo);
    });
};


function setMapOnAll(map) {
    for (var i = 0; i < markers.length; i++) {
        markers[i].setMap(map);
    }
}



function GetMoreDetails(ifarm) {

    //$("#divCropDetails").remove();
    var cropData = tempData[ifarm];
    //$("#map").width(self.innerWidth - self.innerWidth / 3);
    //$("#map").css("position", "absolute");
    // var cropDetails = "<div id='divCropDetails' style='padding-left: 10px; padding-right: 3px;float:right; overflow: auto;'></div>";
    var details = "<table cellspacing=0 id='tblData'>";
    details = details + "<tr><td colspan=2><b> Farmer Details:</b></td></tr>";
    for (var iFarmerDetails in cropData.farmer_details) {
        details = details + "<tr><td><b style='float:right'>" + iFarmerDetails + ":</b></td><td> " + cropData.farmer_details[iFarmerDetails] + "</td></tr>";
    }
    details = details + "<tr><td colspan=2><b> Crop Details:</b></td></tr>" + "<tr><td><b style='float:right'>start_date:</b></td><td> " + cropData.start_date + "</td></tr>";
    details = details + "<tr><td><b style='float:right'>Expected End Date:</b></td><td> " + cropData.expected_end_date + "</td></tr>";
    for (var iLanDetail in cropData.land_details) {
        details = details + "<tr><td ><b style='float:right'>" + iLanDetail + ":</b></td><td> " + cropData.land_details[iLanDetail] + "</td></tr>";
    }
    details = details + "<tr><td><b style='float:right'>farmer type:</b></td><td> " + cropData.farming_type + "</td></tr>";
    details = details + "<tr><td colspan=2 style='text-align:centre'><input type='button' style='background-color:gray' value='Invest' onclick='Payment_Click()'></td></tr></table>";

   // $("#divCropDetails").append(details);
    $(parent.document.getElementById("tblData")).remove();
   $(parent.document.getElementById("divAllDetails")).append(details);
     $(parent.document.getElementById("divFarmerDetails")).css("visibility","visible");

}

function Payment_Click() {
    alert("Need To implement payment details");
}


$(document).ready(function () {
    $(".logout-profile").click(function () {
        $(".logout-popup").css("visibility", "visible");
        $(".logout-transaction-div").css("display", "none");
        $(".logout-profile-div").css("display", "block");
    });
    $(".profile-closeimg").click(function () {
        $(".logout-popup").css("visibility", "hidden");
    });
    $(".logout-transaction").click(function () {
        $(".logout-popup").css("visibility", "visible");
        $(".logout-transaction-div").css("display", "block");
        $(".logout-profile-div").css("display", "none");
    });
    $(".transaction-closeimg").click(function () {
        $(".logout-popup").css("visibility", "hidden");
    });
    $(".map-clickhere").click(function () {
        $(".logout-right").css("visibility", "visible");
    });
    $(".right-closeimg").click(function () {
        $(".logout-right").css("visibility", "hidden");
    });
});
