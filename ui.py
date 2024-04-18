import tkinter as tk
from tkinter import ttk
import pickle
from collections import defaultdict

import main
from main import *

# Load data from pickle
def default_dict():
    return defaultdict(list)

with open("pickle_files/adjacency_list.pkl", "rb") as f:
    adjacency_list = pickle.load(f)

actor_names = list(adjacency_list.keys())

print(len(actor_names))
# Function to update ComboBox values based on search
def search(event):
    value = event.widget.get()
    if value:
        data = [item for item in actor_names if value.lower() in item.lower()]
        event.widget['values'] = data
    else:
        event.widget['values'] = actor_names

def calculate_compatibility():
    actor1 = combo_actor1.get()
    actor2 = combo_actor2.get()
    # Placeholder for compatibility calculation

    dijk_result, dijk_time = main.dijsktra_search(actor1, actor2, adjacency_list)
    bf_result, bf_time = main.bellman_ford_search(actor1, actor2, adjacency_list)
    label_result.config(text=f"Compatibility Score for {actor1} and {actor2}: {dijk_result} Time: {dijk_time}")

# Create the main window
root = tk.Tk()
root.title("Actor Mesh")

def update_color():
    global color_index
    title_label.config(foreground=rainbow_colors[color_index % len(rainbow_colors)])
    color_index += 1
    root.after(500, update_color)  # Update the color every 500 milliseconds

# Set the window to appear in the center of the screen
window_width = 500
window_height = 350
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width // 2) - (window_width // 2)
y = (screen_height // 2) - (window_height // 2)
root.geometry(f"{window_width}x{window_height}+{x}+{y}")

# Define rainbow colors
rainbow_colors = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']
color_index = 0

# Create and pack the title label
title_label = tk.Label(root, text="Actor Mesh", font=("Helvetica", 16))
title_label.pack(pady=(10, 0))

# Start the color animation
update_color()

# Title text
title_label = tk.Label(root, text="Actor Mesh", font=("Helvetica", 16))
title_label.pack(pady=(10, 0))

# First actor selection with label
label_actor1 = tk.Label(root, text="Enter first actor's name:")
label_actor1.pack(fill='x')
combo_actor1 = ttk.Combobox(root, values=actor_names)
combo_actor1.pack(pady=10)
combo_actor1.bind('<KeyRelease>', search)

# Second actor selection with label
label_actor2 = tk.Label(root, text="Enter second actor's name:")
label_actor2.pack(fill='x')
combo_actor2 = ttk.Combobox(root, values=actor_names)
combo_actor2.pack(pady=10)
combo_actor2.bind('<KeyRelease>', search)

# Button to calculate compatibility
button_calculate = tk.Button(root, text="Calculate Compatibility", command=calculate_compatibility)
button_calculate.pack(pady=20)

# Label to display the result
label_result = tk.Label(root, text="Compatibility Score: ")
label_result.pack(pady=10)

root.mainloop()
