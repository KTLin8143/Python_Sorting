from Tkinter import *
import random

master = Tk()


def gen():
    list = []
    for x in range(0, 10):
        list.append(random.randint(0, 100))
    num = ''.join('%4i' % num for num in list)
    label = Label(master, text=num, width=2, height=2)
    label.grid(row=2, columnspan=10, sticky=W + E + N + S)


var = IntVar()

R1 = Radiobutton(master, text='Bubble Sort', variable=var, value=1)
R1.grid(row=0, column=0)

R2 = Radiobutton(master, text='Insertion Sort', variable=var, value=2)
R2.grid(row=0, column=1)

R3 = Radiobutton(master, text='Selection Sort', variable=var, value=3)
R3.grid(row=0, column=2)

R4 = Button(master, text='Generate random number', command=gen)
R4.grid(row=1, column=1, sticky=W + E + N + S)
"""main"""
mainloop()
