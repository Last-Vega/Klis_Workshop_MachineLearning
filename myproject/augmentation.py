from keras.preprocessing.image import load_img, img_to_array
from keras.preprocessing.image import ImageDataGenerator
import matplotlib.pyplot as plt
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
                horizontal_flip=True,
                vertical_flip=True
            )

            if dir_name == 'Field':
                # 1個の画像を生成します
                g = datagen.flow(x, batch_size=1, save_to_dir=target_dir, save_prefix='fliped', save_format='png')
                for i in range(1):
                    batch = g.next()

            elif dir_name == 'Undiscovered':
                # 4個の画像を生成します
                g = datagen.flow(x, batch_size=1, save_to_dir=target_dir, save_prefix='fliped', save_format='png')
                for i in range(4):
                    batch = g.next()

            elif dir_name == 'Bug':
                # 5個の画像を生成します
                g = datagen.flow(x, batch_size=1, save_to_dir=target_dir, save_prefix='fliped', save_format='png')
                for i in range(5):
                    batch = g.next()


            elif dir_name == 'Water':
                # 6個の画像を生成します
                g = datagen.flow(x, batch_size=1, save_to_dir=target_dir, save_prefix='fliped', save_format='png')
                for i in range(6):
                    batch = g.next()

            elif dir_name == 'Human-Like':
                # 11個の画像を生成します
                g = datagen.flow(x, batch_size=1, save_to_dir=target_dir, save_prefix='fliped', save_format='png')
                for i in range(11):
                    batch = g.next()

            elif dir_name == 'Monster':
                # 12個の画像を生成します
                g = datagen.flow(x, batch_size=1, save_to_dir=target_dir, save_prefix='fliped', save_format='png')
                for i in range(12):
                    batch = g.next()

            else:
                # 8個の画像を生成します
                g = datagen.flow(x, batch_size=1, save_to_dir=target_dir, save_prefix='fliped', save_format='png')
                for i in range(8):
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
                horizontal_flip=True,
                vertical_flip=True
            )

            if dir_name == 'Field':
                # 1個の画像を生成します
                g = datagen.flow(x, batch_size=1, save_to_dir=target_dir, save_prefix='fliped', save_format='png')
                for i in range(1):
                    batch = g.next()

            elif dir_name == 'Undiscovered':
                # 4個の画像を生成します
                g = datagen.flow(x, batch_size=1, save_to_dir=target_dir, save_prefix='fliped', save_format='png')
                for i in range(4):
                    batch = g.next()

            elif dir_name == 'Bug':
                # 5個の画像を生成します
                g = datagen.flow(x, batch_size=1, save_to_dir=target_dir, save_prefix='fliped', save_format='png')
                for i in range(5):
                    batch = g.next()


            elif dir_name == 'Water':
                # 6個の画像を生成します
                g = datagen.flow(x, batch_size=1, save_to_dir=target_dir, save_prefix='fliped', save_format='png')
                for i in range(6):
                    batch = g.next()

            elif dir_name == 'Human-Like':
                # 11個の画像を生成します
                g = datagen.flow(x, batch_size=1, save_to_dir=target_dir, save_prefix='fliped', save_format='png')
                for i in range(11):
                    batch = g.next()

            elif dir_name == 'Monster':
                # 12個の画像を生成します
                g = datagen.flow(x, batch_size=1, save_to_dir=target_dir, save_prefix='fliped', save_format='png')
                for i in range(12):
                    batch = g.next()

            else:
                # 8個の画像を生成します
                g = datagen.flow(x, batch_size=1, save_to_dir=target_dir, save_prefix='fliped', save_format='png')
                for i in range(8):
                    batch = g.next()

validation_data_augmentation()
