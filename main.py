import customtkinter as ctk

ctk.set_appearance_mode('System')
ctk.set_default_color_theme('blue')

root = ctk.CTk()

root.geometry('800x800')
root.title("EzInventory")


if __name__ == '__main__':
    root.mainloop()
