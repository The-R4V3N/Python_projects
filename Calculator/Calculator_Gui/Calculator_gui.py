
'''
 * @file Calculator_gui.py
 * @author Oliver Joisten (https://oliver-joisten.se/)
 * @brief A simple Calculator with a very basic gui made with custom tkinter and python's standard library.
 * @version 0.1
 * @date 2023-01-12
 *
 * @copyright Copyright (c) 2023
 *
'''
from tkinter import *
import customtkinter
import tkinter.messagebox

# Modes: system (default), light, dark
customtkinter.set_appearance_mode("System")
# Themes: blue (default), dark-blue, green
customtkinter.set_default_color_theme("green")

root = customtkinter.CTk()
root.geometry("340x300")
root.resizable(0, 0)
calc = Frame(root)
root.title("Calculator")

# Define functions and widget events:


def btn_click(item):
    global expression
    expression = expression + str(item)
    input_text.set(expression)


def btn_clear():
    global expression
    expression = ""
    input_text.set("")


def btn_equal():
    global expression
    result = str(eval(expression))
    input_text.set(result)
    expression = ""


def iExit():
    iExit = tkinter.messagebox.askyesno("Calculator",
                                        "Do you want to exit ?")
    if iExit > 0:
        root.destroy()
        return


def Dark():
    customtkinter.set_appearance_mode("Dark")


def Light():
    customtkinter.set_appearance_mode("Light")


# def cut_text():
#     try:
#         # Get the selected text from the input field
#         selected_text = input_field.get(SEL_FIRST, SEL_LAST)
#         # Clear the selected text from the input field
#         input_field.delete(SEL_FIRST, SEL_LAST)
#         # Place the selected text in the clipboard
#         root.clipboard_clear()
#         root.clipboard_append(selected_text)
#     except:
#         pass


# def copy_text():
#     try:
#         # Get the selected text from the input field
#         selected_text = input_field.get(SEL_FIRST, SEL_LAST)
#         # Place the selected text in the clipboard
#         root.clipboard_clear()
#         root.clipboard_append(selected_text)
#     except:
#         pass


# def paste_text():
#     try:
#         # Get the text from the clipboard
#         clipboard_text = root.clipboard_get()
#         # Insert the text from the clipboard into the input field
#         input_field.insert(INSERT, clipboard_text)
#     except:
#         pass


# Create labels, text boxes, and button:
expression = ""
input_text = StringVar()

input_frame = customtkinter.CTkFrame(
    root, width=360, height=50)
input_frame.pack(side=TOP)

input_field = customtkinter.CTkEntry(input_frame, font=('arial', 18, 'bold'),
                                     textvariable=input_text, width=327, height=40, justify=RIGHT)
input_field.grid(row=0, column=0)
input_field.pack(padx=2, pady=10)


btns_frame = customtkinter.CTkFrame(root, width=350, height=272.5)
btns_frame.pack()

# First Row
clear = customtkinter.CTkButton(btns_frame, text="Clear", width=245, height=40, border_width=1, corner_radius=5,
                                cursor="hand2", command=lambda: btn_clear()).grid(row=0, column=0, columnspan=3, padx=1, pady=2)
divide = customtkinter.CTkButton(btns_frame, text="/", width=77, height=40, border_width=1, corner_radius=5,
                                 cursor="hand2", command=lambda: btn_click("/")).grid(row=0, column=3, padx=1, pady=2)

# Second Row
seven = customtkinter.CTkButton(btns_frame, text="7", width=77, height=40, fg_color="black", hover_color="gray",  border_width=1, corner_radius=5,
                                cursor="hand2", command=lambda: btn_click(7)).grid(row=1, column=0, padx=1, pady=2)
eight = customtkinter.CTkButton(btns_frame, text="8", width=77, height=40, fg_color="black", hover_color="gray", border_width=1, corner_radius=5,
                                cursor="hand2", command=lambda: btn_click(8)).grid(row=1, column=1, padx=1, pady=2)
nine = customtkinter.CTkButton(btns_frame, text="9", width=77, height=40, fg_color="black", hover_color="gray", border_width=1, corner_radius=5,
                               cursor="hand2", command=lambda: btn_click(9)).grid(row=1, column=2, padx=1, pady=2)
