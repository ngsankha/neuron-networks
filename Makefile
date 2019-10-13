all: dataset.tsv dataset-hash.tsv analyze
.PHONY: all analyze

dataset.tsv:
	wget -O dataset.tsv.gz http://snap.stanford.edu/biodata/datasets/10023/files/CC-Neuron_cci.tsv.gz;\
  gunzip dataset.tsv.gz

dataset-hash.tsv: preprocess.py
	pipenv run python preprocess.py

analyze: analyze.py
	pipenv run python analyze.py
