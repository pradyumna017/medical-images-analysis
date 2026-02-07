import torch.nn as nn
from torchvision.models import densenet121

class XRayModel(nn.Module):
    def __init__(self):
        super().__init__()
        self.model = densenet121(pretrained=True)
        self.model.features.conv0 = nn.Conv2d(
            1, 64, kernel_size=7, stride=2, padding=3, bias=False
        )
        self.model.classifier = nn.Linear(1024, 1)

    def forward(self, x):
        return self.model(x)
