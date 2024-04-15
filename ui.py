import tkinter as tk


def calculate_compatibility():
    label_result.config(text="Compatibility Score: (Placeholder)")


root = tk.Tk()
root.title("Actor Compatibility Check")
root.geometry("500x250")

root.configure(bg='light blue')

label_actor1 = tk.Label(root, text="Enter first actor's name:", bg = 'light blue')
label_actor1.pack()
entry_actor1 = tk.Entry(root)
entry_actor1.pack()

label_actor2 = tk.Label(root, text="Enter second actor's name:")
label_actor2.pack()
entry_actor2 = tk.Entry(root)
entry_actor2.pack()

button_calculate = tk.Button(root, text="Calculate Compatibility", command=calculate_compatibility)
button_calculate.pack()

label_result = tk.Label(root, text="Compatibility Score: ")
label_result.pack()

root.mainloop()
