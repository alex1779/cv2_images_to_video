# cv2_images_to_video

## Requirements
```
opencv-python==4.5.5.64
```

## Installation on Windows using Anaconda
```
conda create -n cv2_images_to_video -y && conda activate cv2_images_to_video && conda install python=3.9.7 -y
git clone https://github.com/alex1779/cv2_images_to_video.git
cd cv2_images_to_video
pip install -r requirements.txt
```

## For running

When you done to install the requirements.
you must put in console something like this:

```
python main.py -i input/ -o output/example.mp4 -fps 30
```

# note that:

	-i   #is the path folder to your image	
	-o   #is the full path to your video with format .mp4 
	-fps # is the number of frames per minute



