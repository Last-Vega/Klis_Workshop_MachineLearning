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



3枚ずつ増やしたとき (4倍近くになる)
train Field : 803
train Undiscovered : 396
train Bug : 308
train Amorphous : 204
train Dragon : 214
train Fairy : 188
train Mineral : 190
train Flying : 195
train Grass : 184
train Human-Like : 144
train Monster : 124
train Water : 256

validation Field : 722
validation Undiscovered : 292
validation Bug : 272
validation Amorphous : 194
validation Dragon : 187
validation Fairy : 182
validation Mineral : 184
validation Flying : 167
validation Grass : 152
validation Human-Like : 142
validation Monster : 124
validation Water : 231
"""
