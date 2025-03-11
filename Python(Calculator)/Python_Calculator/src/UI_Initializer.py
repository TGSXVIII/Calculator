import tkinter as tk
from UI_Layout import create_ui  # Import the UI creation function
from tkinter import PhotoImage  # For loading images

# Create the main window
root = tk.Tk()
root.title("Python Calculator")
root.geometry("326x500")  # Set window size to resemble a PC calculator

# Load the Python logo image
python_logo = PhotoImage(file="resources/icons/python_logo.png")  # Use the path to your image file

# Set the window icon to the Python logo
root.iconphoto(False, python_logo)

# Call the function from UI_Layout.py to create the UI
entry_var = create_ui(root)  # Only get entry_var, not root

# Start the application
root.mainloop()