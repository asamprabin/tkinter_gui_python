# GUI with Tkinter

import tkinter as tk
import conf

# initialising Tkinter
window = tk.Tk()
window_height = window.winfo_screenheight()
window_width = window.winfo_screenwidth()
# Assigning window full width
window.geometry(f"{window_width}x{window_height}")
window.title(conf.title)

# Main Frame
main_frame = tk.Frame(window, bg=conf.main_frame_color)
# Menu Frame
menu_frame = tk.Frame(window, bg=conf.menu_frame_color)

# First Menu Button
menu_button = tk.Menubutton(menu_frame, text="firstMenuButton", padx=conf.button_padding_x, pady=conf.button_padding_y)
# menu for menu button
menu_button.menu = tk.Menu(menu_button)
menu_button["menu"] = menu_button.menu
menu_button.menu.add_checkbutton(label="menu 1")
menu_button.menu.add_checkbutton(label="menu 2")

# Name Label
name_label = tk.Label(main_frame, text="Enter Your Name :")
name_entry = tk.Entry(main_frame)
# Lambda in command to monitor click event continuously
finish_button = tk.Button(main_frame, text="Finish", padx=conf.button_padding_x,
                          pady=conf.button_padding_y, command=lambda: display_name())


# Defining initial places for widgets
def initial_load():
    main_frame.place(relheight=0.9, relwidth=1.0, rely=0.1)
    menu_frame.place(relheight=0.1, relwidth=1.0)
    menu_button.place(height=conf.button_height, width=conf.button_width, relx=0.01, rely=0.3)
    name_label.place(relx=0.3, rely=0.2)
    name_entry.place(relx=0.4, rely=0.2)
    finish_button.place(height=conf.button_height, width=conf.button_width, relx=0.35, rely=0.4)


def display_name():
    name = name_entry.get()
    name_entry.place_forget()
    finish_button.place_forget()

    name_label['text'] = name


initial_load()


window.mainloop()
