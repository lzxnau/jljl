---
myst:
  substitutions:
    plc: '/pytorch/example/cv/ic/lions_cheetahs.py'
    cim: |
      :start-after: start import
      :end-before: end import
    ccf: ':pyobject: cfg'
    cex: ':pyobject: Explore'
---

# CV-IC Lions and Cheetahs

PyTorch computer vision example project for image classification of lions and
cheetahs

## Explore Source Data

The first step is to become familiar with the data.
{{ ddin.format('1. Import modules and classes',plc,cim) }}
{{ ddin.format('2. Add configurations into cfg class',plc,ccf) }}
{{ ddin.format('3. Add explore methods into Explore class',plc,cex) }}
