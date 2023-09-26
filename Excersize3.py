import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

import networkx as nx
import numpy as np

def generate_barabasi_albert_graph(n0, N, M):
    """
    We genereren met deze defenitie een grafiek met n0 nodes, N nodes aan de buitenkant en M grootte van de nodes
    
    """
    # De beginster gaan we maken met n0 nodes om de hub en we noemen deze samenstelling G. Het eerste spinnenweb is dus G
    G = nx.star_graph(n0)
    
    # We maken N - n0 nieuwe nodes en voegen deze aan de buitenkant van G (het oorspronkelijke spinnenweb dus)
    for k in range(n0, N):
        # We rekenen uit wat de kans is dat er lijn zit tussen 2 nodes
        probabilities = [G.degree(i) / (2 * (G.number_of_edges())) for i in G.nodes]
        
        # Kies M bestaande nodes om met de nieuwe node te verbinden
        targets = np.random.choice(G.nodes, size=M, replace=False, p=probabilities)
        
        # Hier voegen we de nieuwe node daadwerkelijk toe en voegen we hem teo aan het spinnenweb 
        G.add_node(k)
        for target in targets:
            G.add_edge(k, target)
    # Hier geven we het spinnenweb terug   
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


n0 = 5  
N = 400  
M = 4  
alpha = 0.15  
T = 100000  

# Hier voeren we de eerder gemaakte functie uit met bovenstaande getallen
G = generate_barabasi_albert_graph(n0, N, M)

# Calculate PageRank
page_rank = calculate_page_rank(G, alpha, T)

# print de grafiek
plt.figure(figsize=(10, 8))
pos = nx.spring_layout(G, seed=42)
nx.draw(G, pos, node_size=10, node_color='b', with_labels=False, alpha=0.5)
plt.title('Barabasi-Albert Network')
plt.show()

# print de histogram
plt.hist(page_rank.values(), bins=20, alpha=0.75)
plt.title('PageRank Distribution')
plt.xlabel('PageRank Value')
plt.ylabel('Frequency')
plt.show()
