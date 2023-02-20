from tkinter import PhotoImage

import customtkinter as ctk
import functions
import keyboard
displayfont = "EthnocentricRg-Regular"
typefont = 'Lato Regular'
users = ['User', 'Other User']
rounds = ['','A','B','C','D']

ctk.set_appearance_mode('System')
ctk.set_default_color_theme('dark-blue')




root = ctk.CTk()
frame = ctk.CTkFrame(master=root)
root.geometry('800x800')
root.title("EzInventory")
frame.pack(pady=20, padx=100, fill='both', expand=True)
icon = PhotoImage(file='EzInventory.png')
root.iconphoto(False, icon)
spacerlabel = ctk.CTkLabel(frame, text="")

titlelabel = ctk.CTkLabel(frame, text='EzInventory', font=(displayfont, 40), text_color='deep sky blue').pack(pady=20)


userselectlabel = ctk.CTkLabel(frame, text='User:', font=(typefont, 15)).pack()
userselect = ctk.CTkOptionMenu(frame, values=users, font=(typefont, 20), width=100).pack(pady=10)

roundselectlabel = ctk.CTkLabel(frame, text='Round:', font=(typefont, 15)).pack()
roundselect = ctk.CTkOptionMenu(frame, values=rounds, font=(typefont, 20), width=100).pack()

spacerlabel.pack()

binumlabel = ctk.CTkLabel(frame, text='Bin Number:', font=(typefont, 20)).pack(pady=0)

binum = ctk.CTkEntry(master=frame, placeholder_text='Bin Number', width=300, font=(typefont, 20))
binum.pack(pady=10)




itemnum = ctk.CTkEntry(master=frame, placeholder_text='Item Number', width=300, font=(typefont, 20))
itemnum.pack(pady=10)


lotnum = ctk.CTkEntry(master=frame, placeholder_text='Lot Number', width=300, font=(typefont, 20))
lotnum.pack(pady=10)


qty = ctk.CTkEntry(master=frame, placeholder_text='Quantity Number', width=300, font=(typefont, 20))
qty.pack(pady=10)

submitime = ctk.CTkLabel(frame, text=functions.submission_time(), font=(typefont, 20))

def official_submit():
    submitime.pack()
    functions.item_save()

submitbutton = ctk.CTkButton(frame, text='Submit', font=(displayfont,30), command=official_submit).pack(pady=10)

lotcompletebutton = ctk.CTkButton(frame, text='Lot Complete', font=(displayfont,30)).pack(pady=10)








def bin_enter(event):
    itemnum.focus_set()
    itemnum.delete(0, ctk.END)
    lotnum.delete(0, ctk.END)
    qty.delete(0, ctk.END)
def item_enter(event):
    lotnum.focus_set()
    lotnum.delete(0, ctk.END)
    qty.delete(0, ctk.END)
def lot_enter(event):
    qty.focus_set()
    qty.delete(0, ctk.END)
def qty_enter(event):
    official_submit()
    itemnum.focus_set()
    itemnum.delete(0, ctk.END)
    lotnum.delete(0, ctk.END)
    qty.delete(0, ctk.END)

binum.bind('<Return>', bin_enter)
itemnum.bind('<Return>', item_enter)
lotnum.bind('<Return>', lot_enter)
qty.bind('<Return>', qty_enter)

if __name__ == '__main__':
    root.mainloop()
