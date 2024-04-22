
Project Title: ActorMesh

HOW TO RUN:
First, make sure you have all files and run the adjacency_list_creator.py file. This should take
roughly a minute and will create our graph from scratch. Once this is created, then run the ui.py file.
This should launch the actor mesh window, and you can now get to meshing!

Problem:
How do we know which actors are the most compatible with each other when casting for roles?

Motivation:
There are over 759,487 unique movies in our data set, and with no efficient and user-friendly
way to sort between them, we can program a solution to this problem so that we can find actors
that work well with each other based on their history co starring in movies together

Features:
We want to make a user interactable window which allows the user to input two actors/actress
names. Once it has the names our algorithm will run through our movies and actor list graph and
link actor nodes together with a weight based on (1/# of movies the actors co starred in). This
way, when our algorithm parses through the graph, we are incentivized to seek the lowest weight
connections between actors. Based on this, a rating will be given on how compatible the actors
are based on their previous work