from tkinter import Tk
from tkinter import Menu
from tkinter import messagebox
from tkinter import ttk
from tkinter import StringVar
from tkinter import Button

class Banner:
    
    def __init__(self, master):
        # MENU BAR SECTION
        # Remove dashes from the menubar drop down
        master.option_add('*tearOff', False)
        self.menubar = Menu(master)
        master.config(menu=self.menubar)
        
        file = Menu(self.menubar)

        file.add_command(label='Test', command=lambda: messagebox.showinfo(title='Test', message='This is a test.'))

        self.menubar.add_cascade(menu=file, label='File')

        # BANNER IMAGE SECTION
        # Create widgets
        self.banner_frame = ttk.Frame(master, height=180, width=480, relief='solid')
        self.banner_img_label = ttk.Label(self.banner_frame)

        # Configure widgets
        self.banner_frame.pack_propagate(False)

        # Place widgets
        self.banner_frame.pack()

class ChecklistItem:

    def __init__(self, master, task):
        self.task = task
        # Allows the Checkbutton value to be dynamic
        self.value = StringVar()
        self.item = ttk.Checkbutton(master, text=self.task)
        self.item.config(variable=self.value, onvalue="Complete", offvalue="Imcomplete")

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
        self.add_button = Button(self.button_frame, text="Add Task")

        # Configure widgets
        self.checklist_frame.pack_propagate(False)
        self.button_frame.pack_propagate(False)

        # Place widgets
        self.add_button.pack(pady=15)
        self.checklist_frame.pack()
        self.button_frame.pack()

class App:
    
    def __init__(self, master):
        self.banner = Banner(master)
        self.content = Content(master)

def main():
    root = Tk()
    app = App(root)
    root.mainloop()

if __name__ == '__main__':
    main()