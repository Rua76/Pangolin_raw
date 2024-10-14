# Pangolin_raw
A sample code for getting raw Pangolin prediction from sequence 

Assume you have pulled the published Pangolin repository https://github.com/tkzeng/Pangolin, this snipplet is intended to work in the ***/pangolin*** folder 

Assume you have a list of pre-mRNA sequences as fasta seqs that you prepared by yourself. Note that it is required to have flanking  5,000 bp on both side of the target sequence (in total 10,000 flanking bp). The sequence of interest can have arbitrary length. 

The returned result will Pangolin's prediction on each bp of your **target sequence**, without 10,000 flanking bp. For each bp, there will be two labels  *[prob. unsplice, prob. splice]* and *predicted usage*. You might be primarily interested in ***prob. splice***, as it indicates predicted splice strength. 

The number of models loaded in this sample code is the same as the published Pangolin, 3 models for each of the 4 tissues. You can always edit to load more/less models.
