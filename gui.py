from tkinter import filedialog
from tkinter import *
from tkinter.tix import COLUMN
from Ncrypt import select_dir

root = Tk()
root.title('Ncrypt')
root.resizable(False,False)
# root.withdraw()
# entry.insert(0,'enter directory')

#font
current_font = ("Arial Bold", 15)

# declare
file_dir = Entry(root,width=70)
key_dir = Entry(root,width=70)

browse_key_button = Button(root,font=current_font, text='Browse key',command=select_dir())
browse_file_button = Button(root,font=current_font, text='Browse directory',command=select_dir())

main_label = Label(root,font=current_font, text='******************* Welcome To Ncrypt *******************\n\n- Browse for your key\n\n- Browse for the directory\n\n- Then encrypt / decrypt\n')

encrypt_button = Button(root,font=current_font, text='Encrypt Directory',height=2, width=4)
decrypt_button = Button(root,font=current_font, text='Decrypt Directory',height=2, width=4)

# grid
file_dir.grid(column=0, row=0, columnspan=2, sticky=(W), padx=10,pady=10)
key_dir.grid(column=0,row=1, columnspan=2, sticky=(W),padx=10,pady=10)

browse_file_button.grid(column=3, row=0, sticky=(E), padx=10,pady=10)
browse_key_button.grid(column=3, row=1, sticky=(E), padx=10,pady=10)

main_label.grid(column=0, row=2, columnspan=4, padx=10,pady=10)

encrypt_button.grid(column=0,columnspan=1 , row=3, sticky=(S,E,W), padx=10,pady=10)
decrypt_button.grid(column=1,columnspan=4 , row=3, sticky=(S,E,W), padx=10,pady=10)

# weights
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)
root.columnconfigure(2, weight=1)
root.columnconfigure(3, weight=1)

root.rowconfigure(0, weight=1)
root.rowconfigure(1, weight=1)
root.rowconfigure(2, weight=3)

root.mainloop()