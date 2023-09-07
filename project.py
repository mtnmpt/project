from tkinter import *
root = Tk()
root.title("Casio")
root.geometry("300x300")
root.config(background='gray')
display = Entry(root,borderwidth=5,fg='red')
display.grid(row=1,columnspan=6,ipadx=100,ipady=10)
Button_number1 = Button(root, text="1", bg='black', fg='white', height= 3 , width=6, command=lambda: number(1)).grid(row=2, column=0)
Button_number2 = Button(root, text=" 2", bg='black', fg='white', height= 3, width=6, command=lambda: number(2)).grid(row=2, column=1)
Button_number3 = Button(root, text=" 3", bg='black', fg='white', height= 3, width=6 ,command=lambda: number(3)).grid(row=2, column=2)
Button_add = Button(root, text="+", bg='black', fg='white', height= 3, width=6 ,command=lambda: operation("+")).grid(row=2, column=3)
Button_number4 = Button(root, text="4", bg='black', fg='white', height= 3, width=6 , command=lambda: number(4)).grid(row=3, column=0)
Button_number5 = Button(root, text=" 5", bg='black', fg='white', height= 3, width=6 ,command=lambda: number(5)).grid(row=3, column=1)
Button_number6 = Button(root, text=" 6", bg='black', fg='white', height= 3, width=6 , command=lambda: number(6)).grid(row=3, column=2)
Button_minus = Button(root, text="-", bg='black', fg='white', height= 3, width=6 ,command=lambda: operation("-")).grid(row=3, column=3)
Button_number7 = Button(root, text="7", bg='black', fg='white', height= 3, width=6 , command=lambda: number(7)).grid(row=4, column=0)
Button_number8 = Button(root, text=" 8", bg='black', fg='white', height= 3, width=6 ,command=lambda: number(8)).grid(row=4, column=1,)
Button_number9 = Button(root, text=" 9", bg='black', fg='white', height= 3, width=6 ,command=lambda: number(9)).grid(row=4, column=2)
Button_multiple = Button(root, text="*", bg='black', fg='white', height= 3, width=6 ,command=lambda: operation("*")).grid(row=4, column=3)
Button_undo = Button(root, text="AC", bg='black', fg='white', height= 3, width=6 , command=lambda: clear_all()).grid(row=5, column=0)
Button_number0 = Button(root, text=" 0", bg='black', fg='white', height= 3, width=6 ,command=lambda: number(0)).grid(row=5, column=1)
Button_equal = Button(root, text="=", bg='black', fg='white', height= 3, width=6 , command=lambda: calculate()).grid(row=5,column=2)
Button_divide = Button(root, text="/", bg='black', fg='white', height= 3, width=6 ,command=lambda: operation("/")).grid(row=5, column=3)
i=0
def number(num):
    global i
    display.insert(i,num)
    i+=1
def operation(a):
    global i
    length = len(a)
    display.insert(i,a )
    i+=length
def clear_all():
    display.delete(0,END)
def calculate():
    string = display.get()
    try:
        result = eval(string)
        clear_all()
        display.insert(0,result)
    except Exception:
        clear_all()
        display.insert(0,"Error")
root.mainloop()
# quên mẹ rồi

# 1 ngày mới tốt lành nhé


