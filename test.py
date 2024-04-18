import main
from main import *
import pickle
from collections import defaultdict

def default_dict():
    return defaultdict(list)


with open("pickle_files/adjacency_list.pkl", "rb") as f:
    adjacency_list = pickle.load(f)

actor_1 = input("Actor 1: ")
actor_2 = input("Actor 2: ")

da_score, da_time = main.dijsktra_search(actor_1, actor_2, adjacency_list)
bf_score, bf_time = main.bellman_ford_search(actor_1, actor_2, adjacency_list)

print(f'Dijsktra Search Results: {da_score}, {da_time}')
print(f'Bellman-Ford Search Results: {bf_score}, {bf_time}')