import pymongo
import folium
from geopy.geocoders import Nominatim

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

    mapObj = folium.Map(location=[20.0, 84.0], zoom_start=7)
    shapesLayer = folium.FeatureGroup(name="circles").add_to(mapObj)

    alldoc = collection.find({"City": "Berhampur"}, {'Name': 1, 'Location': 1, 'Image_URL': 1, '_id': 0})
    
    for item in alldoc:
        address = item['Location']
        coordinates = get_coordinates(address)

        if coordinates:
            lat, lon = coordinates
            image_url = item.get('Image_URL', "https://example.com/default_image.jpg")

            popup_content = f"""<h2>{item['Name']}</h2><br/>
                                <b>{address}</b><br/>
                                <img src="{image_url}" alt="Image" style="max-width:100%;max-height:100%">"""

            folium.Marker(
                location=[lat, lon],
                popup=folium.Popup(popup_content, max_width=500),
                icon=folium.Icon(color='green')
            ).add_to(shapesLayer)

    folium.LayerControl().add_to(mapObj)
    mapObj.save('output.html')

if __name__ == "__main__":
    update_map()
