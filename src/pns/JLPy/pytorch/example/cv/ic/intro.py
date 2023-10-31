"""
Introduction Example.

An introduction example to PyTorch image classification for computer vision.

:Authors: JLPy
:Version: 2023.10.26.01

.. note::

   This is a note.
"""
from torch.utils.data import Dataset
import pandas as pd


class ImageDataset(Dataset):
  """
  Custom Image Dataset that inherits from the superclass
  ``torch.utils.data.Dataset``.

  .. card::
  
     PyTorch's Dataset
     ^^^
     
     Abstract Class:
     
        Declare an abstract method ``__getitem__()``.
        
     Container Class:
     
        As a container, it must define the ``__getitem__()`` method to
        allow container objects to be subscribed to. A subclass that implements
        ``__getitem__()`` will be a container class.
        
     Sequence Container:
     
        Like sequence containers ``list`` and ``tuple``, it is subscribed
        to using an ``int`` or a slice.
        
     Implement ``__getitem__()``:
     
        When a sequence container implements this method, it will use an ``int``
        as an index to get an item from the container.
        
     Define ``__getitems__()``: Optional
     
        When a sequence container implements this method, it will use a slice
        to get a range of items from the container.
        
     Mapping Container:
     
        When a subclass try to use a key to fetch the items, it
        
     .. warning::
     
        It is not a mapping container because it does not use a key to
        subscribe.
        
     +++
     1. ``__getitem__()``.
     * Optional method ``__len__()``.
     * Optional method ``__getitems__()``.
     
  .. card::
  
     **ImageDataset**
     ^^^
  """
  
  def __init__(self, df: pd.DataFrame):
    """
    Class Constractor.
    
    This constractor will create an instance of the Dataset class.
    """
    self.df = df
  
  def __getitem__(self, idx: int) -> list:
    """
    Overwrite the abstract method from supper class Pytorch Dataset.
    
    This  method is for a container class that supports subscription.
    
    .. note::
    
       PyTorch's ``Dataset`` supports both integers and slices for
       subscription, so it will be an object of a sequence class, such as a
       ``list`` or ``tuple``.
  
    :param idx: Data index.
    :return:
    """
    return list(self.df.iloc[idx])
