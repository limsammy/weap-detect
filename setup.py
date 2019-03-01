# Run this to fetch and unpack datasets

from urllib.request import urlretrieve
import os	
import tarfile

TRAIN_TAR_URL = 'https://storage.googleapis.com/weap-detect-bucket/datasets/train.tar.gz'
TEST_TAR_URL = 'https://storage.googleapis.com/weap-detect-bucket/datasets/test.tar.gz'
TRAIN_PATH = 'images/train'
TEST_PATH = 'images/test'

def create_dir(path):
	print("[INFO] checking to see if {} exists...".format(path))
	if not os.path.exists(path):
		print("[INFO] {} not found! Creating {} directory...".format(
			path, path))
		os.makedir(path)
		print("[INFO] {} successfully created!".format(path))
	else:
		print("[INFO] {} already exists...".format(path))

def dl_tarball(url):
	try:
		print("[INFO] fetching {}...".format(url))

		file_name = url.split('/')[-1]
		output_location = 'images/{}'.format(file_name)

		urlretrieve(url, output_location)
		print("[INFO] successfully saved file to {}...".format(output_location))

	except Exception as e:
		print("[ERROR] something went wrong downloading file from url: {}".format(
			url))
		print(e)

def unpack_tarball(ball_path):
	tf = tarfile.open(ball_path, "r:gz")
	tf.extractall()

def run():
	print("[INFO] beginning directory setup...")
	try:
		create_dir(TRAIN_PATH)
		create_dir(TEST_PATH)

		print("[INFO] successfully created/verified directories are present!")
	except Exception as e:
		print("[ERROR] failed to create directories...")
		print(e)

	print("[INFO] beginning file fetching...")
	try:
		dl_tarball(TRAIN_TAR_URL)
		dl_tarball(TEST_TAR_URL)

		print("[INFO] successfully downloaded tarballs!")
	except Exception as e:
		print("[ERROR] failed to download tarballs...")

	print("[INFO] attempting to unpack tarballs...")
	try:
		unpack_tarball()


run()
