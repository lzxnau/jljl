# Data Loading Pipeline

## {doc}`torch.utlis.data <pytorch:data>`

It provides base classes for processing PyTorch data loading pipelines. This
package focuses on data [loading]{.wpg}, [sampling]{.wpg}, [batching]{.wpg}, and
[feeding]{.wpg}. Data transformation is optional. Two main classes are
[Dataset]{.wpr} and [DataLoader]{.wpr}. If you want to use your own sampling
strategy, you can use the [Sampler]{.wpr} class. This package supports
[async]{.wpg} and [multiprocess]{.wpg} workflows, with some parameters you can
change to control
its behavior.

:::{mermaid}
flowchart LR
Source--load-->Dataset
subgraph Dataset
Loading
end
Dataset-->DataLoader
subgraph DataLoader
direction TB
Sampling-->Batching
Batching-->Feeding
end
DataLoader--feed-->Model
:::
---
:::bgb
This is a test.
:::
:::fgg
This is a block.
:::