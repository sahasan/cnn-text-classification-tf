#!/usr/bin/env python3

import sys
import sentencepiece as spm

# Usage: encode-raw.py trained-spm.model < input-file > encoded-file
#
# SPM-encodes each sequence of a raw SemEval file (Format: id \t label \t sequence)

sp = spm.SentencePieceProcessor()
sp.Load(sys.argv[1])

for line in sys.stdin:
    sline = line.strip().split('\t')
    if len(sline) != 3:
        print("Wrong format: %s" % sline, file=sys.stderr)
        continue
    id, label, sequence = sline
    seq_encoded = sp.EncodeAsPieces(sequence)
    print('\t'.join([id, label, ' '.join(seq_encoded)]))
