from torchvision.datasets import FashionMNIST
from torchvision import transforms 
import numpy as np

train_data = FashionMNIST(root='./data',
                          train= True,
                          transform = transforms.Compose([transforms.Resize(size=224),transforms.ToTensor()]),
                          download = True)