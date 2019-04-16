# OctaveConv.pytorch
A Pytorch Implementation for the paper [Drop an Octave: Reducing Spatial Redundancy in Convolutional Neural Networks with Octave Convolution](https://arxiv.org/abs/1904.05049).
![](figures/octave_conv.png)


## Usage
```python
from models import octave_resnet50

model = octave_resnet50(num_classes=10)
```
## Reference
Inspired by the MXNet implementation [here](https://github.com/terrychenism/OctaveConv).
