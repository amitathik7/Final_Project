import csv
import pickle
from collections import defaultdict
import time

# We need to initialize a function to return the default dict object since later on
# when we decided to use the pickle library to store the adjacency list, it had problems
# with us using a lambda function to initialize the adjacency list.
# I don't know why that happens but other people who had the same problem said this works
# and it works for us.
def default_dict():
    return defaultdict(list)

start = time.time()
# Initialize an empty dictionary to store the adjacency list
adjacency_list = defaultdict(default_dict)

# Go through the combined csv file
# We need to specify the utf-8 encoding because when we read it without that there are some
# untypical characters in people's names that aren't read properly.
with open('csv_files/movies_and_actors.csv', newline='', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile)
    next(reader)  # Skip the header row

    # Read through each row of movie names + actor names in the file
    for row in reader:
        movie_name, actors_str = row

        # Turn the list of actors in the .csv file into a list in python using eval()
        actors_list = eval(actors_str)

        # For every connection between the two actors we want the list of their common movies
        # to include the current movie we are on in the .csv file.
        for i in range(len(actors_list)):
            for j in range(i + 1, len(actors_list)):
                actor1, actor2 = actors_list[i], actors_list[j]

                # We add the movies on both ways since we want to be able to access the common movies
                # from both actors
                adjacency_list[actor1][actor2].append(movie_name)
                adjacency_list[actor2][actor1].append(movie_name)
end = time.time()

sorted_list = dict(sorted(adjacency_list.items(), key= lambda item: len(item[1])))
final_list = defaultdict(default_dict)

i = 0

# Sorting it and taking only the top 10000 actors by connection count because before
# the connection count was too much
for key, value in reversed(sorted_list.items()):
    if i >= 10000:
        break
    print(key, len(value))
    final_list[key] = value
    i += 1

print(f'Time take for creating adjacency list: {end - start}')

start = time.time()
# Now we save the adjacency list into a .pkl file
# It reduces the time it takes for getting the adjacency list from ~21 seconds to ~2 seconds
# It does take ~5 seconds to store it as the .pkl file but since we only do that once it does not
# contribute to the time in main.py
with open('pickle_files/adjacency_list.pkl', 'wb') as temp:
    pickle.dump(final_list, temp)
end = time.time()

print(f'Time taken for storing adjacency list: {end - start}')