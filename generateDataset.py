#Baixa as imagens para o dataset com as categorias do searchObjects e a configuração do arquivo do test.txt e valid.txt

import glob
import os
from pathlib import Path
root = Path().cwd()/"dataset"

from jmd_imagescraper.core import *

categories = [
  "cadeira",
  "porta de casa",
  "mesa",
  "sofa"
]

maxResults = 50

params = {
  "max_results": maxResults,
  "img_size":    ImgSize.Cached,
  "img_type":    ImgType.Photo,
}

for category in categories:
  try:
    duckduckgo_search(root, category, category, **params)
  except:
    pass
# Percentage of images to be used for the valid set
percentage_test = 10;
# Create train.txt and valid.txt
file_train = open(str(root) + "/train.txt", 'w')  
file_test = open(str(root) + "/valid.txt", 'w')
# Populate train.txt and valid.txt
index_test = round(100 / percentage_test)
for category in categories:
  counter = 1
  current_dir = root/category
  for file in glob.iglob(os.path.join(current_dir, '*.jpg')):  
      title, ext = os.path.splitext(os.path.basename(file))
      if counter == index_test:
          counter = 1
          file_test.write(str(current_dir) + "/" + title + '.jpg' + "\n")
      else:
          file_train.write(str(current_dir) + "/" + title + '.jpg' + "\n")
          counter = counter + 1