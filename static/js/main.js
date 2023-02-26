
var map = L.map('map').setView([27.5, 90.4], 8);

var osm = L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
  maxZoom: 20,
  attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
});

var satImg = L.tileLayer('http://{s}.google.com/vt/lyrs=s&x={x}&y={y}&z={z}', { maxZoom: 20, subdomains: ['mt0', 'mt1', 'mt2', 'mt3'] }).addTo(map);

var Stamen_Terrain = L.tileLayer('http://stamen-tiles-{s}.a.ssl.fastly.net/terrain/{z}/{x}/{y}.{ext}', {
  attribution: 'Map tiles by <a href="http://stamen.com">Stamen Design</a>, <a href="http://creativecommons.org/licenses/by/3.0">CC BY 3.0</a> &mdash; Map data &copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>',
  subdomains: 'abcd',
  minZoom: 0,
  maxZoom: 20,
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

var polygonLayer;
