"""
Lion and cheetah image classification example.

Classify lion or cheetah images using a pre-trained Deep Learning model with
the PyTorch framework.

:Authors: JLPy
:Version: 2023.11.01.01

"""

import os
from os.path import (
  join,
  isfile
)
import pandas as pd


class cfg:
  """
  Static configurations for the project.
  
  :Cls root_path: The directory of the images on the hard drive.
  :Cls sub_dirs: A list of the image directories for lions and cheetahs.
  :Cls labels: 0 refers to lion and 1 refers to cheetah.
  
  .. card::
  """
  
  root_path = 'res/images'  # this is a test.
  sub_dirs = ('Lions', 'Cheetahs')
  labels = (0, 1)


class Explore:
  """
  Prepare and Explore Data.
  
  This is the first step to explore the source data and to become familiar with
  the data.
  
  :Ins df: A pandas dataframe to store all file records with two columns\
           file_path and label.
            
  .. card::
  """
  
  def __init__(self):
    """
    Explore class constractor.
    
    Load the data into an instance of this class.
    """
    
    data = []
    sub_paths = [join(cfg.root_path, x) for x in cfg.sub_dirs]
    for s, l in zip(sub_paths, cfg.labels):
      for f in os.listdir(s):
        if '.jpg' in f and isfile(d := join(s, f)):
          data.append((d, l))
    self.df = pd.DataFrame(data, columns=['file_path', 'label'])


if __name__ == '__main__':
  ex = Explore()
  print(ex.df.head())
