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


def search(event):
    value = event.widget.get()
    if value:
        data = [item for item in actor_names if value.lower() in item.lower()]
        event.widget['values'] = data
    else:
        event.widget['values'] = actor_names


def run_calculations(actor1, actor2, adjacency_list):
    dijk_result, dijk_time = main.dijsktra_search(actor1, actor2, adjacency_list)
    bf_result, bf_time = main.bellman_ford_search(actor1, actor2, adjacency_list)

    # Round results
    dijk_result_rounded = round(dijk_result, 2)
    dijk_time_rounded = round(dijk_time, 2)

    # Update the UI with results on the main thread
    root.after(0, label_result.config, {
        "text": f"Compatibility Score for {actor1} and {actor2}: {dijk_result_rounded} Time: {dijk_time_rounded}"})


def calculate_compatibility():
    actor1 = combo_actor1.get()
    actor2 = combo_actor2.get()
    # Set the label to show loading state
    label_result.config(text="Calculating... Please wait.")
    # Start thread to perform the calculation
    Thread(target=run_calculations, args=(actor1, actor2, adjacency_list)).start()


def open_info_window():
    info_window = Toplevel(root)
    info_window.title("Information")
    info_window.geometry("300x200")
    info_window.configure(background='black')
    info_label = Label(info_window, text="Here is some information about Actor Mesh.", background='black',
                       foreground='white', wraplength=280)
    info_label.pack(pady=20)


# Main window settings
root = tk.Tk()
root.title("Actor Mesh")
root.configure(background='black')

window_width = 500
window_height = 350
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width // 2) - (window_width // 2)
y = (screen_height // 2) - (window_height // 2)
root.geometry(f"{window_width}x{window_height}+{x}+{y}")

rainbow_colors = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']
color_index = 0


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

label_actor2 = tk.Label(root, text="Enter second actor's name:", background='black', foreground='white')
label_actor2.pack(fill='x')
combo_actor2 = ttk.Combobox(root, values=actor_names)
combo_actor2.pack(pady=10)
combo_actor2.bind('<KeyRelease>', search)

button_calculate = tk.Button(root, text="Calculate Compatibility", command=calculate_compatibility)
button_calculate.pack(pady=20)

label_result = tk.Label(root, text="Compatibility Score: ", background='black', foreground='white')
label_result.pack(pady=10)

button_info = tk.Button(root, text="Open Info", command=open_info_window)
button_info.pack(pady=10)

root.mainloop()
