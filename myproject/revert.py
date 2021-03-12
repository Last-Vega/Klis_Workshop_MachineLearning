from keras.preprocessing.image import load_img, img_to_array
from keras.preprocessing.image import ImageDataGenerator
import matplotlib.pyplot as plt
import numpy as np
import os
from os import listdir

def return_original_validation_data():
    dir_name_list = ['Field', 'Undiscovered', 'Bug', 'Amorphous', 'Dragon', 'Fairy', 'Mineral',
                'Flying', 'Grass', 'Human-Like', 'Monster', 'Water']
    for dir_name in dir_name_list:
        target_dir = './AllDataSet/validation/' + dir_name + '/'
        # .DS_Storeを除外
        fltr_list = [filename for filename in listdir(target_dir) if not filename.startswith('.')]
        # すでに水増しされたデータを除外
        fltr_list = [filename for filename in listdir(target_dir) if filename.startswith('zoomed')]

        for f_name in fltr_list:
            filename = target_dir + f_name
            os.remove(filename)


return_original_validation_data()
