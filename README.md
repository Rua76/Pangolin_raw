# Pangolin_raw
A sample code for getting raw Pangolin prediction from sequence
Assume you have pulled the published Pangolin repository https://github.com/tkzeng/Pangolin, you can put it in /pangolin folder so this code could work
Assume you have a list of pre-mRNA sequences as fasta seqs that you prepared by yourself. Note that it is recommended to have 5,000 bp flanking the target sequence, but it is not necessary for Pangolin to do prediction. It can predict on sequence with arbitrary length.
The models loaded in this sample code is the same as the published Pangolin, 3 models for 4 tissues. You can always edit to load more/less models
