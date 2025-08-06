import os
import csv
import tkinter as tk
from tkinter import filedialog, messagebox

def browse_folder():
    folder = filedialog.askdirectory()
    if folder:
        folder_path.set(folder)
        run_button.config(state="normal")

def run_script():
    parent_folder = folder_path.get()

    if not os.path.isdir(parent_folder):
        messagebox.showerror("Error", "Invalid directory selected.")
        return

    folder_name = os.path.basename(parent_folder.rstrip("/\\"))
    csv_filename = os.path.join(parent_folder, f"{folder_name}.csv")

    data = []
    for entry in os.listdir(parent_folder):
        full_path = os.path.join(parent_folder, entry)
        if os.path.isdir(full_path):
            data.append([entry, full_path])

    try:
        with open(csv_filename, "w", newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(["Folder Name", "Full Path"])
            writer.writerows(data)
        messagebox.showinfo("Success", f"CSV created:\n{csv_filename}")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to write CSV:\n{e}")

# GUI setup
root = tk.Tk()
root.title("Directory List to CSV")
root.geometry("400x150")

folder_path = tk.StringVar()

browse_button = tk.Button(root, text="Browse Folder", command=browse_folder)
browse_button.pack(pady=10)

entry = tk.Entry(root, textvariable=folder_path, width=50)
entry.pack(pady=5)

run_button = tk.Button(root, text="Run", state="disabled", command=run_script)
run_button.pack(pady=10)

root.mainloop()
