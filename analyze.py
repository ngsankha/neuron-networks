import snap
G = snap.LoadEdgeList(snap.PUNGraph, "dataset-hash.tsv", 0, 1)
snap.PrintInfo(G, "graph")
CmtyV = snap.TCnComV()
modularity = snap.CommunityGirvanNewman(G, CmtyV)
for Cmty in CmtyV:
    print("Community: ")
    for NI in Cmty:
        print(NI)
print("The modularity of the network is %f" % modularity)

# import pandas as pd

# df = pd.read_csv('dataset.tsv', delimiter='\t', header=None)
# elems = set(df[0])
# elems.update(df[1])
# for item in elems:
#     seq, num = item.split('-')
#     assert set(list(seq)) == set('ATGC') or set(list(seq)).issubset(set('ATGC')), seq
#     assert int(num) < 1000, num
