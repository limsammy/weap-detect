# Run this to fetch and unpack datasets

import os
import requests
import urllib.request

TRAIN_TAR_URL = 'https://storage.googleapis.com/weap-detect-bucket/datasets/train.tar.gz'
TEST_TAR_URL = 'https://storage.googleapis.com/weap-detect-bucket/datasets/test.tar.gz'
TRAIN_PATH = 'images/train'
TEST_PATH = 'images/test'

def create_dir(path):
	if not os.path.exists(path):
		os.makedirs(path)


