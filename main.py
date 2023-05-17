import random
import string
from tkinter import *


passgenerator = Tk()
passgenerator.title("XXSO Password Generator")
passgenerator.config(width=320, height=300, background="black")

def generate_password():
    if password_lenght.get():
        randstr = ""
        integer = "1234567890"
        extrasigns = get_special_chars.get()
        psw = int(password_lenght.get())
        source = string.ascii_letters
        if var1.get() == 1:
            source = source + integer
        if var2.get() == 1:
            source = source + extrasigns
        for i in range(psw):
            randstr += random.choice(source)

        show_password = Entry(generated_password_frame, font=("HELVETICA", 14), background="black",
                              foreground="white")
        show_password.insert(0, randstr)
        show_password.place(x=5, y=0)

        def copy_password():
            passgenerator.clipboard_clear()
            passgenerator.clipboard_append(randstr)
            passgenerator.update()  # the text will stay there after the window is closed

        show_password_copy = Button(generated_password_frame, text="COPY", font=("HELVETICA", 10),
                                    background="black", foreground="white", width=5, command=copy_password)
        show_password_copy.place(x=240, y=0)
label1 = Label(passgenerator, text="Stephen Scharmweber", highlightthickness=0, bd=0, background="black", fg="white", font=("HELVETICA", 20))
label1.grid(row=0, column=0,columnspan=2, padx=5, pady=5)

var1 = IntVar()
password_lenght_label = Label(passgenerator, text="PASSWORD LENGTHS", font=("HELVETICA", 12), background="black",
                              foreground="white")
password_lenght_label.grid(row=1, column=0, padx=5, pady=5)
password_lenght = Entry(passgenerator, font=("HELVETICA", 12), background="black", foreground="white", width=5)
password_lenght.grid(row=1, column=1, padx=5, pady=5)

numbers_check = Checkbutton(passgenerator, text="Numbers", variable=var1, onvalue=1, offvalue=0, font=("HELVETICA", 10),
                            background="black", foreground="white", selectcolor="black")
numbers_check.grid(row=2, column=0, padx=5, pady=5)
var2 = IntVar()
sonderzeichen_check = Checkbutton(passgenerator, text="Special Characters", variable=var2, onvalue=1, offvalue=0,
                                  font=("HELVETICA", 10), background="black", foreground="white",
                                  selectcolor="black")
sonderzeichen_check.grid(row=3, column=0, padx=5, pady=5)
get_special_chars = Entry(passgenerator, font=("HELVETICA", 12), background="black", foreground="white", width=16,
                          insertbackground="white")
get_special_chars.insert(END, r'!§$%&/=?+*#><-_(){}')
get_special_chars.grid(row=3, column=1)
generate = Button(passgenerator, text="Generate Password", command=generate_password, font=("HELVETICA", 18),
                  background="black", foreground="white", width=20)
generate.grid(row=4, column=0,columnspan=2, padx=5, pady=5)




generated_password_frame = LabelFrame(passgenerator, text="Generated password", background="black", foreground="white",
                                      width=290, height=50)
generated_password_frame.grid(row=5, column=0,columnspan=2, padx=5, pady=5)

passgenerator.mainloop()