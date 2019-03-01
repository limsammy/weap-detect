# Run this to fetch and unpack datasets

import os
import requests

TRAIN_PATH = 'images/train'
TEST_PATH = 'images/test'

def create_dir(path):
	if not os.path.exists(path):
		os.makedirs(path)

