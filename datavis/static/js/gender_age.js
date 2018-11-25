
center = [-71.057083, 42.361145]
init_zoom = 11

map = createMap(center, init_zoom)

map.on("load", function() {
    
map.addSource("gender_age", {
    type: "geojson",
    data: "/static/geojson/gender_age.geojson"
});


    
map.addLayer({
    id:      "Seniors",
    type:         "fill",
    source: "gender_age",
    layout:         {},
    paint: {
        "fill-color": 
[
    "interpolate",
    ["linear"],
    ["to-number", ["get", "Seniors"]],
    0.0, "#0d0887",
1037.0, "#cc4778"
]
    ,
        "fill-opacity": 0.85
    }
}, 'waterway-label');


map.on("click", "Seniors", function(e) {
    new mapboxgl.Popup()
        .setLngLat(e.lngLat)
        .setHTML("<b>Seniors:</b> " + e.features[0].properties["Seniors"])
        .addTo(map);
});



map.addLayer({
    id:      "Males18-34",
    type:         "fill",
    source: "gender_age",
    layout:         {},
    paint: {
        "fill-color": 
[
    "interpolate",
    ["linear"],
    ["to-number", ["get", "Males 18-34"]],
    1.0, "#0d0887",
3172.0, "#cc4778"
]
    ,
        "fill-opacity": 0.85
    }
}, 'waterway-label');


map.on("click", "Males18-34", function(e) {
    new mapboxgl.Popup()
        .setLngLat(e.lngLat)
        .setHTML("<b>Males 18-34:</b> " + e.features[0].properties["Males 18-34"])
        .addTo(map);
});



map.addLayer({
    id:      "Females18-34",
    type:         "fill",
    source: "gender_age",
    layout:         {},
    paint: {
        "fill-color": 
[
    "interpolate",
    ["linear"],
    ["to-number", ["get", "Females 18-34"]],
    6.0, "#0d0887",
3426.0, "#cc4778"
]
    ,
        "fill-opacity": 0.85
    }
}, 'waterway-label');


map.on("click", "Females18-34", function(e) {
    new mapboxgl.Popup()
        .setLngLat(e.lngLat)
        .setHTML("<b>Females 18-34:</b> " + e.features[0].properties["Females 18-34"])
        .addTo(map);
});



map.addLayer({
    id:      "Children",
    type:         "fill",
    source: "gender_age",
    layout:         {},
    paint: {
        "fill-color": 
[
    "interpolate",
    ["linear"],
    ["to-number", ["get", "Children"]],
    0.0, "#0d0887",
1437.0, "#cc4778"
]
    ,
        "fill-opacity": 0.85
    }
}, 'waterway-label');


map.on("click", "Children", function(e) {
    new mapboxgl.Popup()
        .setLngLat(e.lngLat)
        .setHTML("<b>Children:</b> " + e.features[0].properties["Children"])
        .addTo(map);
});




map.addSource("bps", {
    type: "geojson",
    data: "/static/geojson/bps.geojson"
});



map.addLayer({
    id:      "CITY",
    type:       "circle",
    source: "bps",
    layout:         {},
    paint: {
        "circle-color": "#E85D75",
        "circle-radius": {
            "base":  1.5,
            "stops": [[6, 2], [12, 4], [18, 50], [22, 180]]
        },
        "circle-opacity": 0.97
    }
}, 'waterway-label');

var CITYpopup = new mapboxgl.Popup({
    closeButton: false,
    closeOnClick: false
});

map.on("mouseenter", "CITY", function(e) {
    CITYpopup
        .setLngLat(e.lngLat)
        .setHTML("<b>SCH_NAME:</b> " + e.features[0].properties["SCH_NAME"] + "<br>" +
                 "<b>CITY:</b> " + e.features[0].properties["CITY"])
        .addTo(map);
});

map.on("mouseleave", "CITY", function(e) {
    map.getCanvas().style.cursor = "";
    CITYpopup.remove();
});

map.setLayoutProperty("CITY", "visibility", "none");





map.addSource("bnps", {
    type: "geojson",
    data: "/static/geojson/bnps.geojson"
});



map.addLayer({
    id:      "TYPE",
    type:       "circle",
    source: "bnps",
    layout:         {},
    paint: {
        "circle-color": "#45CB85",
        "circle-radius": {
            "base":  1.5,
            "stops": [[6, 2], [12, 4], [18, 50], [22, 180]]
        },
        "circle-opacity": 0.97
    }
}, 'waterway-label');

var TYPEpopup = new mapboxgl.Popup({
    closeButton: false,
    closeOnClick: false
});

map.on("mouseenter", "TYPE", function(e) {
    TYPEpopup
        .setLngLat(e.lngLat)
        .setHTML("<b>NAME:</b> " + e.features[0].properties["NAME"] + "<br>" +
                 "<b>TYPE:</b> " + e.features[0].properties["TYPE"])
        .addTo(map);
});

map.on("mouseleave", "TYPE", function(e) {
    map.getCanvas().style.cursor = "";
    TYPEpopup.remove();
});

map.setLayoutProperty("TYPE", "visibility", "none");





map.addSource("colleges", {
    type: "geojson",
    data: "/static/geojson/colleges.geojson"
});



map.addLayer({
    id:      "Cost",
    type:       "circle",
    source: "colleges",
    layout:         {},
    paint: {
        "circle-color": "#A594F9",
        "circle-radius": {
            "base":  1.5,
            "stops": [[6, 2], [12, 4], [18, 50], [22, 180]]
        },
        "circle-opacity": 0.97
    }
}, 'waterway-label');

var Costpopup = new mapboxgl.Popup({
    closeButton: false,
    closeOnClick: false
});

map.on("mouseenter", "Cost", function(e) {
    Costpopup
        .setLngLat(e.lngLat)
        .setHTML("<b>Name:</b> " + e.features[0].properties["Name"] + "<br>" +
                 "<b>Cost:</b> " + e.features[0].properties["Cost"])
        .addTo(map);
});

map.on("mouseleave", "Cost", function(e) {
    map.getCanvas().style.cursor = "";
    Costpopup.remove();
});

map.setLayoutProperty("Cost", "visibility", "none");





map.addSource("wickedwifi", {
    type: "geojson",
    data: "/static/geojson/wickedwifi.geojson"
});



map.addLayer({
    id:      "AP_Name",
    type:       "circle",
    source: "wickedwifi",
    layout:         {},
    paint: {
        "circle-color": "#E4DFDA",
        "circle-radius": {
            "base":  1.5,
            "stops": [[6, 2], [12, 4], [18, 50], [22, 180]]
        },
        "circle-opacity": 0.97
    }
}, 'waterway-label');

var AP_Namepopup = new mapboxgl.Popup({
    closeButton: false,
    closeOnClick: false
});

map.on("mouseenter", "AP_Name", function(e) {
    AP_Namepopup
        .setLngLat(e.lngLat)
        .setHTML("<b>AP_Name:</b> " + e.features[0].properties["AP_Name"] + "<br>" +
                 "<b>AP_Name:</b> " + e.features[0].properties["AP_Name"])
        .addTo(map);
});

map.on("mouseleave", "AP_Name", function(e) {
    map.getCanvas().style.cursor = "";
    AP_Namepopup.remove();
});

map.setLayoutProperty("AP_Name", "visibility", "none");


})