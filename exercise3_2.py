import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


# Load the squirrel network data
edges_df = pd.read_csv('squirrel_edges.csv')

# Create a directed graph
G = nx.DiGraph()

# Add edges from the dataframe
for _, row in edges_df.iterrows():
    source, target = row['Source'], row['Target']
    G.add_edge(source, target)

# Calculate PageRank
page_rank = nx.pagerank(G)

# Visualize PageRank distribution
plt.hist(page_rank.values(), bins=20, alpha=0.75)
plt.title('PageRank Distribution')
plt.xlabel('PageRank Value')
plt.ylabel('Frequency')
plt.show()