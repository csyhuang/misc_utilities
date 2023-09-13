# import the necessary packages
from imutils import paths
import numpy as np
import argparse
from pprint import pprint
import cv2
import os


def dhash(image, hash_size=8):
	# Source: https://www.pyimagesearch.com/2020/04/20/detect-and-remove-duplicate-images-from-a-dataset-for-deep-learning/
	# convert the image to grayscale and resize the grayscale image,
	# adding a single column (width) so we can compute the horizontal
	# gradient
	gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
	resized = cv2.resize(gray, (hash_size + 1, hash_size))
	# compute the (relative) horizontal gradient between adjacent
	# column pixels
	diff = resized[:, 1:] > resized[:, :-1]
	# convert the difference image to a hash and return it
	return sum([2 ** i for (i, v) in enumerate(diff.flatten()) if v])


def another_trial():
	"""
	https://towardsdatascience.com/finding-duplicate-images-with-python-71c04ec8051
	:return:
	"""


if __name__ == "__main__":

	imagePaths = [
		"/Users/claresyhuang/Downloads/164891292_266842288351939_3467122440782596377_n.jpg",
		"/Users/claresyhuang/Downloads/166311780_1333839610332815_5675003728725994364_n.jpg",
	]
	# grab the paths to all images in our input dataset directory and
	# then initialize our hashes dictionary
	# print("[INFO] computing image hashes...")
	# imagePaths = list(paths.list_images(args["dataset"]))
	hashes = {}
	# loop over our image paths
	for imagePath in imagePaths:
		# load the input image and compute the hash
		image = cv2.imread(imagePath)
		h = dhash(image, 32)
		# grab all image paths with that hash, add the current image
		# path to it, and store the list back in the hashes dictionary
		p = hashes.get(h, [])
		p.append(imagePath)
		hashes[h] = p

	pprint(hashes)
