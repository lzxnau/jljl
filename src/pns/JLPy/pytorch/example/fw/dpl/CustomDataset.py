import io
import time
from torch.utils.data import (
  DataLoader,
  IterableDataset
)


class MyIterableDataset(IterableDataset):
  
  def __init__(self):
    self.stream = io.StringIO()
  
  def __iter__(self):
    while True:
      # Generate a data sample
      data_sample = time.time()
      
      # Write the data sample to the stream
      self.stream.write(str(data_sample) + '\n')
      
      time.sleep(1)
      
      # Yield the data sample
      yield data_sample


my_dataset = MyIterableDataset()

dataloader = DataLoader(my_dataset, batch_size=3)

for batch in dataloader:
  print(batch)
