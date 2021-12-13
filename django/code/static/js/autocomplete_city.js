
$(document).ready(function () {
  google.maps.event.addDomListener(window, 'load', initialize);
});

function initialize() {
   var input = document.getElementById('locality');
   var autocomplete = new google.maps.places.Autocomplete(input);
}

