import csv
import pickle
from collections import defaultdict

def default_dict():
    return defaultdict(list)

# Initialize an empty dictionary to store the adjacency list
# adjacency_list = defaultdict(default_dict)
#
# # Read the CSV file and parse movie names and associated lists of actor names
# with open('movies_and_actors.csv', newline='', encoding='utf-8') as csvfile:
#     reader = csv.reader(csvfile)
#     next(reader)  # Skip the header row
#
#     # Iterate through each row in the CSV file
#     for row in reader:
#         movie_name, actors_str = row
#
#         # Extract list of actors from the string representation
#         actors_list = eval(actors_str)
#
#         # Update adjacency list based on actors in the current movie
#         for i in range(len(actors_list)):
#             for j in range(i + 1, len(actors_list)):
#                 actor1, actor2 = actors_list[i], actors_list[j]
#
#                 # Increment the edge weight between actors
#                 adjacency_list[actor1][actor2].append(movie_name)
#                 adjacency_list[actor2][actor1].append(movie_name)
#
# with open('movies_and_actors.pickle', 'wb') as f:
#     pickle.dump(adjacency_list, f)

# print(len(adjacency_list['Will Smith']['Jaden Smith']))

# Print the adjacency list representation of the graph
# for actor, neighbors in adjacency_list.items():
#     print(f"{actor}: {neighbors}")

with open("movies_and_actors.pickle", "rb") as f:
    adjacency_list = pickle.load(f)
