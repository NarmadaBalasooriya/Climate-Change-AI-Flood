import os
import sys
import os
from options.test_options import TestOptions
from data import create_dataset
from models import create_model
from util.visualizer import save_images
from util import html


from googlegeocoder import GoogleGeocoder
import google_streetview.api

google_key = "AIzaSyBDc5jaJG0k0o1k1NHoinwU7E89AMujmso"

search = sys.argv[1:]
search_addr = ",".join(search)

geocoder = GoogleGeocoder(google_key)

location = geocoder.get(search_addr)
location = location[0]
print('Address of ', search_addr, ' is ', location.formatted_address)

loc_lat = location.geometry.location.lat
loc_lng = location.geometry.location.lng

print('Latitude and Longitudes of ', search_addr, ' are ', [loc_lat, loc_lng])

loc_lat_lng = [loc_lat, loc_lng]
loc_lat_lng = ",".join(map(str,loc_lat_lng))
loc = str(loc_lat_lng)
print(loc)


params = {
  'size': '600x300', # max 640x640 pixels
  'location': loc,
  'heading': '0;90;180;270;360',
  'pitch': '0',
  'key': google_key
}


api_list = google_streetview.helpers.api_list(params)
results = google_streetview.api.results(api_list)
results.download_links(str(search_addr))
results.save_metadata('metadata.json')
