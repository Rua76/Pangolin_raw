# Pangolin_raw
A sample code for getting raw Pangolin prediction from sequence 

**Warning: This is not a tested working code, it is only a snipplet to show how to convert your sequence to one-hot encoded sequence, and use Pangolin to get raw prediction**

Assume you have pulled the published Pangolin repository https://github.com/tkzeng/Pangolin, this snipplet is intended to work in the */pangolin* folder 

Assume you have a list of pre-mRNA sequences as fasta seqs that you prepared by yourself. Note that it is recommended to have 5,000 bp flanking both side of the target sequence, but it is not necessary for Pangolin to do prediction. It can predict on sequence with arbitrary length. 

The number of models loaded in this sample code is the same as the published Pangolin, 3 models for each of the 4 tissues. You can always edit to load more/less models.
