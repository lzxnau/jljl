import io
import time
from torch.utils.data import (
  Dataset,
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


class MyDataset(Dataset):
  
  def __init__(self):
    self.ds = [[x, x * 2] for x in range(10)]
  
  def __getitem__(self, idx):
    return self.ds[idx]
  
  def __len__(self):
    return len(self.ds)


# my_dataset = MyIterableDataset()

# dataloader = DataLoader(my_dataset, batch_size=3)


mds = MyDataset()

dl = DataLoader(mds, batch_size=2)

for batch in dl:
  print(batch)
