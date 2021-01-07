## 各種ファイルに関しての説明

- PrepareTrainPokemonData.ipynb
  - 学習用の画像データにラベル付けするためのプログラム

- PrepareValidationPokemonData.ipynb
  - 検証用の画像データにラベル付けするためのプログラム

- TrainPokemonEggType.ipynb
 - VGG16をFine-tuningして学習したモデルを保存するプログラム (実行結果は各クラス1200枚のときのもの)

- TestPokemonEggType.ipynb
 - 学習したモデルを読み込んでテストするプログラム　(実行結果は各クラス1200枚のときのもの)

- augmentation.py 
 - 上下左右反転の画像で各クラス400枚程度に水増しするプログラム

- - augmentation-2.py 
 - 拡大縮小の画像で各クラス1200枚程度に水増しするプログラム