//Declaring map 
var mapplot = L.map('mapplot').setView([27.5, 90.4], 8);

//Basemap Layers

var osm = L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
  maxZoom: 20,
  attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
});

var satImg = L.tileLayer('http://{s}.google.com/vt/lyrs=s&x={x}&y={y}&z={z}', { maxZoom: 20, subdomains: ['mt0', 'mt1', 'mt2', 'mt3'] }).addTo(mapplot);

var Stamen_Terrain = L.tileLayer('http://stamen-tiles-{s}.a.ssl.fastly.net/terrain/{z}/{x}/{y}.{ext}', {
  attribution: 'Map tiles by <a href="http://stamen.com">Stamen Design</a>, <a href="http://creativecommons.org/licenses/by/3.0">CC BY 3.0</a> &mdash; Map data &copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>',
  subdomains: 'abcd',
  minZoom: 0,
  maxZoom: 20,
  ext: 'png'
});

//Loadning Administrative Boundary from Geojson files
var sub_district = L.geoJSON(sub_dist, {
  style: {
    fillOpacity: 0,
    color: 'grey',
    weight: 0.3
  }
}).addTo(mapplot);
sub_district.eachLayer(function(layer) {
  var center = layer.getBounds().getCenter();
  var label = L.marker(center, {
      icon: L.divIcon({
          className: 'label1',
          html: layer.feature.properties.admin2Name
      })
  }).addTo(mapplot);
});

var district = L.geoJSON(districtJSON, {
  style: {
    fillOpacity: 0,
    color: 'brown',
    weight: 1
  }
}).addTo(mapplot);

district.eachLayer(function(layer) {
  var center = layer.getBounds().getCenter();
  var label = L.marker(center, {
      icon: L.divIcon({
          className: 'label2',
          html: layer.feature.properties.admin1Name
      })
  }).addTo(mapplot);
});

var country = L.geoJSON(countryJSON, {
  style: {
    fillOpacity: 0,
    color: 'red',
    weight: 2.5
  }
}).addTo(mapplot);

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
L.control.layers(baseLayer).addTo(mapplot);
L.control.layers(adminLayer).addTo(mapplot);
baseLayer.addOverlay(baseLayer, 'Base Maps');


var polygonLayer;
