Team Name: Group 19
Team Members: Amit Athi Kesavan, Jaden Yun, and Brendan Wind
Project Title: ActorMesh
Problem:
How do we know which actors are the most compatible with each other when casting for roles?
Motivation: 
There are over 759,487 unique movies in our data set, and with no efficient and user-friendly way to sort between them, we can program a solution to this problem so that we can find actors that work well with each other based on their history co starring in movies together
Features:
We want to make a user interactable window which allows the user to input two actors/actress names. Once it has the names our algorithm will run through our movies and actor list graph and link actor nodes together with a weight based on (1/# of movies the actors co starred in). This way, when our algorithm parses through the graph, we are incentivized to seek the lowest weight connections between actors. Based on this, a rating will be given on how compatible the actors are based on their previous work.
Data:
https://www.kaggle.com/datasets/gsimonx37/letterboxd?resource=download&select=movies.csv 
Tools:
Pandas, Jupyter, SFML, Matplotlib, Networkx, Tkinter, Plotly
Visuals: 


Strategy: 
We will use pandas to concatenate our csv files to a format we can use. We will then build our graph from scratch in python using the movies and actors in them for our nodes. Once our graph is built, we will import data sets in the form of pairs with the first node in the pair being an int variable holding the movieID, and the second node of the pair holding a vector of actor names in the form of strings. For each of these pairs being imported, we will update our graph with connections between every combination of actors in that data set, creating new nodes and edges where necessary. The weights of each edge will be determined by the number of movies those nodes (actors) have in common, with the numerical weight being (1 / # of co starred movies). This will help us later on in development when we apply Dijkstra’s Algorithm and Bellman-Ford’s Algorithm to find the shortest path between nodes, or the highest number of movies that certain actors have in common. Finally, a compatibility score will be computed using these two algorithms and the speed will be compared to see which is more efficient. In the end the program will give the user a rating on how strongly connected the actors are and if they should work together.
Distribution of Responsibility and Roles: 
Reading/Cleaning, and Analyzing Data: Brendan
Functionality and Display of Data: Jaden
Development of User Interface (SFML): Amit
References: 
https://www.kaggle.com/datasets/gsimonx37/letterboxd?resource=download&select=movies.csv 
https://plotly.com/python/network-graphs/ 
