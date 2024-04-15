import csv
import pickle
import time
from collections import defaultdict

def default_dict():
    return defaultdict(list)

with open("movies_and_actors.pickle", "rb") as f:
    adjacency_list = pickle.load(f)

actor_names = list()

for actors, movies in adjacency_list.items():
    actor_names.append(actors)

print(actor_names)