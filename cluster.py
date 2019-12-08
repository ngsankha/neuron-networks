import csv
import logging

history = {}
logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s', level=logging.DEBUG)

with open('cluster.txt') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter='\t')
    node_id = 0
    for row in csv_reader:
        for item in row:
            history[item] = node_id
        node_id += 1

logging.info("Read clusters")

written = set()
with open('data.tsv') as src:
    reader = csv.reader(src, delimiter='\t')
    with open('output.tsv', 'w') as dst:
        writer = csv.writer(dst, delimiter='\t')
        for row in reader:
            lhs = row[0]
            rhs = row[1]
            if lhs not in history:
                history[lhs] = node_id
                node_id += 1
            if rhs not in history:
                history[rhs] = node_id
                node_id += 1

            if history[lhs] == history[rhs] or "{} {}".format(history[lhs], history[rhs]) in written:
                continue
            else:
                written.add("{} {}".format(history[lhs], history[rhs]))
                writer.writerow([history[lhs], history[rhs]])

logging.info("wrote reduced graph")
