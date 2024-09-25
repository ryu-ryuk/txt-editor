import tkinter as tk
from tkinter import filedialog, Menu, messagebox

class TextEditor:
    def __init__(self, root):
        # Initialize the main window
        self.root = root
        self.root.title("Enhanced Text Editor")  # Set the title of the window
        self.root.geometry("600x400")  # Set the size of the window

        # Create a text area for user input
        self.text_area = tk.Text(self.root, undo=True)  # Enable undo functionality
        self.text_area.pack(expand=True, fill='both')  # Pack it to fill the window

        # Create a menu bar
        self.menu = Menu(self.root)  # Create a Menu widget
        self.root.config(menu=self.menu)  # Configure the root window to use this menu

        # Create the File menu
        self.file_menu = Menu(self.menu)  # Create a submenu for File
        self.menu.add_cascade(label='File', menu=self.file_menu)  # Add it to the menu bar
        self.file_menu.add_command(label='Open', command=self.open_file, accelerator='Ctrl+O')  # Add Open option
        self.file_menu.add_command(label='Save', command=self.save_file, accelerator='Ctrl+S')  # Add Save option
        self.file_menu.add_separator()  # Add a separator line
        self.file_menu.add_command(label='Exit', command=root.quit)  # Add Exit option

        # Create the Edit menu
        self.edit_menu = Menu(self.menu)  # Create a submenu for Edit
        self.menu.add_cascade(label='Edit', menu=self.edit_menu)  # Add it to the menu bar
        self.edit_menu.add_command(label='Undo', command=self.text_area.edit_undo, accelerator='Ctrl+Z')  # Add Undo option
        self.edit_menu.add_command(label='Redo', command=self.text_area.edit_redo, accelerator='Ctrl+Y')  # Add Redo option

        # Bind keyboard shortcuts
        self.root.bind('<Control-o>', lambda event: self.open_file())  # Bind Ctrl+O to open_file
        self.root.bind('<Control-s>', lambda event: self.save_file())  # Bind Ctrl+S to save_file
        self.root.bind('<Control-z>', lambda event: self.text_area.edit_undo())  # Bind Ctrl+Z to undo
        self.root.bind('<Control-y>', lambda event: self.text_area.edit_redo())  # Bind Ctrl+Y to redo

        # Create a status bar to display word count
        self.status_bar = tk.Label(self.root, text="Word Count: 0", anchor='w')  # Create a Label for status bar
        self.status_bar.pack(side='bottom', fill='x')  # Pack it to the bottom
        self.text_area.bind('<KeyRelease>', self.update_word_count)  # Update word count on key release

    def open_file(self):
        # Function to open a file and read its contents
        file_path = filedialog.askopenfilename()  # Open a file dialog to select a file
        if file_path:  # Check if a file was selected
            try:
                with open(file_path, 'r') as file:  # Open the file in read mode
                    content = file.read()  # Read the file's contents
                    self.text_area.delete(1.0, tk.END)  # Clear the text area
                    self.text_area.insert(tk.END, content)  # Insert the file's contents into the text area
            except Exception as e:
                messagebox.showerror("Error", f"Failed to open file: {e}")  # Show error if file can't be opened

    def save_file(self):
        # Function to save the current contents of the text area to a file
        file_path = filedialog.asksaveasfilename(defaultextension=".txt")  # Open a save dialog
        if file_path:  # Check if a file path was provided
            try:
                with open(file_path, 'w') as file:  # Open the file in write mode
                    content = self.text_area.get(1.0, tk.END)  # Get the text area content
                    file.write(content)  # Write the content to the file
            except Exception as e:
                messagebox.showerror("Error", f"Failed to save file: {e}")  # Show error if file can't be saved

    def update_word_count(self, event):
        # Function to update the word count in the status bar
        content = self.text_area.get(1.0, tk.END)  # Get the content of the text area
        word_count = len(content.split())  # Count the words
        self.status_bar.config(text=f"Word Count: {word_count}")  # Update the status bar

if __name__ == "__main__":
    root = tk.Tk()  # Create the main application window
    editor = TextEditor(root)  # Instantiate the TextEditor class
    root.mainloop()  # Start the Tkinter event loop
