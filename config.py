# All the statics inside the files

# Database values
N = 16384
R = 8
P = 1
BUFLEN = 16

# Default Language
LANGUAGE = 'NL'

# camera detection settings
CAM_PNG_LOCATION = "Frame/"
MODEL_PATH = 'source/yolov8n.blob'
MODEL_SIZE = 480 # Note that the model you trained has the same dimensions so (MODEL_SIZE, MODEL_SIZE). When this is not the case specify here 
MODEL_CONFIDENCE = 0.75 # this means the model will be some percentile sure of the detection, so for example 0.75 means 75%.
MODEL_DETECTIONS = {'Bag'} #Specify what kind of object there is being detected if there are more then 1 detections at them to the row, example: {'Bag','Bicycle','dog','cat'}

# Database values
N = 16384
R = 8
P = 1
BUFLEN = 16

# Folder/File locations
PERSON_IMAGES_DIRECTORY = 'rescources/Persons' 