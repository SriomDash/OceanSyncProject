import pymongo
from geopy.geocoders import Nominatim
from datetime import datetime

geolocator = Nominatim(user_agent="my_geocoder")

def get_coordinates(address):
    location = geolocator.geocode(address)
    if location:
        return location.latitude, location.longitude
    else:
        return None

def update_map():
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    db = client['mydb']
    collection = db['collection1']

    html_output = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Google Maps</title>
        <script src="https://maps.googleapis.com/maps/api/js?key=AIzaSyDh0vh0wtcJJVTPlKwS38f64KZGydanqCs"></script>
    </head>
    <body>
        <div id="map" style="height: 400px; width: 150%;"></div>
        <script>
            function initMap() {
                var mapOptions = {
                    center: { lat: 20.0, lng: 84.0 },
                    zoom: 7
                };
                var map = new google.maps.Map(document.getElementById('map'), mapOptions);

                // Add markers dynamically
                // Replace this with your code to retrieve data from MongoDB and add markers
                // Example:
                var marker = new google.maps.Marker({
                    position: { lat: 20.0, lng: 84.0 },
                    map: map,
                    title: 'Marker'
                });
            }
            initMap();
        </script>
    </body>
    </html>
    """

    with open('output.html', 'w') as f:
        f.write(html_output)

if __name__ == "__main__":
    update_map()
