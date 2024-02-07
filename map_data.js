
var map = L.map('map').setView([20.0, 84.0], 7);

L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    maxZoom: 19,
}).addTo(map);


L.marker([T, a]).addTo(map)
    .bindPopup('<b>TONY STARK</b><br>Tata Benz');

L.marker([M, K]).addTo(map)
    .bindPopup('<b>om prasad</b><br>MKCG Medical College');

