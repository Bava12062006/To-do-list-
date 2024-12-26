import tkinter as tk
from tkinter import messagebox

# List to store tasks
tasks = []

def add_task():
    task = task_entry.get()
    if task.strip():
        tasks.append(task)
        update_task_list()
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Task cannot be empty!")

def update_task():
    try:
        selected_index = task_listbox.curselection()[0]
        selected_task = tasks[selected_index]

        # Open a new window for editing
        edit_window = tk.Toplevel(root)
        edit_window.title("Edit Task")
        tk.Label(edit_window, text="Edit your task:").pack(pady=5)
        edit_entry = tk.Entry(edit_window, width=40)
        edit_entry.pack(pady=5)
        edit_entry.insert(0, selected_task)

        def save_edit():
            updated_task = edit_entry.get()
            if updated_task.strip():
                tasks[selected_index] = updated_task
                update_task_list()
                edit_window.destroy()
            else:
                messagebox.showwarning("Warning", "Task cannot be empty!")

        save_button = tk.Button(edit_window, text="Save", command=save_edit)
        save_button.pack(pady=5)

    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to update!")

def delete_task():
    try:
        selected_index = task_listbox.curselection()[0]
        tasks.pop(selected_index)
        update_task_list()
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to delete!")

def update_task_list():
    task_listbox.delete(0, tk.END)
    for task in tasks:
        task_listbox.insert(tk.END, task)
root = tk.Tk()
root.title("To-Do List")
task_entry = tk.Entry(root, width=40)
task_entry.grid(row=0, column=0, padx=10, pady=10)
add_button = tk.Button(root, text="Add Task", command=add_task)
add_button.grid(row=0, column=1, padx=10, pady=10)
task_listbox = tk.Listbox(root, width=50, height=15)
task_listbox.grid(row=1, column=0, columnspan=2, padx=10, pady=10)
update_button = tk.Button(root, text="Update Task", command=update_task)
update_button.grid(row=2, column=0, padx=10, pady=5, sticky="w")
delete_button = tk.Button(root, text="Delete Task", command=delete_task)
delete_button.grid(row=2, column=1, padx=10, pady=5, sticky="e")
root.mainloop()
