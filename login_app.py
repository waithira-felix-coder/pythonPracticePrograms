import tkinter as tk
from tkinter import messagebox
from tkinter import font as tkfont

# -------------------- LOGIN FUNCTION --------------------
def login():
    username = entry_username.get()
    password = entry_password.get()

    # Simple hardcoded credentials (for learning)
    if username == "admin" and password == "1234":
        messagebox.showinfo("Login Successful", "Welcome, Admin!")
    else:
        messagebox.showerror("Login Failed", "Invalid username or password")


# -------------------- MAIN WINDOW --------------------
root = tk.Tk()
root.title("Login System")
root.geometry("350x220")
root.resizable(True, False)

# -------------------- HEADING --------------------
label_title = tk.Label(root, text="User Login", font=("Arial", 16, "bold"))
label_title.pack(pady=10)

# -------------------- USERNAME --------------------
frame_username = tk.Frame(root)
frame_username.pack(pady=5)

label_username = tk.Label(frame_username, text="Username:", width=10, anchor="w")
label_username.pack(side="left")

entry_username = tk.Entry(frame_username, width=25)
entry_username.pack(side="left")

# -------------------- PASSWORD --------------------
frame_password = tk.Frame(root)`        `
frame_password.pack(pady=5)

label_password = tk.Label(frame_password, text="Password:", width=10, anchor="w")
label_password.pack(side="left")

entry_password = tk.Entry(frame_password, width=25, show="*")
entry_password.pack(side="left")

# -------------------- LOGIN BUTTON --------------------
btn_login = tk.Button(root, text="Login", width=15, command=login)
btn_login.pack(pady=15)

# -------------------- START EVENT LOOP --------------------
root.mainloop()
