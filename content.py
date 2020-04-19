from tkinter import ttk
from tkinter import Button
from tkinter import Toplevel
from tkinter import messagebox
from item import ChecklistItem

class Content:
    
    def __init__(self, master, checklist=None):
        # Constants
        frame_width = 480
        checklist_frame_height = 480
        button_frame_height = checklist_frame_height/8

        # Create widgets
        self.checklist_frame = ttk.Frame(master, height=checklist_frame_height, width=frame_width, relief='solid')
        self.button_frame = ttk.Frame(master, height=button_frame_height, width=frame_width, relief='solid')
        if checklist is None:
            self.checklist = []
        else:
            self.checklist = checklist

        for task in self.checklist:
            task.config(command=self.update_state)

        self.add_button = Button(self.button_frame, text="\u271a Add Task", command=self.add_task)

        # Configure widgets
        self.checklist_frame.pack_propagate(False)
        self.button_frame.pack_propagate(False)

        # Place widgets
        self.add_button.pack(pady=15)
        self.checklist_frame.pack()
        self.button_frame.pack()

    def display_tasks(self):
        for task in self.checklist:
            task.item.pack(anchor='w', pady=5, padx=5)

    def add_task(self):
        # Create widgets
        add_window = Toplevel(self.button_frame, height=120, width=480)
        # Prevent window resizing along x and y
        add_window.resizable(False, False)
        add_frame = ttk.Frame(add_window)
        add_label = ttk.Label(add_frame, text="Task Name: ")
        add_entry = ttk.Entry(add_frame, width=48)
        add_entry.bind('<Return>', lambda e: self.submit(add_entry.get(), add_window))
        submit_button = Button(add_frame, text="Submit", command=lambda: self.submit(add_entry.get(), add_window))
        cancel_button = Button(add_frame, text="Cancel", command=lambda: self.cancel(add_window))

        # Place widgets
        add_label.pack(side='left')
        add_entry.pack(side='left')
        submit_button.pack(side='left')
        cancel_button.pack(side='left')
        add_frame.pack()

    def cancel(self, master):
        master.destroy()

    def submit(self, task, master):
        if task != "":
            new_task = ChecklistItem(self.checklist_frame, task)
            new_task.item.config(command=self.update_state)
            self.checklist.append(new_task)
            self.cancel(master)
            self.display_tasks()
        else:
            messagebox.showerror(title="Invalid entry", message="A task cannot be blank.")

    def update_state(self):
        for task in self.checklist:
            if task.value.get() == "Complete":
                self.checklist.remove(task)
                task.item.destroy()
        self.display_tasks()