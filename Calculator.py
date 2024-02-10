from tkinter import *

h = 2
w = 8

root = Tk()
root.geometry("196x293")
root.title("Calculator")

e = Entry(width=27, borderwidth=15)
e.grid(row=0, column=0, columnspan=5)

def button_click(number):
    current=e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))

def button_clear():
     e.delete(0,END)

def add():
    first_num = e.get()
    global f_num
    global math
    math = "add"
    f_num = int(first_num)
    e.delete(0,END)

def subtract():
    first_num = e.get()
    global f_num
    global math
    math = "subtract"
    f_num = int(first_num)
    e.delete(0, END)

def multiply():
    first_num = e.get()
    global f_num
    global math
    math = "multiply"
    f_num = int(first_num)
    e.delete(0, END)

def divide():
    first_num = e.get()
    global f_num
    global math
    math = "divide"
    f_num = int(first_num)
    e.delete(0, END)

def equal():
    second_num = e.get()
    e.delete(0, END)

    if(math=="add"):
        e.insert(0, f_num + int(second_num))
    elif(math=="subtract"):
        e.insert(0, f_num - int(second_num))
    elif (math == "multiply"):
        e.insert(0, f_num * int(second_num))
    elif (math == "divide"):
        e.insert(0, f_num / int(second_num))

B_1 = Button (text="1",width=w,height=h,command=lambda: button_click(1))
B_2 = Button (text="2",width=w,height=h,command=lambda: button_click(2))
B_3 = Button (text="3",width=w,height=h,command=lambda: button_click(3))
B_4 = Button (text="4",width=w,height=h,command=lambda: button_click(4))
B_5 = Button (text="5",width=w,height=h,command=lambda: button_click(5))
B_6 = Button (text="6",width=w,height=h,command=lambda: button_click(6))
B_7 = Button (text="7",width=w,height=h,command=lambda: button_click(7))
B_8 = Button (text="8",width=w,height=h,command=lambda: button_click(8))
B_9 = Button (text="9",width=w,height=h,command=lambda: button_click(9))
B_0 = Button (text="0",width=w,height=h,command=lambda: button_click(0))

B_add = Button (text="+",width=w,height=h,command=add)
B_subtract = Button (text="-",width=w,height=h,command=subtract)
B_multiply = Button (text="*",width=w,height=h,command=multiply)
B_divide = Button (text="/",width=w,height=h,command=divide)

B_Equal = Button (text="=",width=w,height=h,command=equal)
B_AC = Button (text="AC",width=27,height=h,command=button_clear)

B_1.grid(row=1,column=0)
B_2.grid(row=1,column=1)
B_3.grid(row=1,column=2)

B_4.grid(row=2,column=0)
B_5.grid(row=2,column=1)
B_6.grid(row=2,column=2)

B_7.grid(row=3,column=0)
B_8.grid(row=3,column=1)
B_9.grid(row=3,column=2)

B_0.grid(row=4,column=1)

B_add.grid(row=4,column=2)
B_subtract.grid(row=5,column=2)
B_multiply.grid(row=4,column=0)
B_divide.grid(row=5,column=0)

B_Equal.grid(row=5,column=1)
B_AC.grid(row=6,column=0, columnspan=5)

root.mainloop()