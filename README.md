# seqstats
Print basic stats from sequence files.

## Usage
`usage: seqstats [-h] [-f {fasta,clustal,embl,genbank,imgt,phd,pir,tab}] [-v]
                seqfile [seqfile ...]`

## Installation
This is a Python script, so, you can just run the uniqseq.py file or put a symbolic link in any directory of your PATH (e.g. /usr/local/bin). The second option is recommend.

## Dependencies
* Python3
* Biopython
* argparse
* statistics

## OSs
It runs in Linux, probably in Mac OS too, but not tested.

## Examples
`seqstats seq.fasta`

`seqstats seq1.pir seq2.pir -f pir`

