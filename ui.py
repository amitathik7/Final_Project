import tkinter as tk
from tkinter import ttk, Toplevel, Label
import pickle
from collections import defaultdict
from threading import Thread

import main
from main import *

# Load data from pickle
def default_dict():
    return defaultdict(list)

with open("pickle_files/adjacency_list.pkl", "rb") as f:
    adjacency_list = pickle.load(f)

actor_names = list(adjacency_list.keys())

# Search function for the actor names drop-down list
def search(event):
    if event.keysym == "Return":  # Reduce unnecessary event firing by handling only when Return key is pressed
        return
    value = event.widget.get()
    if value:
        data = [item for item in actor_names if value.lower() in item.lower()]
        event.widget['values'] = data
    else:
        event.widget['values'] = actor_names

def handle_selection_change(event):
    # This will trigger when an actual selection is made either by mouse or keyboard
    event.widget.set(event.widget.get())

#Calls the algorithm from main and rounds and displays it in the UI window
def run_calculations(actor1, actor2, adjacency_list):
    dijk_result, dijk_time = main.dijsktra_search(actor1, actor2, adjacency_list)
    bf_result, bf_time = main.bellman_ford_search(actor1, actor2, adjacency_list)

    dijk_result_rounded = round(dijk_result, 2)
    dijk_time_rounded = round(dijk_time, 2)
    bf_result_rounded = round(bf_result, 2)
    bf_time_rounded = round(bf_time, 2)

    if dijk_result < 0:
        rating = "Invalid. Make sure Actor(s) exists and name is typed case sensitive."
    elif dijk_result_rounded < 2:
        rating = "Very Bad Connection"
    elif dijk_result_rounded < 3:
        rating = "Weak Connection"
    elif dijk_result_rounded < 4:
        rating = "Decent Connection"
    elif dijk_result_rounded < 5:
        rating = "Strong Connection"
    elif dijk_result_rounded < 6:
        rating = "Very Strong Connection"
    else:
        rating = "As good as it gets! Extremely strong connection!"

    root.after(0, label_result.config, {"text": f"Dijsktra Score for {actor1} and {actor2}: {dijk_result_rounded} Time: {dijk_time_rounded} \n Bellman Ford Score: {bf_result_rounded} Time: {bf_time_rounded} \n Rating: {rating}"})

#Handling function for when the calculation is running
def calculate_compatibility():
    actor1 = combo_actor1.get()
    actor2 = combo_actor2.get()
    label_result.config(text="Calculating... Please wait.")
    Thread(target=run_calculations, args=(actor1, actor2, adjacency_list)).start()

# Window for displaying the information about the program
def open_info_window():
    info_window = Toplevel(root)
    info_window.title("Information")
    info_window.geometry("400x400")
    info_window.configure(background='black')

    # Header label
    header_label = Label(info_window, text="What is ActorMesh?", font=('Helvetica', 16, 'bold'), background='black', foreground='white')
    header_label.pack(pady=(10, 0))  # Add padding to separate from the main text

    paragraph_text = ("ActorMesh is a program that allows you to see how compatibile any two actors you can think of are! "
                      "Using our advanced algorithm, ActorMesh will go through millions of connections of cast members and the movies"
                      " they have worked on to see how just compatible two actors are. This tool would be a casting director's dream to see"
                      " how they can put a cast together, or can just be used by any movie fan prospecting about how much chemistry their"
                      " favorite hollywood stars have. Due to the nature of the project, we use two different "
                      "algorithms to calculate the rank to compare their speeds, but the rank will be the same each time. "
                      "All you have to do is think of two actors and get to meshing!")
    info_label = Label(info_window, text= paragraph_text, background='black', foreground='white', wraplength=280)
    info_label.pack(pady=20)

# Window for the scoring legend of the scores
def open_legend_window():
    legend_window = Toplevel(root)
    legend_window.title("Scoring Legend")
    legend_window.geometry("500x200")
    legend_window.configure(background='black')
    legend_text = ("Scoring Legend:\n\n"
                   "< 2: Very Bad, not great chemistry between these two\n"
                   "2-3: Not the Best connection\n"
                   "3-4: Solidly Connected\n"
                   "4-5: Strong Connection\n"
                   "5-6: Very Strong Connection\n"
                   "> 6: As Good as it Gets! These two are dynamite!")
    legend_label = Label(legend_window, text=legend_text, background='black', foreground='white', justify=tk.LEFT, font=("Helvetica", 12))
    legend_label.pack(pady=20, padx=20)

# Main window settings
root = tk.Tk()
root.title("Actor Mesh")
root.configure(background='black')
window_width = 500
window_height = 500
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width // 2) - (window_width // 2)
y = (screen_height // 2) - (window_height // 2)
root.geometry(f"{window_width}x{window_height}+{x}+{y}")

rainbow_colors = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']
color_index = 0

# Function to make the title flash rainbow
def update_color():
    global color_index
    title_label.config(foreground=rainbow_colors[color_index % len(rainbow_colors)])
    color_index += 1
    root.after(500, update_color)

title_label = tk.Label(root, text="Actor Mesh", font=("Arial", 38, 'bold'), background='black')
title_label.pack(pady=(10, 0))
update_color()

label_actor1 = tk.Label(root, text="Enter first actor's name:", background='black', foreground='white')
label_actor1.pack(fill='x')
combo_actor1 = ttk.Combobox(root, values=actor_names)
combo_actor1.pack(pady=10)
combo_actor1.bind('<KeyRelease>', search)
combo_actor1.bind('<<ComboboxSelected>>', handle_selection_change)

label_actor2 = tk.Label(root, text="Enter second actor's name:", background='black', foreground='white')
label_actor2.pack(fill='x')
combo_actor2 = ttk.Combobox(root, values=actor_names)
combo_actor2.pack(pady=10)
combo_actor2.bind('<KeyRelease>', search)
combo_actor2.bind('<<ComboboxSelected>>', handle_selection_change)

button_calculate = tk.Button(root, text="Calculate Compatibility", command=calculate_compatibility)
button_calculate.pack(pady=20)

label_result = tk.Label(root, text="Compatibility Score: ", background='black', foreground='white')
label_result.pack(pady=10)

button_info = tk.Button(root, text="What is ActorMesh?", command=open_info_window)
button_info.pack(pady=10)

button_legend = tk.Button(root, text="Open Scoring Legend", command=open_legend_window)
button_legend.pack(pady=10)

root.mainloop()
