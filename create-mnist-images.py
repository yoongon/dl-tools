from PIL import Image
import os
import numpy as np
from keras import datasets

(X_train, y_train), (X_test, y_test) = datasets.mnist.load_data()

base_path = os.popen("pwd").read().strip()
img_folder, label_file = "dataset", "labels.txt"
create_cmd = "mkdir " + img_folder + "; touch " + label_file
os.system(create_cmd)

# ex) the number of images per class is 100 !
img_cnt_per_class = int(input('Enter number of images per digits(0~9):'))

class_cnt = [0] * 10
for i in range(X_train.shape[0]):
    if class_cnt[y_train[i]] < img_cnt_per_class:
        filename = img_folder + os.sep + str(y_train[i]) + "_" + str(i).zfill(5) + ".png"

        im = Image.fromarray(np.uint8(X_train[i]))
        im.save(filename)

        label_cmd = "echo " + base_path + os.sep + filename + " " + str(y_train[i]) + " >> labels.txt"
        os.system(label_cmd)

        class_cnt[y_train[i]] += 1
