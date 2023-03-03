#!/usr/bin/env python3

import os
import argparse
from Bio import SeqIO

# Adding input, output and help arguments
parser = argparse.ArgumentParser(description='Calculating assembly metrics')
parser.add_argument('test_data', metavar='test_data', type=str, help='input fasta file from genome assembly')
parser.add_argument('-o', metavar='quast_test_output', type=str, default=None, help='mention the name of output directory or file or path the output to be saved')

args = parser.parse_args()

# opening the file and creating lists of contigs and their lengths
records = []
lengths = []
with open(args.test_data, 'r') as handle:
    for record in SeqIO.parse(handle, 'fasta'):
        if len(record.seq) >= 500:
            records.append(record)
            lengths.append(len(record.seq))

# Number of contigs, total length and largest contig
total_contigs = len(records)
largest_contig = max(lengths)
total_length = sum(lengths)

# N50
lengths.sort(reverse=True)
n50 = 0
current_length = 0
for length in lengths:
    current_length += length
    if current_length >= total_length / 2:
        n50 = length
        break

# copying metrics to output file
if args.o:
    output_file = args.o
else:
    output_file = 'report.txt'

with open(output_file, 'w') as handle:
    handle.write(f'Number of contigs: {total_contigs}\n')
    handle.write(f'Total length: {total_length}\n')
    handle.write(f'Largest contig: {largest_contig}\n')
    handle.write(f'N50: {n50}\n')

print(f'Results written to {output_file}')
