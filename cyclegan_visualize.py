import os
from options.test_options import TestOptions
from data import create_dataset
from models import create_model
from util.visualizer import save_images
from util import html, util
from util.util import tensor2im, save_image, mkdirs
import numpy as np
import sys
import ntpath
import time
from subprocess import Popen, PIPE
from scipy.misc import imresize
from street_view import get_google_streetview

def save_cyclegan_images(opt, place_addr, aspect_ratio):

	#opt = TestOptions().parse()

	opt.num_threads = 0
	opt.batch_size = 1
	opt.serial_batches = True
	opt.no_flip = True
	opt.display_id = -1

	opt.dataroot = place_addr

	dataset = create_dataset(opt)
	model = create_model(opt)
	model.setup(opt)

	fake_im_path = place_addr
	if not os.path.exists(fake_im_path):
		os.makedirs(fake_im_path)

	if opt.eval:
		model.eval()
	for i, data in enumerate(dataset):
		model.set_input(data)
		model.test()
		visuals = model.get_current_visuals()
		img_path = model.get_image_paths()

		for label, im in visuals.items():
			im = tensor2im(im)
			im_name = '%s_%d.jpg' % (label, i)
			save_path = os.path.join(fake_im_path, im_name)
			h, w, _ = im.shape
			if aspect_ratio > 1.0:
				im = imresize(im, (h, int(w * aspect_ratio)), interp='bicubic')
			if aspect_ratio < 1.0:
				im = imresize(im, (int(h / aspect_ratio), w), interp='bicubic')
			save_image(im, save_path)

	return fake_im_path
