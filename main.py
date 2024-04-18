import pickle
import sys
import time
from collections import defaultdict

def dijsktra_search(start_name, end_name, adj_list):
    start = time.time()
    if start_name not in adj_list.keys() or end_name not in adj_list.keys():
        return -1, (time.time() - start)

    # This is for when the two actors given are the same in which case their compataibility score would be invalid
    if start_name == end_name:
        return -1, (time.time() - start)

    # We initialize the distance map and the set of visited actors/vertices
    distance = defaultdict(float)
    visited_actors = set()

    for actor in adj_list:
        if actor != start_name:
            distance[actor] = sys.maxsize
        else:
            distance[actor] = 0

    # Setting the current actor to the starting actor
    curr_actor = start_name

    while (curr_actor != 'invalid'):
        curr_distance = distance[curr_actor]

        for neighbor, movies in adj_list[curr_actor].items():
            neighbor_distance = curr_distance + (1 / len(movies))
            if (distance[neighbor] > neighbor_distance):
                distance[neighbor] = neighbor_distance

        visited_actors.add(curr_actor)

        min = sys.maxsize

        for actor in adj_list:
            if distance[actor] < min and actor not in visited_actors:
                curr_actor = actor
                min = distance[curr_actor]

        if (min == sys.maxsize):
            curr_actor = 'invalid'

    final_score = 1 / distance[end_name]
    return final_score, (time.time() - start)


def bellman_ford_search(start_name, end_name, adj_list):
    return -1, -1