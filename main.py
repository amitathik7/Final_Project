import csv
from collections import defaultdict

# Initialize an empty dictionary to store the adjacency list
adjacency_list = defaultdict(lambda: defaultdict(int))

# Read the CSV file and parse movie names and associated lists of actor names
with open('movies_and_actors.csv', newline='', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile)
    next(reader)  # Skip the header row

    # Iterate through each row in the CSV file
    for row in reader:
        movie_name, actors_str = row

        # Extract list of actors from the string representation
        actors_list = eval(actors_str)

        # Update adjacency list based on actors in the current movie
        for i in range(len(actors_list)):
            for j in range(i + 1, len(actors_list)):
                actor1, actor2 = actors_list[i], actors_list[j]

                # Increment the edge weight between actors
                adjacency_list[actor1][actor2] += 1
                adjacency_list[actor2][actor1] += 1

# Optionally remove self-loops and edges with weight of 1
for actor in adjacency_list:
    if actor in adjacency_list[actor]:
        del adjacency_list[actor][actor]
    adjacency_list[actor] = {other_actor: weight for other_actor, weight in adjacency_list[actor].items() if weight > 1}

# Print the adjacency list representation of the graph
for actor, neighbors in adjacency_list.items():
    print(f"{actor}: {neighbors}")
