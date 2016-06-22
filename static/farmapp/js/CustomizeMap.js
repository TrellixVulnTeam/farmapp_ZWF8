

/**
 * Created by kanuru.sagar on 03/26/16.
 */



// This example requires the Places library. Include the libraries=places
// parameter when you first load the API. For example:
// <script src="https://maps.googleapis.com/maps/api/js?key=YOUR_API_KEY&libraries=places">
var infowindow = null, marker = null,markers=[];
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
    for (var ifarm in tempData.farms) {
        if (ifarm > 0)
            continue;
        var cropData = tempData.farms[ifarm];
        if (cropData.land_details.latitude == latitude && cropData.land_details.longitude == langitude)
            lDetails = lDetails + "<br>CROP : " + cropData.crop + "<br>CROP_TYPE : " + cropData.crop_type + "<br>expected_end_date : " + cropData.expected_end_date
                + "<br>land_details: <br> Lat:" + cropData.land_details.latitude + "<br> Lang:" + cropData.land_details.longitude+"<input type='button' value='More' onclick='GetMoreDetails("+ifarm+")'>"
        ;
    }

    if(lDetails=="") {
        lDetails = "<br>No Data Avaliable";
        var newLocFound = tempData.farms[0];
        newLocFound.land_details.latitude = latitude;
        newLocFound.land_details.longitude = langitude;
        tempData.farms.push(newLocFound);
    }
     infowindow = new google.maps.InfoWindow({
        content: lDetails
    });
    infowindow.open(map, marker);
}
var tempData = { "farms": [{ "no_of_units_left_for_fund": 10, "farming_type": "organic", "start_date": "2-6-2016", "farming_id": 1, "crop": "rice", "land_details": { "area_unit": "hector", "details": "Good yield, organic farm", "longitude": 27.00007, "village": "ramapuram", "total_area": "2", "district": "Nizamabad", "latitude": 22.0006, "mandal": "thari", "address": "near post office", "state": "Telangana" }, "crop_type": "Sonamasuri", "estimated_weight_per_unit": "20kg", "farmer_details": { "full_name": "Bugga Narsaiah", "address": "1-6-09/a,near post office", "history": "good farmer had been working hard to make living", "name": "Narsaiah", "mobile": "234988734" }, "officer_incharge": { "email": "sureshramesh@gmail.com", "full_name": "suresh ramesh", "name": "suresh", "mobile": "89274923", "qualification": "B.Sc Agriculture, 5 years of exp in farming " }, "expected_end_date": "2-8-2016" }, { "no_of_units_left_for_fund": 20, "farming_type": "organic", "start_date": "2-6-2016", "farming_id": 2, "crop": "rice", "land_details": { "area_unit": "hector", "details": "Good yield, organic farm", "longitude": 26.00007, "village": "ramapuram", "total_area": "2", "district": "Nizamabad", "latitude": 23.0006, "mandal": "thari", "address": "near post office", "state": "Telangana" }, "crop_type": "Sonamasuri", "estimated_weight_per_unit": "20kg", "farmer_details": { "full_name": "Bugga Roshiah", "address": "1-6-09/a,near post office", "history": "good farmer had been working hard to make living", "name": "Roshiah", "mobile": "234988734" }, "officer_incharge": { "email": "sureshramesh@gmail.com", "full_name": "suresh ramesh", "name": "suresh", "mobile": "89274923", "qualification": "B.Sc Agriculture, 5 years of exp in farming " }, "expected_end_date": "22-8-2016" }] };

function initMap() {
    var map = new google.maps.Map(document.getElementById('map'), {
        center: { lat: -33.8688, lng: 151.2195 },
        zoom: 13,
        mapTypeId: google.maps.MapTypeId.ROADMAP
    });
    var input = /** @type {!HTMLInputElement} */(
        document.getElementById('pac-input'));

    var types = document.getElementById('type-selector');
    map.controls[google.maps.ControlPosition.TOP_LEFT].push(input);
    map.controls[google.maps.ControlPosition.TOP_LEFT].push(types);
    infoWindow = new google.maps.InfoWindow({ map: map });
 if (navigator.geolocation) {
     navigator.geolocation.getCurrentPosition(function (position) {
         initialLocation = new google.maps.LatLng(position.coords.latitude, position.coords.longitude);
         map.setCenter(initialLocation);
     });
 } else {
    // Browser doesn't support Geolocation
    handleLocationError(false, infoWindow, map.getCenter());
  }


function handleLocationError(browserHasGeolocation, infoWindow, pos) {
  infoWindow.setPosition(pos);
  infoWindow.setContent(browserHasGeolocation ?
                        'Error: The Geolocation service failed.' :
                        'Error: Your browser doesn\'t support geolocation.');
}
    google.maps.event.addListener(map, 'click', function (event) {
        if (infowindow) {
            infowindow.close();
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
        infowindow.close();
        if(marker==null)
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
}

function setMapOnAll(map) {
    for (var i = 0; i < markers.length; i++) {
        markers[i].setMap(map);
    }
}



function GetMoreDetails(ifarm){
    $("#divCropDetails").remove();
var cropData = tempData.farms[ifarm];
    $("#map").width( self.innerWidth-self.innerWidth/3);
    $("#map").css("position","absolute");
    var cropDetails="<div id='divCropDetails' style='padding-left: 10px; padding-right: 3px;float:right; overflow: auto;'></div>";
    var details="<table cellspacing=0>";
     details=details+"<tr><td colspan=2><b> Farmer Details:</b></td></tr>";
    for(var iFarmerDetails in cropData.farmer_details){
         details=details+"<tr><td><b style='float:right'>"+iFarmerDetails+":</b></td><td> "+cropData.farmer_details[iFarmerDetails]+"</td></tr>";
    }
    details=details+"<tr><td colspan=2><b> Crop Details:</b></td></tr>"+"<tr><td><b style='float:right'>start_date:</b></td><td> "+cropData.start_date+"</td></tr>";
    details=details+"<tr><td><b style='float:right'>Expected End Date:</b></td><td> "+cropData.expected_end_date+"</td></tr>";
    for(var iLanDetail in cropData.land_details){
         details=details+"<tr><td ><b style='float:right'>"+iLanDetail+":</b></td><td> "+cropData.land_details[iLanDetail]+"</td></tr>";
    }
    details=details+"<tr><td><b style='float:right'>farmer type:</b></td><td> "+cropData.farming_type+"</td></tr></table>";
   details=details+"<tr><td colspan=2 style='text-align:centre'><input type='button'   value='Invest' onclick='Payment_Click()'></td></tr></table>";
    if($("#divMapFarmerData").find("map").length==0)
        $("#map").appendTo("#divMapFarmerData");
    $("#map").after(cropDetails);
    $("#divCropDetails").append(details);
}

function Payment_Click(){
alert("Need To implement payment details");
}