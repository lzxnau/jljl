"""
Lion and cheetah image classification example.

Classify lion or cheetah images using a pre-trained Deep Learning model with
the PyTorch framework.

:Authors: JLPy
:Version: 2023.11.01.01

"""


class Explore:
  """
  Prepare and Explore Data.
  
  This is the first step to explore the source data and to become familiar with
  the data.
  """
  
  def __init__(self, path: str):
    """
    Explore class constractor.
    
    Load the data into an instance of this class.
    
    :param path: The directory of the source data at local disk.
    """
    self.path = path


if __name__ == '__main__':
  ex = Explore('res/images')
  print(ex.path)
