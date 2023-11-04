"""
Lions and cheetahs image classification example.

Classify lion or cheetah images using a pre-trained Deep Learning model with
the PyTorch framework.

:Authors: JLPy
:Version: 2023.11.01.01

"""
# start import
import os
from os.path import (
  join,
  isfile
)
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import cv2 as cv


# end import


class cfg:
  """
  Static configurations for the project.
  
  :Cls prj_path: Project's working directory on the hard drive.
  :Cls img_path: The directory of the images under the project folder.
  :Cls sub_dirs: A list of the image directories for lions and cheetahs.
  :Cls labels: 0 refers to lions and 1 refers to cheetahs.
  
  .. card::
  """
  
  prj_path = os.environ.get("JLDPPATH")
  img_path = 'res/images'
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
  
  def __init__(self) -> None:
    """
    Explore class constractor.
    
    Load the data into an instance of this class.
    """
    data = []
    sub_paths = [join(cfg.prj_path, cfg.img_path, x) for x in cfg.sub_dirs]
    for s, l in zip(sub_paths, cfg.labels):
      for f in os.listdir(s):
        if '.jpg' in f and isfile(d := join(s, f)):
          data.append((d, l))
    self.df = pd.DataFrame(data, columns=['file_path', 'label'])
  
  def countBar(self) -> None:
    """
    Show count plot using 'label' column.
    """
    print(self.df.groupby(['label']).count())
    sns.countplot(self.df, x='label')
  
  def showFigures(self) -> None:
    """
    Show figures plot for jpg files.
    """
    dfg = self.df.groupby('label')
    dfs = dfg.apply(lambda x: x.sample(3, replace=False))
    dfs = dfs.reset_index(drop=True)
    dfs = dfs.sample(frac=1).reset_index(drop=True)
    
    fig, ax = plt.subplots(2, 3, figsize=(10, 6))
    
    for i in range(2):
      for j in range(3):
        label = dfs.label[i * 3 + j]
        file_path = dfs.file_path[i * 3 + j]
        
        image = cv.imread(file_path)
        image = cv.cvtColor(image, cv.COLOR_BGR2RGB)
        image = cv.resize(image, (256, 256))
        
        ax[i, j].imshow(image)
        ax[i, j].set_title(
          f"Label: {label} ({'Lion' if label == 0 else 'Cheetah'})")
        ax[i, j].axis('off')
    
    plt.tight_layout()
    plt.show()


if __name__ == '__main__':
  ex = Explore()
  ex.countBar()
  ex.showFigures()
