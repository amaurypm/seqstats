#!/usr/bin/env python3
## Print basic stats from sequence files.
##
## Amaury Pupo Merino
## amaury.pupo@gmail.com
##
## This script is released under GPL v3.
##

## Importing modules
import argparse
import sys
from Bio import SeqIO
from statistics import mean, median, mode

## Functions
def print_stats(seqfilename, fmt):
    """Print sequence stats.
    """
    print("File:\t{}".format(seqfilename))
    seq_lengths = []
    try:
        for record in SeqIO.parse(seqfilename, fmt):
            seq_lengths.append(len(record))

    except ValueError:
        sys.stderr.write("ERROR: File {} has not a valid {} format.".format(seqfilename, fmt))
        return 

    seq_lengths_len = len(seq_lengths)
    print("\t{:,d} sequence{}.".format(seq_lengths_len, "" if seq_lengths_len == 1 else "s"))
    if seq_lengths_len > 1:
        print("\tSequence length stats:")
        print("\t\tMin:\t{:,d}".format(min(seq_lengths)))
        print("\t\tMean:\t{:,.1f}".format(mean(seq_lengths)))
        try:
            print("\t\tMode:\t{:,d}".format(mode(seq_lengths)))

        except:
            print("\t\tMode: no unique mode")

        print("\t\tMedian:\t{:,.1f}".format(median(seq_lengths)))
        print("\t\tMax:\t{:,d}".format(max(seq_lengths)))
        print("\t\tTotal:\t{:,d}".format(sum(seq_lengths)))

    elif len(seq_lengths) == 1:
        print("\tSequence length:\t{:,d}".format(seq_lengths[0]))

    print("\n")
        
## Main
def main():
    """Main function.
    """
    parser=argparse.ArgumentParser(description="Print basic stats from sequence files.")
    parser.add_argument('seqfile', nargs='+', help='Sequence file.')
    parser.add_argument('-f', '--format', choices=['fasta','clustal', 'embl', 'genbank', 'imgt', 'phd', 'pir', 'tab'], default='fasta', help='Sequence format [default: %(default)s].')
    parser.add_argument('-v', '--version', action='version', version='0.9.3', help="Show program's version number and exit.")

    args=parser.parse_args()

    for infile in args.seqfile:
        print_stats(infile, args.format)

## Running the script
if __name__ == "__main__":
        main()

