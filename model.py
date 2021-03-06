import torch
import torch.nn as nn
import torch.nn.functional as F

class QNetwork(nn.Module):
    """Actor (Policy) Model."""

    def __init__(self, state_size, action_size, seed,
                 fc1_units=32,
                 fc2_units=64,
                 fc3_units=128,
                 fc4_units=64,
                 fc5_units=32):
        """Initialize parameters and build model.
        Params
        ======
            state_size (int): Dimension of each state
            action_size (int): Dimension of each action
            seed (int): Random seed
            fc1_units (int): Number of nodes in first hidden layer
            fc2_units (int): Number of nodes in second hidden layer
            fc3_units (int): Number of nodes in second hidden layer
        """
        super(QNetwork, self).__init__()
        self.seed = torch.manual_seed(seed)
        self.fc1 = nn.Linear(state_size, fc1_units)
        self.fc1_bn = nn.BatchNorm1d(fc1_units)
        self.fc1_dropout = nn.Dropout(0.2)
        self.fc2 = nn.Linear(fc1_units, fc2_units)
        self.fc2_bn = nn.BatchNorm1d(fc2_units)
        self.fc2_dropout = nn.Dropout(0.2)
        self.fc3 = nn.Linear(fc2_units, fc3_units)
        self.fc3_bn = nn.BatchNorm1d(fc3_units)
        self.fc3_dropout = nn.Dropout(0.2)
        self.fc4 = nn.Linear(fc3_units, fc4_units)
        self.fc4_bn = nn.BatchNorm1d(fc4_units)
        self.fc4_dropout = nn.Dropout(0.3)
        self.fc5 = nn.Linear(fc4_units, fc5_units)
        self.fc5_bn = nn.BatchNorm1d(fc5_units)
        self.fc5_dropout = nn.Dropout(0.3)
        self.fc6 = nn.Linear(fc5_units, action_size)

    def forward(self, state):
        """Build a network that maps state -> action values."""
        x = F.relu(self.fc1_dropout(self.fc1_bn(self.fc1(state))))
        x = F.relu(self.fc2_dropout(self.fc2_bn(self.fc2(x))))
        x = F.relu(self.fc3_dropout(self.fc3_bn(self.fc3(x))))
        x = F.relu(self.fc4_dropout(self.fc4_bn(self.fc4(x))))
        x = F.relu(self.fc5_dropout(self.fc5_bn(self.fc5(x))))
        return self.fc6(x)
