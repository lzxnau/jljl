---
myst:
  substitutions:
    plc: '/pytorch/example/cv/ic/lions_cheetahs.py'
    cim: |
      :start-after: start import
      :end-before: end import
    ccf: ':pyobject: cfg'
    cex: ':pyobject: Explore'
    cid: ':pyobject: ImgsDataset'
---

# CV-IC Lions and Cheetahs

PyTorch computer vision example project for image classification of lions and
cheetahs

## Explore Source Data

Step 1: Become familiar with the data.
{{ ddin.format('1. Import modules and classes',plc,cim) }}
{{ ddin.format('2. Add configurations into cfg class',plc,ccf) }}
{{ ddin.format('3. Add explore methods into Explore class',plc,cex) }}
{bdg-link-info}`Explore Output <explore.ipynb>`

---

## Data Loading Pipeline

Step 2: Customize a subclass of [Dataset]{.pcls} to load the data and use two
[Dataloader]{.pcls}s to batch and sample the data for training and validation.

{{ ddin.format('1. Custom a subclass of Dataset',plc,cid) }}
{bdg-link-info}`Data Pipeline Output <data_pipeline.ipynb>`

---

## Prepare the model

Step 3: Prepare the model


---

Jupyter Output Reference:

:::{toctree}
explore
data_pipeline
:::
