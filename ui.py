import tkinter as tk
from tkinter import ttk
import pickle
from collections import defaultdict

# Load data from pickle
def default_dict():
    return defaultdict(list)

with open("movies_and_actors.pickle", "rb") as f:
    adjacency_list = pickle.load(f)

actor_names = list(adjacency_list.keys())

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
    label_result.config(text=f"Compatibility Score: (Placeholder for {actor1} and {actor2})")

# Create the main window
root = tk.Tk()
root.title("Actor Mesh")
root.geometry("500x300")

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
