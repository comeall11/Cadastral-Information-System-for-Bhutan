
var map = L.map('map').setView([27.5, 90.4], 8);

var osm = L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
  maxZoom: 19,
  attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
});

var satImg = L.tileLayer('http://{s}.google.com/vt/lyrs=s&x={x}&y={y}&z={z}', { maxZoom: 20, subdomains: ['mt0', 'mt1', 'mt2', 'mt3'] }).addTo(map);

var Stamen_Terrain = L.tileLayer('http://stamen-tiles-{s}.a.ssl.fastly.net/terrain/{z}/{x}/{y}.{ext}', {
  attribution: 'Map tiles by <a href="http://stamen.com">Stamen Design</a>, <a href="http://creativecommons.org/licenses/by/3.0">CC BY 3.0</a> &mdash; Map data &copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>',
  subdomains: 'abcd',
  minZoom: 0,
  maxZoom: 18,
  ext: 'png'
});

var sub_district = L.geoJSON(sub_dist, {
  onEachFeature: function (feature, layer) {
    var label = L.marker(layer.getBounds().getCenter(), {
      icon: L.divIcon({
        className: 'label',
        html: feature.properties.admin2Name,
      })
    });
    // add the label to the map
    label.addTo(map);
  },
  style: {
    color: 'black',
  }
}).addTo(map);

var district = L.geoJSON(districtJSON, {
  onEachFeature: function (feature, layer) {
    var label = L.marker(layer.getBounds().getCenter(), {
      icon: L.divIcon({
        className: 'label',
        html: feature.properties.admin1Name,
      })
    });
    // add the label to the map
    label.addTo(map);
  },
  style: {
    fillOpacity: 0,
    color: 'brown',
  }
}).addTo(map);


var country = L.geoJSON(countryJSON, {
  onEachFeature: function (feature, layer) {
    var label = L.marker(layer.getBounds().getCenter(), {
      icon: L.divIcon({
        className: 'label',
        html: feature.properties.admin0Name,
        fontSize: 20,

      })
    });
    // add the label to the map
    label.addTo(map);
  },
  style: {
    fillOpacity: 0,
    color: 'red',
    outerWidth: 0.2
  }
}).addTo(map);



baseLayer = {
  "Open Street Map": osm,
  "Satellite Imagery": satImg,
  "Stamen Terrain": Stamen_Terrain
}

adminLayer = {
  "Country": country,
  "District": district,
  "Sub-district": sub_district
}
L.control.layers(baseLayer).addTo(map);
L.control.layers(adminLayer).addTo(map);

/* var footprint = JSON.parse('{{geometry | tojson}}');
var parcel = L.geoJSON(footprint); */
/* var footprint = JSON.parse('{{geometry | tojson}}');
var parcel = L.geoJSON(footprint).addTo(map);
map.fitBounds(parcel.getBounds()).addTo(map); */

// Make an AJAX request to get the GeoJSON data
/* function requestData() {
  $.ajax({
    url: "/plot-thram",
    type: 'GET',
    cache: false,
    success: function (html) {
      var data = html; */
/* var layer = L.geoJSON(data, {
  onEachFeature: function (feature, layer) {
  },
  style: {
    fillOpacity: 1,
    color: 'blue',
    outerWidth: 5
  },
  onEachFeature: function (feature, layer) {
    // add a popup for each feature
    layer.bindPopup(feature.properties.popupContent);
  }
}).addTo(map); */


/* var parcel = '{{ data|tojson|safe }}';
L.geoJSON(parcel).addTo(map);
map.fitBounds(parcel.getBounds()); */
/* {% set parcel = data %}
{% set geojson = parcel|json %}

var plots = L.geoJSON(data, {
  onEachFeature: function (feature, layer) {
    if (feature.geometry.type == 'MultiPolygon') {
      var polygons = feature.geometry.coordinates;
      for (var i = 0; i < polygons.length; i++) {
        var polygon = polygons[i];
        var latlngs = [];
        for (var j = 0; j < polygon.length; j++) {
          var ring = polygon[j];
          var coords = [];
          for (var k = 0; k < ring.length; k++) {
            var coord = ring[k];
            coords.push([coord[1], coord[0]]);
          }
          latlngs.push(coords);
        }
        L.polygon(latlngs).addTo(map);
      }
    } else {
      // handle other geometry types
    }
  }
}).addTo(map); */
/* 
var latlngs = L.geoJSON.coordsToLatLngs(data);
var multiPolygon = L.multiPolygon(latlngs);
multiPolygon.addTo(map);
map.fitBounds(multiPolygon.getBounds());  */



