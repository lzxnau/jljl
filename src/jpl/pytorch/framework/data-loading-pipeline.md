# Data Loading Pipeline

## {doc}`torch.utlis.data <pytorch:data>` Package

PyTorch's data package plays a crucial role in deep learning pipelines, with
three foundational classes at its core: [Dataset]{.wpr},[IterableDataset]{.wpr},
and [DataLoader]{.wpr}. The Dataset class supports both [map-style]{.wpg}
and [iterable-style]{.wpg} datasets, while the DataLoader efficiently
handles the complex tasks of data loading, sampling, batching, and data feeding.
For map-style datasets, custom [Sampler]{.wpr}s can be used to meet specific
needs. IterableDataset is particularly valuable for dealing with data that
exceeds available memory or requires computationally expensive loading.
This class allows data to be processed and streamed in an iterative manner.
Furthermore, PyTorch's DataLoader is adept at handling asynchronous and
multiprocessing workflows, enhancing data loading performance through
configurable parameters such as num_workers, pin_memory, and multiprocessing,
all tailored to specific hardware and data loading requirements.

---

## Map-style Dataset Pipeline

::::blc
:::{mermaid}
:caption: Map-style Dataset Pipeline
:align: center
flowchart LR
Source--init-->Dataset
subgraph Dataset
Loading
end
Dataset--getitem-->Sampler
subgraph Sampler
Sampling
end
Sampler--iter-->DataLoader
subgraph DataLoader
direction TB
Batching-->Feeding
end
DataLoader--iter-->Model
:::
:::bls

1. Map-Style Dataset Subclass of [Dataset]{.wpr}
    
    * [\_\_init\_\_()]{.wpr}: Required
    * [\_\_getitem\_\_()]{.wpr}: Required
    * [\_\_len\_\_()]{.wpr}: Optional
    * [\_\_getitems\_\_()]{.wpr}: Optional

:::
:::bls

2. [DataLoader]{.wpr}
    
    * [\_\_init\_\_()]{.wpr}: Constructor
    * [\_\_iter\_\_()]{.wpr}: Iterator

:::
:::bls

3. Optional [Sampler]{.wpr} Subclass
    
    * [\_\_init\_\_()]{.wpr}: Optional
    * [\_\_iter_\_()]{.wpr}: Required

:::
::::
---

## Iterable-style Dataset Pipeline

:::blc
:::{mermaid}
:caption: Iterable-style Dataset Pipeline
:align: center
flowchart LR
Source--iter-->IterableDataset
subgraph IterableDataset
Loading
end
IterableDataset--multiprocess-->DataLoader
subgraph DataLoader
direction TB
Batching-->Feeding
end
DataLoader--iter-->Model
:::

---

## Datasets

PyTorch supports two different types of datasets, map-style datasets and
iterable-style datasets.
:::{card}
[Dataset]{.wpr}: An abstract class
^^^

* [\_\_getitem\_\_()]{.wpr}: Required
    
    * Subclass must implement this method.
    * A map-style fetching method. It uses an integer index or string key to
      subscript one item from the dataset.
    * DataLoader only supports integer index. If the dataset is the key based
      container, a custom Sampler must be supplied.

* [\_\_len\_\_()]{.wpr}: Required
    
    * Subclass must implement this method.
    * Sampler or DataLoader will use it to get the size of the dataset.

* [\_\_getitems\_\_()]{.wpr}: Optional
    
    * This is a optional method.
    * It uses for speedup batched samples loading. This method accepts list of
      indices of samples of batch and returns list of samples.
    * A custom sampler must be supplied to fetch the key-based list of samplers.

:::
:::{card}
[IterableDataset]{.wpr} : An abstract class
^^^

*

:::
:::bgb
This is a test.
:::
:::fgg
This is a block.
:::