# Import necessary modules
from tkinter import Label, Button, Listbox, Entry, Tk
import os
import tkinter as tk
from tkinter import filedialog, messagebox

# Define the class for the file renaming tool
class FileRenamingTool:
    def __init__(self, master):
        # Initialize the class
        self.master = master
        self.master.title("File Renaming Tool")  # Set the title of the window
        self.master.configure(bg="#4F228A")  # Set the background color of the window

        self.file_list = []  # Initialize a list to store file paths
        self.rename_format = tk.StringVar(value="")  # Initialize a StringVar to store rename format
        self.new_extension = tk.StringVar(value="")  # Initialize a StringVar to store new extension

        # Create GUI widgets
        self.create_widgets()

    def create_widgets(self):
        # Browse button
        browse_button = Button(self.master,
                               text="Browse File",
                               width=20, height=1,
                               command=self.browse_files)  # Command to call browse_files function
        browse_button.pack(pady=15)  # Pack the browse button

        # Set color of browse_button with hex code
        browse_button.configure(bg="#FFA07A")

        # Listbox to display selected files
        self.file_listbox = Listbox(self.master, width=50, height=10)  # Create a Listbox widget
        self.file_listbox.pack(pady=5)  # Pack the Listbox

        # Set Listbox color with hex code
        self.file_listbox.configure(bg="#62E8CF")

        # Entry widget for rename format
        rename_label = Label(self.master, width=15, height=1, text="Rename Format:")  # Create a Label widget
        rename_label.pack()  # Pack the Label

        rename_entry = Entry(self.master, textvariable=self.rename_format)  # Create an Entry widget
        rename_entry.pack(pady=10)  # Pack the Entry

        # Entry widget for new extension
        extension_label = Label(self.master, width=15, height=1, text="New Extension:")  # Create a Label widget
        extension_label.pack()  # Pack the Label

        extension_entry = Entry(self.master, textvariable=self.new_extension)  # Create an Entry widget
        extension_entry.pack(pady=10)  # Pack the Entry

        # Rename button
        rename_button = Button(self.master,
                               text="Done",
                               width=20, height=1,
                               command=self.rename_files)  # Command to call rename_files function
        rename_button.pack(ipady=10)  # Pack the Rename button

        rename_button.configure(bg="#62E8CF")  # Set the background color of the Rename button
        rename_button.configure(borderwidth=5)  # Set the border width of the Rename button

    def browse_files(self):
        # Open file dialog to select files
        file_paths = filedialog.askopenfilenames()
        if file_paths:
            self.file_list = file_paths
            self.update_file_listbox()  # Update the Listbox with selected files

    def update_file_listbox(self):
        # Clear and update the Listbox with selected files
        self.file_listbox.delete(0, tk.END)
        for file_path in self.file_list:
            self.file_listbox.insert(tk.END, os.path.basename(file_path))

    def rename_files(self):
        if not self.file_list:
            # Display error message if no files are selected
            messagebox.showerror("Error", "No files selected.")
            return

        if not self.rename_format.get():
            # Display error message if no rename format is entered
            messagebox.showerror("Error", "Please enter a rename format.")
            return

        for index, old_file_path in enumerate(self.file_list):
            # Iterate through selected files
            file_dir = os.path.dirname(old_file_path)  # Get directory of the file
            file_name, file_extension = os.path.splitext(os.path.basename(old_file_path))  # Get file name and extension
            new_file_name = self.rename_format.get() + self.new_extension.get()  # Construct new file name
            new_file_path = os.path.join(file_dir, new_file_name)  # Construct new file path
            if os.path.exists(new_file_path):
                # If file with the same name exists, add index to the name
                new_file_name = f"{self.rename_format.get()}_{index+1}{self.new_extension.get()}"
                new_file_path = os.path.join(file_dir, new_file_name)
            try:
                # Rename the file
                os.rename(old_file_path, new_file_path)
            except Exception as e:
                # Display error message if renaming fails
                messagebox.showerror(
                    "Error",
                    f"Failed to rename {os.path.basename(old_file_path)}: {str(e)}")

        messagebox.showinfo("Success", "Files renamed successfully.")  # Display success message

def main():
    root = Tk()  # Create Tkinter window
    root.minsize(200, 400)  # Set the minimum size of the window

    label = Label(text='This is My First Python Project ')  # Create a Label widget
    label.pack()  # Pack the Label

    app = FileRenamingTool(root)  # Create an instance of the FileRenamingTool class
    root.mainloop()  # Run the main event loop

if __name__ == "__main__":
    main()  # Call the main function
