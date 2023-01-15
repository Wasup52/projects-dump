import cv2
from cv2 import dnn_superres
import os

def save_upscale(img_path):
    img_name = img_path.split("/")[len(img_path.split("."))]

    # Create an SR object
    sr = dnn_superres.DnnSuperResImpl_create()

    # Read image
    image = cv2.imread(img_path)

    file_ = "FSRCNN_x2.pb"

    sr.readModel("get_diapo/models/" + file_)

    # Set the desired model and scale to get correct pre- and post-processing
    num = int(file_.split(".")[0][len(file_.split(".")[0]) - 1])
    sr.setModel("fsrcnn", num)

    # Upscale the image
    result = sr.upsample(image)

    # Save the image
    print(img_name)
    cv2.imwrite("get_diapo/diapos-compta-upscaled/" + img_name, result)

dir_path = "get_diapo/diapos-compta"
files = os.listdir(dir_path)

for img in files:
    img_path = dir_path + "/" + img
    save_upscale(img_path)