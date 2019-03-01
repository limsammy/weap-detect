# Weap Detect

### Instructions
## Setup 
  - Clone repo locally `git clone git@github.com:limsammy/weap-detect.git`
  - Navigate to project directory `cd weap-detect`
  - Create python virtualenv `virtualenv env`
  - Activate environment `source env/bin/activate`
  - Install python dependencies from requirements.txt file `pip install -r requirements.txt`


  - Install OpenCV using this guide [here](https://www.pyimagesearch.com/2018/08/17/install-opencv-4-on-macos/) and create python site-packages symlink as `cv2`


  - Install tensorflow model library locally `git clone git@github.com:tensorflow/models.git`


## Getting Started
  - Uncompress train and test images and place images in correct directories with the setup file `python setup.py`
  - Run `python images/xml_to_csv.py` to generate csv files
  - Generate tfrecords `python images/generate_tfrecord.py --csv_input=data/train_labels.csv --output_path=data/train.record`
  - Create training directory `mkdir training`
  - Pull SSD Mobilenet model
  - Make sure the ckpt file in the mobilenet dir is named `model.cpkt`


  - Train your model locally `python models/research/object_detection/model_main.py--pipeline_config_path=training/pipeline.config --model_dir=training/ --num_train_steps=5000 --num_eval_steps=2000  --alsologtostderr`


  - Export graphs
  - Paste graphs into outputs folder
  - Count number of bounding boxes `python image_detection.py`


### utils/image_resizer.py
  - usage
    - python image_resizer.py -input=input_folder_images -output=output_folder -height=800 -width=600


### References:
  - Modified version of xml_to_csv.py from racoon github repo.
  - generate_tfrecord.py from racoon github repo.
