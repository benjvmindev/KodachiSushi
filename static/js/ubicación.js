function mostrarMapa() {
    const ubicacion = { lat: -36.741182, lng: -72.991532 }; // -36.741182, -72.991532

    const mapa = new google.maps.Map(document.getElementById("mapa"), {
        zoom: 12,
        center: ubicacion,
    });

    new google.maps.Marker({
        position: ubicacion,
        map: mapa,
        title: "Ubicación inicial"
    });
}