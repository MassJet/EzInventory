import customtkinter as ctk
import functions
font = 'Lato Regular'
users = ['Select a user...','Geris', 'Henry', 'Zoe', 'Jonida', 'VERY LONG SENTENCE VERY LONG SENTENCE VERY LONG SENTENCE VERY LONG SENTENCE ']

ctk.set_appearance_mode('System')
ctk.set_default_color_theme('blue')

root = ctk.CTk()
frame = ctk.CTkFrame(master=root)
root.geometry('800x800')
root.title("EzInventory")
frame.pack(pady=20,padx=100, fill='both', expand=True)

userselect = ctk.CTkOptionMenu(frame, values=users, font=(font, 20), width=100, )
userselect.configure(width=100)
userselect.pack(pady=50)

binum = ctk.CTkEntry(master=frame, placeholder_text='Bin Number', width=300, font=(font, 20))



if __name__ == '__main__':
    root.mainloop()
