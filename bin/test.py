import torch
import torch.nn as nn
import torch.optim as optim
import torchvision
import torchvision.transforms as transforms
import torchvision.models as models

resnet = models.resnet18(pretrained=False)

for name, module in resnet.named_modules():
    print(name, module)
