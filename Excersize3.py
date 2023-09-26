import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

import networkx as nx
import numpy as np

def generate_barabasi_albert_graph(n0, N, M):
    # Create a star graph with n0 nodes
    G = nx.star_graph(n0)
    
    # Add N - n0 nodes with preferential attachment
    for k in range(n0, N):
        # Calculate link probabilities for each existing node
        probabilities = [G.degree(i) / (2 * (G.number_of_edges())) for i in G.nodes]
        
        # Choose M existing nodes to connect to the new node
        targets = np.random.choice(G.nodes, size=M, replace=False, p=probabilities)
        
        # Add the new node and its edges
        G.add_node(k)
        for target in targets:
            G.add_edge(k, target)
    
    return G


def calculate_page_rank(G, alpha, T):
    # Simulate random surfer
    page_rank = {node: 0 for node in G.nodes}
    current_node = np.random.choice(list(G.nodes))
    
    for _ in range(T):
        if np.random.rand() < alpha:
            # Randomly choose a neighbor to follow
            neighbors = list(G.neighbors(current_node))
            if neighbors:
                current_node = np.random.choice(neighbors)
        else:
            # Move to a random node not connected to the current node
            non_neighbors = [node for node in G.nodes if node != current_node and not G.has_edge(current_node, node)]
            if non_neighbors:
                current_node = np.random.choice(non_neighbors)
        # Update PageRank
        page_rank[current_node] += 1
    
    # Normalize PageRank values
    for node in page_rank:
        page_rank[node] /= T
    
    return page_rank

# Parameters
n0 = 5  # Initial star graph nodes
N = 400  # Total number of nodes
M = 4  # Number of links for each new node
alpha = 0.15  # Probability to follow a link
T = 100000  # Number of steps for PageRank simulation

# Generate the Barabasi-Albert graph
G = generate_barabasi_albert_graph(n0, N, M)

# Calculate PageRank
page_rank = calculate_page_rank(G, alpha, T)

# Visualize the network
plt.figure(figsize=(10, 8))
pos = nx.spring_layout(G, seed=42)
nx.draw(G, pos, node_size=10, node_color='b', with_labels=False, alpha=0.5)
plt.title('Barabasi-Albert Network')
plt.show()

# Visualize PageRank distribution
plt.hist(page_rank.values(), bins=20, alpha=0.75)
plt.title('PageRank Distribution')
plt.xlabel('PageRank Value')
plt.ylabel('Frequency')
plt.show()
