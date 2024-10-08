import webbrowser
import os
import sys
from tkinter import BooleanVar, Checkbutton, Tk, Frame, Label, Button, Entry
from PIL import Image, ImageTk
from src.person import Person
from src.id_control import IdControl
from config.version import __version__

def start_gui():
    root = Tk()
    root.title("Id Buddy")
    root.geometry("800x600")
    root.resizable(width=False, height=False)
    root.configure(bg="#282c34")

    icon = ImageTk.PhotoImage(file=resource_path("src/img/idbuddy.ico"))
    root.iconphoto(True, icon)

    container = Frame(root)
    container.pack(fill="both", expand=True)

    start_page = Frame(container, bg="#282c34")
    result_page = Frame(container, bg="#282c34")

    for frame in (start_page, result_page):
        frame.place(relwidth=1, relheight=1)

    # Setup start page
    setup_start_page(start_page, result_page)

    show_frame(start_page)

    root.mainloop()

def setup_start_page(start_page: Frame, result_page: Frame):
    img = Image.open(resource_path("src/img/idbuddy_logo.png"))
    resized_img = img.resize((250, 250))
    logo = ImageTk.PhotoImage(resized_img)

    logo_label = Label(start_page, image=logo, bg="#282c34")
    logo_label.image = logo 
    logo_label.pack(pady=20)

    entry_frame = Frame(start_page, bg="#F0B437", bd=1)
    entry_frame.pack(pady=10)

    text_input = Entry(entry_frame, width=20, font=("Helvetica", 16), bg="#2D323B", fg="#B3B4E8", bd=0, 
                       insertbackground="#FFFFFF", selectbackground="#F0B437", selectforeground="#282c34", 
                       highlightthickness=1, highlightbackground="#2D323B", highlightcolor="#F0B437")
    text_input.pack(ipady=5, padx=3, pady=3)

    text_input.focus_set()

    swedish_id_var = BooleanVar(value=True)
    swedish_id_checkbox = Checkbutton(start_page, text="Swedish ID", variable=swedish_id_var, font=("Helvetica", 16), 
                                      bg="#282c34", fg="#F0B437", selectcolor="#282c34", activebackground="#282c34", 
                                      activeforeground="#B3B4E8")
    swedish_id_checkbox.pack(pady=5)
    swedish_id_checkbox.config(highlightbackground="#F0B437", highlightthickness=10)

    error_label = Label(start_page, text="", font=("Helvetica", 15), fg="#F04843", bg="#282c34")
    error_label.pack(pady=5)

    button = Button(start_page, text="Check ID >", command=lambda: on_button_click(text_input, error_label, start_page, result_page, swedish_id_var), 
                    width=20, height=2, bg="#F0B437", fg="#2D323B", font=("Helvetica", 12), cursor="hand2")
    button.pack(pady=20)

    text_input.bind('<Return>', lambda event: on_button_click(text_input, error_label, start_page, result_page, swedish_id_var))
    
    version_label = Label(start_page, text=f"Version {__version__}", font=("Helvetica", 10), fg="#B3B4E8", bg="#282c34")
    version_label.place(relx=1.0, rely=1.0, anchor="se", x=-10, y=-10) 

    small_img = Image.open(resource_path("src/img/2brackets.png"))
    small_resized_img = small_img.resize((40, 40))  
    small_icon = ImageTk.PhotoImage(small_resized_img)
    small_image_label = Label(start_page, image=small_icon, bg="#282c34", cursor="hand2")
    small_image_label.image = small_icon  
    small_image_label.place(relx=0.0, rely=1.0, anchor="sw", x=10, y=-10)
    small_image_label.bind("<Button-1>", lambda e: webbrowser.open_new("https://www.2brackets.com"))


def on_button_click(text_input: Entry, error_label: Label, start_page: Frame, result_page: Frame, swedish_id_var: BooleanVar):
    error_label.config(text="")
    text_value = text_input.get()
    swedish_id = swedish_id_var.get()

    if not text_value:
        error_label.config(text="Please insert a ID number")
    else:
        id_control = IdControl(text_value, swedish_id)
        if not id_control.person_id_valid:
            error_label.config(text=id_control.error_message)
        else:
            person = Person(id_control)
            birthdate = person.get_format_date()
            age = person.get_age()
            gender = person.determine_gender()
            birthday_today = person.is_birthday_today()
            
            show_result_page(start_page, result_page, birthdate, age, gender, birthday_today)
            show_frame(result_page)  

    text_input.delete(0, 'end')


def show_result_page(start_page, result_page, birthdate, age, gender, birthday_today):
    for widget in result_page.winfo_children():
        widget.destroy()

    result_frame = Frame(result_page, bg="#282c34")
    result_frame.pack(expand=True)

    labels = [
        ("BirthDay:", birthdate, "#B3B4E8"),
        ("Age:", age, "#8CF070" if age >= 18 else "#F04843"), 
        ("Gender:", gender, "#B3B4E8"),
        ("Birthday to day:", "Yes, Happy birthday" if birthday_today else "No", "#B3B4E8")
    ]

    for label_text, value, color in labels:
        label = Label(result_frame, text=label_text, font=("Helvetica", 16), fg="orange", bg="#282c34")
        label.pack(anchor="center", pady=5)
        value_label = Label(result_frame, text=value, font=("Helvetica", 16), fg=color, bg="#282c34")
        value_label.pack(anchor="center", pady=5)

    back_button = Button(result_frame, text="< Back", command=lambda: show_frame(start_page), width=20, height=2, bg="#F0B437", fg="#2D323B", font=("Helvetica", 12), cursor="hand2")
    back_button.pack(pady=20)
    back_button.focus_set()
    back_button.bind('<Return>', lambda event: go_back_start_page(start_page))

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except AttributeError:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

def show_frame(frame):
    frame.tkraise()


def go_back_start_page(start_page: Frame):
    for widget in start_page.winfo_children():
        if isinstance(widget, Frame):  
            for child in widget.winfo_children():
                if isinstance(child, Entry):
                    child.delete(0, 'end') 
                    child.focus_set()  
                elif isinstance(child, Label):
                    child.config(text="")  
    show_frame(start_page)