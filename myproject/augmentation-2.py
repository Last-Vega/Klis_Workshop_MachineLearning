from keras.preprocessing.image import load_img, img_to_array
from keras.preprocessing.image import ImageDataGenerator
import numpy as np
import os
from os import listdir

def train_data_augmentation():
    dir_name_list = ['Field', 'Undiscovered', 'Bug', 'Amorphous', 'Dragon', 'Fairy', 'Mineral',
                'Flying', 'Grass', 'Human-Like', 'Monster', 'Water']
    for dir_name in dir_name_list:
        target_dir = './AllDataSet/train/' + dir_name + '/'
        # .DS_Storeの削除
        fltr_list = [filename for filename in listdir(target_dir) if not filename.startswith('.')]

        for filename in fltr_list:
            original_image = load_img(target_dir + filename)
            x = img_to_array(original_image)
            x = np.expand_dims(x, axis=0)

            # ImageDataGeneratorの生成
            datagen = ImageDataGenerator(
                zoom_range = [0.7, 1.3]
            )

            g = datagen.flow(x, batch_size=1, save_to_dir=target_dir, save_prefix='zoomed', save_format='png')
            for i in range(2):
                batch = g.next()



train_data_augmentation()


def validation_data_augmentation():
    dir_name_list = ['Field', 'Undiscovered', 'Bug', 'Amorphous', 'Dragon', 'Fairy', 'Mineral',
                'Flying', 'Grass', 'Human-Like', 'Monster', 'Water']
    for dir_name in dir_name_list:
        target_dir = './AllDataSet/validation/' + dir_name + '/'
        # .DS_Storeの削除
        fltr_list = [filename for filename in listdir(target_dir) if not filename.startswith('.')]

        for filename in fltr_list:
            original_image = load_img(target_dir + filename)
            x = img_to_array(original_image)
            x = np.expand_dims(x, axis=0)

            # ImageDataGeneratorの生成
            datagen = ImageDataGenerator(
                zoom_range = [0.7, 1.3]
            )

            g = datagen.flow(x, batch_size=1, save_to_dir=target_dir, save_prefix='zoomed', save_format='png')
            for i in range(2):
                batch = g.next()


validation_data_augmentation()
