from tkinter import *
from tkinter.filedialog import *
from tkinter.messagebox import *
from tkinter.colorchooser import *

flag_save = False


def fnew():
    global flag_save
    data = text.get(1.0, END)
    if len(data) > 1 and flag_save == False:
        fsave()
    if flag_save:
        text.delete(1.0, END)
    flag_save = False


def fopen():
    global flag_save
    # f = askopenfile()
    f = askopenfilename()
    if f:
        file = open(f)
        data = file.readlines()
        # print(data)
        text.delete(1.0, END)
        text.insert(1.0, data)
        root.title(f)
        flag_save = True
    else:
        print("canclled...")


def fsave():
    global flag_save
    f = asksaveasfilename(defaultextension='.txt',
                          filetypes=[("text file", ".txt"), ("c file", ".c"), ("python file", ".py")])
    print(f)
    if (f):
        file = open(f, "w")
        data = text.get(1.0, END)
        print(data)
        file.write(data)
        flag_save = True
    else:
        print("canclled...")


def fexit():
    # print('bye')
    global flag_save
    if not flag_save:
        a = askyesnocancel(message='do you want to quit', title='msg')
        if a:
            fsave()
            if flag_save:
                root.quit()
        elif not a:
            root.quit()


def normal():
    text.config(font=('arial', 15))


def bold():
    text.config(font=('arial', 15, 'bold'))


def italic():
    text.config(font=('arial', 15, 'italic'))


def underline():
    text.config(font=('arial', 15, 'underline'))


def about():
    t = Toplevel(root)
    l = Label(t, text='Just For Fun')
    l.pack()


def fg_():
    c1, c2 = askcolor()
    text.config(fg=c2)


def bg_():
    c1, c2 = askcolor()
    text.config(bg=c2)


root = Tk()
root.geometry('500x400')

text = Text(root, font=('arial', 15))
text.pack(fill='both', expand=1)

menubar = Menu(root)

filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="new", command=fnew)
filemenu.add_command(label="open", command=fopen)
filemenu.add_command(label="save", command=fsave)
filemenu.add_command(label="exit", command=fexit)
menubar.add_cascade(label="File", menu=filemenu)

editmenu = Menu(menubar, tearoff=0)
editmenu.add_command(label="copy")
editmenu.add_command(label="paste")
menubar.add_cascade(label="Edit", menu=editmenu)

searchmenu = Menu(menubar, tearoff=0)
searchmenu.add_command(label="find")
menubar.add_cascade(label="Search", menu=searchmenu)

colourmenu = Menu(menubar, tearoff=0)
colourmenu.add_command(label="fg", command=fg_)
colourmenu.add_command(label="bg", command=bg_)
menubar.add_cascade(label="Colour", menu=colourmenu)

formatmenu = Menu(menubar, tearoff=0)
formatmenu.add_radiobutton(label='Normal', command=normal)
formatmenu.add_radiobutton(label='Italic', command=italic)
formatmenu.add_radiobutton(label='Bold', command=bold)
formatmenu.add_radiobutton(label='Underline', command=underline)
menubar.add_cascade(menu=formatmenu, label='Format')

helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="About", command=about)
menubar.add_cascade(label="Help", menu=helpmenu)

root.config(menu=menubar)

root.mainloop()
