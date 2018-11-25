
center = [-71.057083, 42.361145]
init_zoom = 11

map = createMap(center, init_zoom)

map.on("load", function() {
    
map.addSource("race_demographics", {
    type: "geojson",
    data: "/static/geojson/race_demographics.geojson"
});


    
map.addLayer({
    id:      "Asian",
    type:         "fill",
    source: "race_demographics",
    layout:         {},
    paint: {
        "fill-color": 
[
    "interpolate",
    ["linear"],
    ["to-number", ["get", "Asian"]],
    0.0, "#0d0887",
2614.0, "#cc4778"
]
    ,
        "fill-opacity": 0.85
    }
}, 'waterway-label');


map.on("click", "Asian", function(e) {
    new mapboxgl.Popup()
        .setLngLat(e.lngLat)
        .setHTML("<b>Asian:</b> " + e.features[0].properties["Asian"])
        .addTo(map);
});



map.addLayer({
    id:      "Black",
    type:         "fill",
    source: "race_demographics",
    layout:         {},
    paint: {
        "fill-color": 
[
    "interpolate",
    ["linear"],
    ["to-number", ["get", "Black"]],
    2.0, "#0d0887",
4227.0, "#cc4778"
]
    ,
        "fill-opacity": 0.85
    }
}, 'waterway-label');


map.on("click", "Black", function(e) {
    new mapboxgl.Popup()
        .setLngLat(e.lngLat)
        .setHTML("<b>Black:</b> " + e.features[0].properties["Black"])
        .addTo(map);
});



map.addLayer({
    id:      "White",
    type:         "fill",
    source: "race_demographics",
    layout:         {},
    paint: {
        "fill-color": 
[
    "interpolate",
    ["linear"],
    ["to-number", ["get", "White"]],
    3.0, "#0d0887",
4665.0, "#cc4778"
]
    ,
        "fill-opacity": 0.85
    }
}, 'waterway-label');


map.on("click", "White", function(e) {
    new mapboxgl.Popup()
        .setLngLat(e.lngLat)
        .setHTML("<b>White:</b> " + e.features[0].properties["White"])
        .addTo(map);
});



map.addLayer({
    id:      "Hispanic",
    type:         "fill",
    source: "race_demographics",
    layout:         {},
    paint: {
        "fill-color": 
[
    "interpolate",
    ["linear"],
    ["to-number", ["get", "Hispanic"]],
    0.0, "#0d0887",
2426.0, "#cc4778"
]
    ,
        "fill-opacity": 0.85
    }
}, 'waterway-label');


map.on("click", "Hispanic", function(e) {
    new mapboxgl.Popup()
        .setLngLat(e.lngLat)
        .setHTML("<b>Hispanic:</b> " + e.features[0].properties["Hispanic"])
        .addTo(map);
});



map.addLayer({
    id:      "PercentAsian",
    type:         "fill",
    source: "race_demographics",
    layout:         {},
    paint: {
        "fill-color": 
[
    "interpolate",
    ["linear"],
    ["to-number", ["get", "Percent Asian"]],
    0.0, "#0d0887",
0.726067747, "#cc4778"
]
    ,
        "fill-opacity": 0.85
    }
}, 'waterway-label');


map.on("click", "PercentAsian", function(e) {
    new mapboxgl.Popup()
        .setLngLat(e.lngLat)
        .setHTML("<b>Percent Asian:</b> " + e.features[0].properties["Percent Asian"])
        .addTo(map);
});



map.addLayer({
    id:      "PercentBlack",
    type:         "fill",
    source: "race_demographics",
    layout:         {},
    paint: {
        "fill-color": 
[
    "interpolate",
    ["linear"],
    ["to-number", ["get", "Percent Black"]],
    0.001168224, "#0d0887",
0.85298767, "#cc4778"
]
    ,
        "fill-opacity": 0.85
    }
}, 'waterway-label');


map.on("click", "PercentBlack", function(e) {
    new mapboxgl.Popup()
        .setLngLat(e.lngLat)
        .setHTML("<b>Percent Black:</b> " + e.features[0].properties["Percent Black"])
        .addTo(map);
});



map.addLayer({
    id:      "PercentWhite",
    type:         "fill",
    source: "race_demographics",
    layout:         {},
    paint: {
        "fill-color": 
[
    "interpolate",
    ["linear"],
    ["to-number", ["get", "Percent White"]],
    0.009760426, "#0d0887",
0.982476636, "#cc4778"
]
    ,
        "fill-opacity": 0.85
    }
}, 'waterway-label');


map.on("click", "PercentWhite", function(e) {
    new mapboxgl.Popup()
        .setLngLat(e.lngLat)
        .setHTML("<b>Percent White:</b> " + e.features[0].properties["Percent White"])
        .addTo(map);
});



map.addLayer({
    id:      "PercentHispanic",
    type:         "fill",
    source: "race_demographics",
    layout:         {},
    paint: {
        "fill-color": 
[
    "interpolate",
    ["linear"],
    ["to-number", ["get", "Percent Hispanic"]],
    0.0, "#0d0887",
0.645220588, "#cc4778"
]
    ,
        "fill-opacity": 0.85
    }
}, 'waterway-label');


map.on("click", "PercentHispanic", function(e) {
    new mapboxgl.Popup()
        .setLngLat(e.lngLat)
        .setHTML("<b>Percent Hispanic:</b> " + e.features[0].properties["Percent Hispanic"])
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
