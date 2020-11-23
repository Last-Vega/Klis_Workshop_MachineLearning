import numpy as np
import os
from os import listdir

def train_data_augmentation():
    dir_name_list = ['Field', 'Undiscovered', 'Bug', 'Amorphous', 'Dragon', 'Fairy', 'Mineral',
        'Flying', 'Grass', 'Human-Like', 'Monster', 'Water'
    ]

    for dir_name in dir_name_list:
        target_dir = './AllDataSet/train/' + dir_name + '/'
        # .DS_Storeの削除
        fltr_list = [filename for filename in listdir(target_dir) if not filename.startswith('.')]

        print('train', dir_name, ':', len(fltr_list) )

def validation_data_augmentation():
    dir_name_list = ['Field', 'Undiscovered', 'Bug', 'Amorphous', 'Dragon', 'Fairy', 'Mineral',
        'Flying', 'Grass', 'Human-Like', 'Monster', 'Water'
    ]
    for dir_name in dir_name_list:
        target_dir = './AllDataSet/validation/' + dir_name + '/'
        # .DS_Storeの削除
        fltr_list = [filename for filename in listdir(target_dir) if not filename.startswith('.')]

        print('validation', dir_name, ':', len(fltr_list) )

train_data_augmentation()
validation_data_augmentation()

# 出力結果
"""
水増し前
train Field : 203
train Undiscovered : 100
train Bug : 77
train Amorphous : 52
train Dragon : 54
train Fairy : 47
train Mineral : 48
train Flying : 49
train Grass : 46
train Human-Like : 36
train Monster : 31
train Water : 65

validation Field : 186
validation Undiscovered : 73
validation Bug : 68
validation Amorphous : 49
validation Dragon : 47
validation Fairy : 46
validation Mineral : 46
validation Flying : 42
validation Grass : 38
validation Human-Like : 36
validation Monster : 31
validation Water : 58

水増し後
train Field : 404
train Undiscovered : 489
train Bug : 455
train Amorphous : 460
train Dragon : 477
train Fairy : 415
train Mineral : 424
train Flying : 437
train Grass : 405
train Human-Like : 420
train Monster : 396
train Water : 443

validation Field : 371
validation Undiscovered : 358
validation Bug : 403
validation Amorphous : 430
validation Dragon : 417
validation Fairy : 407
validation Mineral : 406
validation Flying : 371
validation Grass : 335
validation Human-Like : 426
validation Monster : 391
validation Water : 400

"""
