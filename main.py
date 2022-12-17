from tkinter import PhotoImage

import customtkinter as ctk
import functions
import keyboard



font = 'Lato Regular'
users = ['Select a user...', 'Geris', 'Henry', 'Zoe', 'Jonida','VERY LONG SENTENCE VERY LONG SENTENCE VERY LONG SENTENCE VERY LONG SENTENCE ']

ctk.set_appearance_mode('System')
ctk.set_default_color_theme('blue')

root = ctk.CTk()
frame = ctk.CTkFrame(master=root)
root.geometry('800x800')
root.title("EzInventory")
frame.pack(pady=20, padx=100, fill='both', expand=True)
icon = PhotoImage(file = 'EzInventory.png')
root.iconphoto(False, icon)

userselect = ctk.CTkOptionMenu(frame, values=users, font=(font, 20), width=100, )
userselect.configure(width=100)
userselect.pack(pady=50)
binumlabel = ctk.CTkLabel(frame, text='Bin Number', font=(font,30)).pack()
binum = ctk.CTkEntry(master=frame, placeholder_text='Bin Number', width=300, font=(font, 20))
binum.pack(pady=50)

itemnum = ctk.CTkEntry(master=frame, placeholder_text='Item Number', width=300, font=(font, 20))
itemnum.pack(pady=10)

lotnum = ctk.CTkEntry(master=frame, placeholder_text='Lot Number', width=300, font=(font, 20))
lotnum.pack(pady=10)

qty = ctk.CTkEntry(master=frame, placeholder_text='Quantity Number', width=300, font=(font, 20))
qty.pack(pady=10)


if __name__ == '__main__':
    root.mainloop()
