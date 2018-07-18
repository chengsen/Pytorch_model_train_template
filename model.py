from torch import nn

__build__ = 2018
__author__ = "singsam_jam@126.com"


class Net(nn.Module):
    def __init__(self):
        super(Net, self).__init__()

    def forward(self, x):
        return x
