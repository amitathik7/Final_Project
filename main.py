import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

# Read the .csv files into DataFrames
actors_df = pd.read_csv('actors.csv')
movies_df = pd.read_csv('movies.csv')

# Create a graph object
G = nx.Graph()

# Add nodes representing actors
for index, row in actors_df.iterrows():
    G.add_node(row['id'], label=row['name'], type='actor')

# Add nodes representing movies
for index, row in movies_df.iterrows():
    G.add_node(row['id'], label=row['name'], type='movie')

# Add edges connecting actors to movies
for index, row in actors_df.iterrows():
    movie_ids = row['id']
    for movie_id in movie_ids:
        G.add_edge(row['id'], movie_id)

# Compute layout
pos = nx.spring_layout(G, k=0.5, iterations=50)

# Draw the graph with adjusted layout
nx.draw(G, pos, with_labels=True, labels=nx.get_node_attributes(G, 'label'), node_color=[('blue' if ntype == 'actor' else 'red') for ntype in nx.get_node_attributes(G, 'type').values()])
plt.show()
