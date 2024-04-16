import pandas as pd

# We read the movies.csv file and the actors.csv file into 2 dataframes
movies_df = pd.read_csv('csv_files/movies.csv')
actors_df = pd.read_csv('csv_files/actors.csv')

# We merge the dataframes based on the column of movie id's (id)
combined_df = pd.merge(movies_df, actors_df, on='id')

# We combine all the entries with the same movie id and put all the names into a list
combined_df = combined_df.groupby('movie_name')['actor_name'].agg(list).reset_index()

# Write the combined .csv files into a new .csv file for us to use later
combined_df.to_csv('csv_files/movies_and_actors.csv', index=False)