multiply = customtkinter.CTkButton(btns_frame, text="*", width=77, height=40, border_width=1, corner_radius=5,
                                   cursor="hand2", command=lambda: btn_click("*")).grid(row=1, column=3, padx=1, pady=2)

# Third Row
four = customtkinter.CTkButton(btns_frame, text="4", width=77, height=40, fg_color="black", hover_color="gray", border_width=1, corner_radius=5,
                               cursor="hand2", command=lambda: btn_click(4)).grid(row=2, column=0, padx=1, pady=2)
five = customtkinter.CTkButton(btns_frame, text="5", width=77, height=40, fg_color="black", hover_color="gray", border_width=1, corner_radius=5,
                               cursor="hand2", command=lambda: btn_click(5)).grid(row=2, column=1, padx=1, pady=2)
six = customtkinter.CTkButton(btns_frame, text="6", width=77, height=40, fg_color="black", hover_color="gray", border_width=1, corner_radius=5,
                              cursor="hand2", command=lambda: btn_click(6)).grid(row=2, column=2, padx=1, pady=2)
minus = customtkinter.CTkButton(btns_frame, text="-", width=77, height=40, border_width=1, corner_radius=5,
                                cursor="hand2", command=lambda: btn_click("-")).grid(row=2, column=3, padx=1, pady=2)

# Fourth Row
one = customtkinter.CTkButton(btns_frame, text="1", width=77, height=40, fg_color="black", hover_color="gray", border_width=1, corner_radius=5,
                              cursor="hand2", command=lambda: btn_click(1)).grid(row=3, column=0, padx=1, pady=2)
two = customtkinter.CTkButton(btns_frame, text="2", width=77, height=40, fg_color="black", hover_color="gray", border_width=1, corner_radius=5,
                              cursor="hand2", command=lambda: btn_click(2)).grid(row=3, column=1, padx=1, pady=2)
three = customtkinter.CTkButton(btns_frame, text="3", width=77, height=40, fg_color="black", hover_color="gray", border_width=1, corner_radius=5,
                                cursor="hand2", command=lambda: btn_click(3)).grid(row=3, column=2, padx=1, pady=2)
plus = customtkinter.CTkButton(btns_frame, text="+", width=77, height=40, border_width=1, corner_radius=5,
                               cursor="hand2", command=lambda: btn_click("+")).grid(row=3, column=3, padx=1, pady=2)

# Fifth Row
zero = customtkinter.CTkButton(btns_frame, text="0", width=158, height=40, fg_color="black", hover_color="gray", border_width=1, corner_radius=5, cursor="hand2",
                               command=lambda: btn_click(0)).grid(row=4, column=0, columnspan=2, padx=1, pady=2)
point = customtkinter.CTkButton(btns_frame, text=".", width=77, height=40, border_width=1, corner_radius=5,
                                cursor="hand2", command=lambda: btn_click(".")).grid(row=4, column=2, padx=1, pady=2)
equals = customtkinter.CTkButton(btns_frame, text="=", width=77, height=40, fg_color="black", hover_color="gray", border_width=1, corner_radius=5,
                                 cursor="hand2", command=lambda: btn_equal()).grid(row=4, column=3, padx=1, pady=2)

# Adding Menu and Settings

menubar = Menu(calc)

# MenuBar 1 :
filemenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label='Settings', menu=filemenu)
filemenu.add_command(label="BG-Color Light", command=Light)
filemenu.add_command(label="BG-Color Dark", command=Dark)

filemenu.add_separator()
filemenu.add_command(label="Exit", command=iExit)

# # MenuBar 2 :
# editmenu = Menu(menubar, tearoff=0)
# menubar.add_cascade(label='Edit', menu=editmenu)
# editmenu.add_command(label="Cut", command=cut_text)
# editmenu.add_command(label="Copy", command=copy_text)

# editmenu.add_separator()
# editmenu.add_command(label="Paste", command=paste_text)


root.config(menu=menubar)


root.mainloop()
