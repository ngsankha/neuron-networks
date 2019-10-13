import csv

def hash_entry(item):
    seq, num = item.split("-")
    result = 0
    for c in seq:
        result <<= 2
        if c == 'A':
            result |= 0
        elif c == 'T':
            result |= 1
        elif c == 'G':
            result |= 2
        elif c == 'C':
            result |= 3
        else:
            raise RuntimeError("unexpected")

    result = (result * 1000) + int(num)
    return result

with open('dataset.tsv', 'r') as fin:
    reader = csv.reader(fin, delimiter='\t')
    with open('dataset-hash.tsv', 'w') as fout:
        writer = csv.writer(fout, delimiter='\t')
        for line in reader:
            writer.writerow(map(hash_entry, line))
