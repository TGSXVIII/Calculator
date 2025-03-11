import tkinter as tk
from calculations_Processor import calculate  # Import the function from calculations_Processor.py

# Helper Functions
def on_click(button_text, entry_var):
    if button_text == "=":
        result = calculate(entry_var.get())  # Calls function from calculations_Processor.py
        entry_var.set(result)
    elif button_text == "C":
        entry_var.set("")  # Clears the entry
    elif button_text == "<-":
        current_text = entry_var.get()
        entry_var.set(current_text[:-1])  # Removes the last character
    else:
        entry_var.set(entry_var.get() + button_text)  # Appends the clicked button text

#===========================================

def toggle_menu(menu_frame):
    """Toggle the visibility of the menu."""
    if menu_frame.winfo_ismapped():
        menu_frame.grid_forget()  # Hide the menu
    else:
        menu_frame.grid(row=0, column=0, sticky="nsew", padx=3, pady=3)  # Show the menu

def toggle_scientific(advanced_frame):
    if advanced_frame.winfo_ismapped():
        advanced_frame.grid_forget()  # Hide it
    else:
        advanced_frame.grid(row=7, column=0, columnspan=4, sticky="nsew", padx=5, pady=5)

#===========================================

def create_menu(root, advanced_frame):
    """Create a sliding left-side menu"""

    # Sidebar menu frame (hidden by default)
    menu_frame = tk.Frame(root, bg="lightgray", width=150, height=500)

    # ☰ Button (Now in row 0, above the entry widget)
    menu_button = tk.Button(root, text="☰", font=("Arial", 14), command=lambda: toggle_menu(menu_frame))
    menu_button.grid(row=0, column=0, sticky="w", padx=5, pady=5)

    # Menu buttons inside menu_frame (appear below ☰)
    btn_standard = tk.Button(menu_frame, text="Standard", font=("Arial", 12), command=lambda: advanced_frame.grid_forget())
    btn_scientific = tk.Button(menu_frame, text="Scientific", font=("Arial", 12), command=lambda: toggle_scientific(advanced_frame))
    btn_exit = tk.Button(menu_frame, text="Exit", font=("Arial", 12), command=root.quit)

    # Pack buttons inside the menu frame
    btn_standard.pack(fill="x", padx=5, pady=5)
    btn_scientific.pack(fill="x", padx=5, pady=5)
    btn_exit.pack(fill="x", padx=5, pady=5)

    return menu_frame, menu_button

def create_entry_widget(root):
    entry_var = tk.StringVar()
    entry = tk.Entry(root, textvariable=entry_var, font=("Arial", 12), justify="right", bd=5, relief="sunken")
    entry.grid(row=1, column=0, columnspan=4, ipadx=5, ipady=26, sticky="ew")  # Move entry to row 1
    return entry_var, entry

def create_memory_buttons(root, entry_var):
    memory_buttons = [
        ("MC", "MR", "M+", "M-", "MS", "Mv")
    ]

    memory_frame = tk.Frame(root)
    memory_frame.grid(row=2, column=0, columnspan=4, padx=5, pady=1, sticky="nsew")  # Shifted to row 2

    for r, row in enumerate(memory_buttons, start=0):
        for c, text in enumerate(row):
            btn = tk.Button(memory_frame, text=text, font=("Arial", 10), height=2, width=6,
                            command=lambda t=text: on_click(t, entry_var))
            btn.grid(row=r, column=c, padx=1, pady=1, sticky="nsew")

    for i in range(6):
        memory_frame.grid_columnconfigure(i, weight=1)

def create_main_buttons(root, entry_var):
    buttons = [
        ("%", "CE", "C", "<="),
        ("1/x", "x^2", "2√x", "/"),
        ("7", "8", "9", "x"),
        ("4", "5", "6", "-"),
        ("1", "2", "3", "+"),
        ("+/-", "0", ",", "="),
    ]

    main_button_frame = tk.Frame(root)
    main_button_frame.grid(row=3, column=0, columnspan=4, padx=5, pady=1, sticky="nsew")  # Shifted to row 3

    for r, row in enumerate(buttons, start=0):
        for c, text in enumerate(row):
            btn = tk.Button(main_button_frame, text=text, font=("Arial", 12), height=2,
                            command=lambda t=text: on_click(t, entry_var))
            btn.grid(row=r, column=c, padx=1, pady=1, sticky="nsew")

    for i in range(4):
        main_button_frame.grid_columnconfigure(i, weight=1)

def create_trigonomatri_section(root, entry_var):
    trigonometry_frame = tk.Frame(root)
    trigonometry_buttons = [
        ("2nd", "sin", "cos", "tan"),
        ("hyp", "sec", "csc", "cot")
    ]
    for r, row in enumerate(trigonometry_buttons, start=2):  # Shifted to row 2
        for c, text in enumerate(row):
            btn = tk.Button(trigonometry_frame, text=text, font=("Arial", 12), height=2, width=4,
                            command=lambda t=text: on_click(t, entry_var))
            btn.grid(row=r, column=c, padx=3, pady=3, sticky="nsew")

    return trigonometry_frame

def create_function_section(root, entry_var):
    trigonometry_frame = tk.Frame(root)
    trigonometry_buttons = [
        ("|x|", "??", "??"),
        ("rand", "->dms", "->deg")
    ]
    for r, row in enumerate(trigonometry_buttons, start=2):  # Shifted to row 2
        for c, text in enumerate(row):
            btn = tk.Button(trigonometry_frame, text=text, font=("Arial", 12), height=2, width=4,
                            command=lambda t=text: on_click(t, entry_var))
            btn.grid(row=r, column=c, padx=3, pady=3, sticky="nsew")

    return trigonometry_frame

def create_scientific_section(root, entry_var):
    advanced_frame = tk.Frame(root)
    advanced_buttons = [
        ("2nd", "pi", "e", "C", "<="),
        ("x^2", "1/x", "|x|", "exp", "mod"),
        ("2√x", "(", ")", "n!", "/"),
        ("x^y","7","8","9","x"),
        ("10^x","4","5","6","-",),
        ("log","1","2","3","+"),
        ("in", "+/-", "0", ",", "=")
    ]
    for r, row in enumerate(advanced_buttons, start=2):  # Shifted to row 2
        for c, text in enumerate(row):
            btn = tk.Button(advanced_frame, text=text, font=("Arial", 12), height=2, width=4,
                            command=lambda t=text: on_click(t, entry_var))
            btn.grid(row=r, column=c, padx=3, pady=3, sticky="nsew")

    return advanced_frame

#===========================================

def configure_grid(root):
    for i in range(0, 10):
        root.grid_rowconfigure(i, weight=1)
        root.grid_columnconfigure(i, weight=1)

    for i in range(4):
        root.grid_columnconfigure(i, minsize=80)

def create_ui(root):
    entry_var, entry = create_entry_widget(root)
    create_memory_buttons(root, entry_var)
    create_main_buttons(root, entry_var)

    advanced_frame = create_scientific_section(root, entry_var)
    menu_frame, menu_button = create_menu(root, advanced_frame)  # Add the menu

    configure_grid(root)

    return entry_var, root
