import tkinter as tk

def greet():
    label.config(text="Hello, " + entry.get())

root = tk.Tk()
root.title("Tkinter Demo1")
root.geometry("350x220")


entry = tk.Entry(root)
entry.pack()

button = tk.Button(root, text="Greet", command=greet)
button.pack()

label = tk.Label(root, text="Enter your name")
label.pack()

root.mainloop()
