import pickle
import time
from collections import defaultdict

def default_dict():
    return defaultdict(list)

start = time.time()
with open("pickle_files/adjacency_list.pkl", "rb") as f:
    adjacency_list = pickle.load(f)
end = time.time()

print(f'Time taken to load adjacency list: {end - start}')
def dijsktra_search(start_name, end_name):
    return -1

def bellman_ford_search(start_name, end_name):
    return -1