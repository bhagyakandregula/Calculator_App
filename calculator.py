from tkinter import *

cal = Tk()
cal.title('Calculator')


def clear():
    design.delete(0, END)


def btn_clk(num):
    cur_num = design.get()
    clear()
    f_num = cur_num + num
    design.insert(0, f_num)


first_num = 0
math = ''


def calc(math_type):
    global first_num, math
    math = math_type

    first_num = design.get()
    clear()


def equal():
    result = ''
    second_num = design.get()
    clear()
    if math == 'add':
        result = int(first_num) + int(second_num)
    elif math == 'sub':
        result = int(first_num) - int(second_num)
    elif math == 'mul':
        result = int(first_num) * int(second_num)
    elif math == 'div':
        result = int(first_num) / int(second_num)
    design.insert(0, str(result))


# CREATING WIDGETS
design = Entry(cal, width=14, font=('Arial', 28), justify=RIGHT)
btn_0 = Button(cal, text='0', padx=36, pady=10, font=('Arial', 14), command=lambda: btn_clk('0'))
btn_1 = Button(cal, text='1', padx=36, pady=10, font=('Arial', 14), command=lambda: btn_clk('1'))
btn_2 = Button(cal, text='2', padx=36, pady=10, font=('Arial', 14), command=lambda: btn_clk('2'))
btn_3 = Button(cal, text='3', padx=36, pady=10, font=('Arial', 14), command=lambda: btn_clk('3'))
btn_4 = Button(cal, text='4', padx=36, pady=10, font=('Arial', 14), command=lambda: btn_clk('4'))
btn_5 = Button(cal, text='5', padx=36, pady=10, font=('Arial', 14), command=lambda: btn_clk('5'))
btn_6 = Button(cal, text='6', padx=36, pady=10, font=('Arial', 14), command=lambda: btn_clk('6'))
btn_7 = Button(cal, text='7', padx=36, pady=10, font=('Arial', 14), command=lambda: btn_clk('7'))
btn_8 = Button(cal, text='8', padx=36, pady=10, font=('Arial', 14), command=lambda: btn_clk('8'))
btn_9 = Button(cal, text='9', padx=36, pady=10, font=('Arial', 14), command=lambda: btn_clk('9'))
btn_clear = Button(cal, text='clear', padx=74, pady=10, font=('Arial', 14), command=clear)
btn_mul = Button(cal, text='*', padx=38, pady=10, font=('Arial', 14), command=lambda: calc('mul'))
btn_div = Button(cal, text='/', padx=38, pady=10, font=('Arial', 14), command=lambda: calc('div'))
btn_add = Button(cal, text='+', padx=36, pady=10, font=('Arial', 14), command=lambda: calc('add'))
btn_sub = Button(cal, text='-', padx=38, pady=10, font=('Arial', 14), command=lambda: calc('sub'))
btn_equal = Button(cal, text='=', padx=36, pady=40, font=('Arial', 14), command=equal)

# SHOW WIDGETS
design.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

btn_add.grid(row=6, column=0, padx=2, pady=2)
btn_sub.grid(row=6, column=1, padx=2, pady=2)

btn_equal.grid(row=5, column=2, rowspan=2, padx=2, pady=2)
btn_mul.grid(row=5, column=0, padx=2, pady=2)
btn_div.grid(row=5, column=1, padx=2, pady=2)

btn_0.grid(row=4, column=0, padx=2, pady=2)
btn_clear.grid(row=4, column=1, columnspan=2, padx=2, pady=2)

btn_1.grid(row=3, column=0, padx=2, pady=2)
btn_2.grid(row=3, column=1, padx=2, pady=2)
btn_3.grid(row=3, column=2, padx=2, pady=2)

btn_4.grid(row=2, column=0, padx=2, pady=2)
btn_5.grid(row=2, column=1, padx=2, pady=2)
btn_6.grid(row=2, column=2, padx=2, pady=2)

btn_7.grid(row=1, column=0, padx=2, pady=2)
btn_8.grid(row=1, column=1, padx=2, pady=2)
btn_9.grid(row=1, column=2, padx=2, pady=2)

cal.mainloop()
