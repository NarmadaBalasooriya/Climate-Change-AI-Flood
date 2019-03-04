import os
from street_view import get_google_streetview
from cyclegan_visualize import save_cyclegan_images
from options.test_options import TestOptions

import shutil

def check_model(search_loc, google_api_key):

	opt = TestOptions().parse()

	place_addr = search_loc
	opt.name = "cyclegan_floods_v2"
	#place_addr = ",".join(place_addr)
	if os.path.isdir(place_addr):
		print('File exists')
	else:
		real_img_path = get_google_streetview(place_addr, google_api_key)
		print('Saved google street view images of %s to %s' %(place_addr, real_img_path))

		fake_img_path = save_cyclegan_images(opt, place_addr, opt.aspect_ratio)

		os.remove(os.path.join(real_img_path, "metadata.json"))

		for root, dirs, files in os.walk(fake_img_path):
			if not files:
				continue
			prefix = os.path.basename(root)

			for f in files:
				os.rename(os.path.join(root, f), os.path.join(root, "{}_{}".format(prefix, f)))

		print('Saved generated images to %s' %(fake_img_path))

	src_files = os.listdir(place_addr)
	dst = "./images"
	for file in src_files:
		full_f_name = os.path.join(place_addr, file)
		if(os.path.isfile(full_f_name)):
			shutil.copy(full_f_name, dst)

	print('Done Generating Images')
