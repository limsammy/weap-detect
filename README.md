# Weap Detect

### Instructions
  - Create python virtualenv
  - Install python dependencies from requirements.txt file `pip install -r requirements.txt`


  - Install OpenCV using this guide [here](https://www.pyimagesearch.com/2018/08/17/install-opencv-4-on-macos/)


  - Install tensorflow model library locally `git clone git@github.com:tensorflow/models.git`


  - Uncompress train and test images
  - Run `python images/xml_to_csv.py`
  - Create tfrecords `python images/generate_tfrecord.py --csv_input=data/train_labels.csv --output_path=data/train.record`
  - Create training directory `mkdir training`
  - Pull SSD Mobilenet model
  - Make sure the ckpt file in the mobilenet dir is named `model.cpkt`
  - Train your model `python models/research/object_detection/model_main.py--pipeline_config_path=training/pipeline.config --model_dir=training/ --num_train_steps=5000 --num_eval_steps=2000  --alsologtostderr`

  - Export graphs
  - Paste graphs into outputs folder
  - Count number of bounding boxes `python image_detection.py`


### utils/image_resizer.py
  - usage
    - python image_resizer.py -input=input_folder_images -output=output_folder -height=800 -width=600


### References:
  - Modified version of xml_to_csv.py from racoon github repo.
  - generate_tfrecord.py from racoon github repo.
