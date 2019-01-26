from PIL import Image
import os
import numpy as np
from keras import datasets

cifar_classes = ['airplane', 'automobile', 'bird', 'cat', 'deer', 'dog', 'frog', 'horse', 'ship', 'truck']

type = input('Which dataset do you want to generate (1) MNIST 2) CIFAR10)? ')
if type == "1":
    (X_train, y_train), (X_test, y_test) = datasets.mnist.load_data()
elif type == "2":
    (X_train, y_train), (X_test, y_test) = datasets.cifar10.load_data()
else:
    exit()

base_path = os.popen("pwd").read().strip()
img_folder, label_file = "dataset", "labels.txt"

remove_cmd = 'rm -rf ' + img_folder + ' ' + label_file
create_cmd = 'mkdir ' + img_folder + '; touch ' + label_file

if os.path.exists(img_folder):
    os.system(remove_cmd)
os.system(create_cmd)

# ex) the number of images per class is 100 !
img_cnt_per_class = int(input('How many images per class? '))

class_cnt = [0] * 10
for i in range(X_train.shape[0]):
    y_idx = int(y_train[i]) if type == '1' else y_train[i][0]
    y_value = str(y_train[i]) if type=='1' else str(cifar_classes[y_train[i][0]])
    if class_cnt[y_idx] < img_cnt_per_class:
        filename = img_folder + os.sep + y_value + "_" + str(i).zfill(5) + ".png"

        im = Image.fromarray(np.uint8(X_train[i]))
        im.save(filename)

        label_cmd = "echo " + base_path + os.sep + filename + " " + str(y_idx) + " >> labels.txt"
        os.system(label_cmd)

        class_cnt[y_idx] += 1
