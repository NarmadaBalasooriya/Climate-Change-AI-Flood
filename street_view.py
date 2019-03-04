import os
from googlegeocoder import GoogleGeocoder
import google_streetview.api


def get_google_streetview(addr, google_key):

	geocoder = GoogleGeocoder(google_key)
	location = geocoder.get(addr)
	location = location[0]

	loc_lat = location.geometry.location.lat
	loc_lng = location.geometry.location.lng 

	loc_lat_lng = [loc_lat, loc_lng]
	loc_lat_lng = ",".join(map(str, loc_lat_lng))
	loc = str(loc_lat_lng)

	params = {
		'size': '512x512',
		'location': loc,
		'heading': '0;90;180;270;360',
		'pitch': '0',
		'key': google_key
	}

	real_img_path = addr
	api_list = google_streetview.helpers.api_list(params)
	results = google_streetview.api.results(api_list)
	results.download_links(str(real_img_path))
	check = results.download_links(str(real_img_path))
	print('results: ', check)
	return real_img_path
