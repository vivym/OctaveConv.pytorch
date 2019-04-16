from torchvision.models import resnet18, resnet34, resnet50, resnet101, resnet152
from .octave_resnet import octave_resnet50, octave_resnet101, octave_resnet152

__all__ = [
    "resnet18", "resnet34", "resnet50", "resnet101", "resnet152",
    "octave_resnet50", "octave_resnet101", "octave_resnet152",
]
