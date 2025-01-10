# About
Adjust SRU (simple recurrent unit) to be compatible with pytorch >=1.9. The adjustments are based on the sru repository: https://github.com/asappresearch/sru.git. Main checks and changes are deprecated functions, torch.cuda API, autograd and optimizers.

# Requirements
PyTorch >=1.9 recommended
ninja
Install requirements via 'pip install -r requirements.txt'

# Installation
## From source:
SRU can be installed as a regular package via 'python setup.py install' or 'pip install .'
## Directly use the source without installation:
Make sure this repo and CUDA library can be found by the system, e.g.

'export PYTHONPATH=path_to_repo/sru
export LD_LIBRARY_PATH=/usr/local/cuda/lib64'

# Examples
The usage of SRU is similar to nn.LSTM. SRU likely requires more stacking layers than LSTM. We recommend starting by 2 layers and use more if necessary (see our report for more experimental details).
'import torch
from sru import SRU, SRUCell

# input has length 20, batch size 32 and dimension 128
x = torch.FloatTensor(20, 32, 128).cuda()

input_size, hidden_size = 128, 128

rnn = SRU(input_size, hidden_size,
    num_layers = 2,          # number of stacking RNN layers
    dropout = 0.0,           # dropout applied between RNN layers
    bidirectional = False,   # bidirectional RNN
    layer_norm = False,      # apply layer normalization on the output of each layer
    highway_bias = -2,        # initial bias of highway gate (<= 0)
)
rnn.cuda()

output_states, c_states = rnn(x)      # forward pass

# output_states is (length, batch size, number of directions * hidden size)
# c_states is (layers, batch size, number of directions * hidden size)'

