import argparse
from pkg_resources import resource_filename
from pangolin.model import *
import vcf
import gffutils
import pandas as pd
import pyfastx
# import time
# startTime = time.time()

IN_MAP = np.asarray([[0, 0, 0, 0],
                     [1, 0, 0, 0],
                     [0, 1, 0, 0],
                     [0, 0, 1, 0],
                     [0, 0, 0, 1]])

if torch.cuda.is_available():
    print("Using GPU")
else:
    print("Using CPU")


def one_hot_encode(seq, strand):
    seq = seq.upper().replace('A', '1').replace('C', '2')
    seq = seq.replace('G', '3').replace('T', '4').replace('N', '0')
    if strand == '+':
        seq = np.asarray(list(map(int, list(seq))))
    elif strand == '-':
        seq = np.asarray(list(map(int, list(seq[::-1]))))
        seq = (5 - seq) % 5  # Reverse complement
    return IN_MAP[seq.astype('int8')]


def compute_score(seq, strand, models):
    # one hot encoding
    seq = one_hot_encode(seq, strand).T
    # convert to torch tensor
    seq = torch.from_numpy(np.expand_dims(seq, axis=0)).float()
    # load to gpu
    if torch.cuda.is_available():
        seq = seq.to(torch.device("cuda"))

    # iterate through 4 tissues (heart, liver, brain, testis) 
    for j in range(4):
        # iterate through 3 models that trained specific for the tissue
        for model in models[3*j:3*j+3]:
            with torch.no_grad():
                # extract predicted splice site strength for the specific tissue
                seq_scores = model(seq)[0][[1,4,7,10][j],:].cpu().numpy()
                # as the Reverse complement of - strand is used for prediction, it needs to be fliped back to match original seq
                if strand == '-':
                    seq_scores = seq_scores[::-1]
            """ .... your analysis here ..."""

models = []
# heart-spliced, liver-spliced, brain-spliced, testis-spliced models
for i in [0,2,4,6]:
    # trained model 1-3
    for j in range(1,4):
        model = Pangolin(L, W, AR)
        if torch.cuda.is_available():
            model.cuda()
            weights = torch.load(resource_filename(__name__,"models/final.%s.%s.3.v2" % (j, i)))
        else:
            weights = torch.load(resource_filename(__name__,"models/final.%s.%s.3.v2" % (j, i)), map_location=torch.device('cpu'))
        model.load_state_dict(weights)
        model.eval()
        models.append(model)

seq = '5000bp upstream + your sequence of interest + 5000bp downstream' # recommended
# call compute score function
compute_score(seq, '+', models)
