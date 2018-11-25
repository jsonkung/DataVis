var allLayers = []
mapboxgl.accessToken = "pk.eyJ1IjoibWF0dGZlbmciLCJhIjoiY2pvdW5vZ2hhMHNrdjNrczMwd3lvdGg5biJ9.c0qStkkLmJXpuFHtomb0_g";

function createMap(center, zoom) {
  var map = new mapboxgl.Map({
    container: 'map',
    style: 'mapbox://styles/mapbox/dark-v9',
    center: center,
    zoom: zoom
  });

  return map;
}

function focusLayer(layer) {
    for (var i = 0; i < allLayers.length; i++) {
        if (allLayers[i] !== layer)
          map.setLayoutProperty(allLayers[i], "visibility", "none")
        $("#" + allLayers[i]).removeClass("active");
    }

    map.setLayoutProperty(layer, 'visibility', 'visible');
    $("#" + layer).addClass("active");
}

function toggleOverlay(overlay) {
    if (map.getLayoutProperty(overlay, "visibility") === "visible") {
      map.setLayoutProperty(overlay, "visibility", "none");
      $("#" + overlay).removeClass("active");
    } else {
      map.setLayoutProperty(overlay, "visibility", "visible");
      $("#" + overlay).addClass("active");
    }
}

function changeDataset(dataset) {
  console.log("hi")
  window.location = dataset;
}