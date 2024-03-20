Team Name: Group 19
Team Members: Amit Athi Kesavan, Jaden Yun, and Brendan Wind
Project Title: MovieMatch
Problem:
How can we find the movies we want to watch?
Motivation: 
There are over 759,487 unique movies in our data set, and with no efficient and user-friendly way to sort between them, we can program a solution to this problem so that we can find the movies we want to watch.
Features: 
We want to make a user interactable “search engine” allowing users to search up movies using a variety of filters. For example “What are the top 10 rated movies starring Margot Robbie?” or “What are the 5 most popular movies made in France?” With this extensive dataset we can answer these questions and store movie data into different data structures to see which ones are more efficient for grabbing our search results.
Data:
https://www.kaggle.com/datasets/gsimonx37/letterboxd?resource=download&select=movies.csv 
Tools:
Pandas, Jupyter, SFML, Matplotlib, Networkx, Tkinter, Plotly
Visuals: 

Strategy: 
We would go through the actors.csv file and reformat it to where each entry has an actor’s name and a list of the movie id’s of movies they acted in. We would also go through the directors.csv file and reformat it to where each entry has a director’s name and a list of the movie id’s of movies they directed. We would go through movies.csv and turn it into a B tree based on the movie ID. We would be comparing the efficiency of breadth-first search vs. depth-first search.
Distribution of Responsibility and Roles: 
Reading/Cleaning, and Analyzing Data: Brendan
Functionality and Display of Data: Jaden
Development of User Interface (SFML): Amit
References: 
https://www.kaggle.com/datasets/gsimonx37/letterboxd?resource=download&select=movies.csv 
https://plotly.com/python/network-graphs/ 
