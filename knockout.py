import graph_tool.all as gt
import sys
import numpy as np
import matplotlib
matplotlib.use("macOSX")
from matplotlib import pyplot as plt

FILENAME = sys.argv[1]
KNOCKOUT = 0.01

def deg_frequency(degrees):
  deg_count = {}
  for d in degrees:
    if d in deg_count:
      deg_count[d] += 1
    else:
      deg_count[d] = 1
  return zip(*deg_count.items())

def plot_log_log_dist(g, fname):
    (data_xs, data_ys) = deg_frequency(g.get_total_degrees(g.get_vertices()))
    ys = np.divide(data_ys, np.sum(data_ys))
    plt.clf()
    plt.scatter(data_xs, ys, alpha=0.5, color='b', label='Dataset')
    plt.legend(loc='lower left')
    plt.xscale('log')
    plt.yscale('log')
    plt.xlim(0.5, 1500)
    plt.ylim(0.0001, 0.5)
    plt.xlabel("degree")
    plt.ylabel("fraction of nodes")
    plt.savefig(fname)

G = gt.load_graph_from_csv(FILENAME, csv_options={"delimiter": "\t"})
plot_log_log_dist(G, "dist.png")
# state1 = gt.minimize_blockmodel_dl(G, verbose=True)
N = len(G.get_vertices())
print(len(G.get_edges()))

knock_count = int(KNOCKOUT * N)
# to_remove = np.random.randint(0, N, knock_count)
# G.remove_vertex(to_remove)

# top_degree_nodes = [[idx[0], elem] for idx, elem in np.ndenumerate(G.get_total_degrees(G.get_vertices()))]
# top_degree_nodes.sort(key=lambda x: x[1], reverse=True)
# top_degree_nodes = top_degree_nodes[0:knock_count]
# top_degree_nodes = [i[1] for i in top_degree_nodes]
# G.remove_vertex(top_degree_nodes)

eival, eivec = gt.eigenvector(G)
to_remove = list(np.argsort(-eivec.get_array())[0:knock_count])
G.remove_vertex(to_remove)
plot_log_log_dist(G, "dist2.png")

# print(len(G.get_vertices()))
# print(len(G.get_edges()))
# plot_log_log_dist(G, "dist2.png")
# state2 = gt.minimize_blockmodel_dl(G, verbose=True)

# print(state1)
# print(state2)
