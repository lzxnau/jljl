"""
Introduction.

This is an introduction example for Pytorch image classification.

:Authors: JLPy
:Version: 2023.10.26.01

.. note::

   This is a note.
"""
from torch.utils.data import Dataset
import pandas as pd


class ImageDataset(Dataset):
  """
  Image Dataset.
  
  This is an image dataset.
  """
  
  def __init__(self, df: pd.DataFrame):
    """
    Class Constractor.
    
    This constractor will create the instance.
    """
    self.df = df
  
  def __getitem__(self, idx: int) -> list:
    """
    A method for a container class that supports subscription.
    
    .. note::
    
       PyTorch's ``Dataset`` supports both integers and slices for
       subscription, so it will be an object of a sequence class, such as a
       ``list`` or ``tuple``.
  
    :param idx: Data index.
    :return:
    """
    return list(self.df.iloc[idx])
