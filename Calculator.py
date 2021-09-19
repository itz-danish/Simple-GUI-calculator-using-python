from tkinter import *

root = Tk()


###
mystr = StringVar()
mystr.set("")
###

'''All functions'''
###
def n1():
	calc=mystr.get()
	calc=calc+"1"
	mystr.set(calc)

def n2():
	calc=mystr.get()
	calc=calc+"2"
	mystr.set(calc)
	
def n3():
	calc=mystr.get()
	calc=calc+"3"
	mystr.set(calc)

def n4():
	calc=mystr.get()
	calc=calc+"4"
	mystr.set(calc)

def n5():
	calc=mystr.get()
	calc=calc+"5"
	mystr.set(calc)

def n6():
	calc=mystr.get()
	calc=calc+"6"
	mystr.set(calc)

def n7():
	calc=mystr.get()
	calc=calc+"7"
	mystr.set(calc)

def n8():
	calc=mystr.get()
	calc=calc+"8"
	mystr.set(calc)

def n9():
	calc=mystr.get()
	calc=calc+"9"
	mystr.set(calc)

def n0():
	calc=mystr.get()
	calc=calc+"0"
	mystr.set(calc)

def point():
	calc=mystr.get()
	calc=calc+"."
	mystr.set(calc)

def equal():
	calc=mystr.get()
	calc=eval(calc)
	mystr.set(calc)

def plus():
	calc=mystr.get()
	calc=calc+"+"
	mystr.set(calc)

def clear():
	calc=""
	mystr.set(calc)

def erase():
	calc=mystr.get()
	calc=calc[0:-1]
	mystr.set(calc)

def minus():
	calc=mystr.get()
	calc=calc+"-"
	mystr.set(calc)

def multiply():
	calc=mystr.get()
	calc=calc+"*"
	mystr.set(calc)

def divide():
	calc=mystr.get()
	calc=calc+"/"
	mystr.set(calc)





###

###
Label(root, text="Calculator by Danish").grid(row=1)
###


'''Exit Button'''
###
exit_button = Button(root, text="exit", justify="right", command=root.destroy).grid(row=1, pady=5, padx=2, sticky="E")
###

'''Display'''
###
entry = Entry(textvariable=mystr, state=DISABLED, font=("Calibri",15)).grid(padx=10, pady=10, ipadx=30, ipady=70)
###

'''Buttons'''
###

###   1st row
minus_btn = Button(root, text="-", font=("Calibri", 10), command=minus).grid(row=100, sticky="w", padx=5, ipadx=83, ipady=50)

multiply_btn = Button(root, text="×", font=("Calibri", 10), command=multiply).grid(row=100, sticky="n", ipadx=45, ipady=50)

divide_btn = Button(root, text="÷", 
font=("Calibri", 10), command=divide).grid(row=100, sticky="e", ipadx=80, padx=5, ipady=50)
###

###    2nd row

add_btn = Button(root, text="+", font=("Calibri", 10), command=plus).grid(row=101, sticky="w", ipadx=78, padx=5, ipady=50, pady=10)


clear_btn = Button(root, text="Clear", font=("Calibri", 10), command=clear).grid(row=101, sticky="n", ipadx=10, padx=5, ipady=50, pady=10)

erase_btn = Button(root, text="<-", font=("Calibri", 10), command=erase).grid(row=101, sticky="e", ipadx=75, padx=5, ipady=50, pady=10)

###

###    3rd row

n7_btn = Button(root, text="7", font=("Calibri", 10), command=n7).grid(row=102, sticky="w", ipadx=78, padx=5, ipady=50, pady=10)

n8_btn = Button(root, text="8", font=("Calibri", 10), command=n8).grid(row=102, sticky="n", ipadx=45, padx=5, ipady=50, pady=10)

n9_btn = Button(root, text="9", font=("Calibri", 10), command=n9).grid(row=102, sticky="e", ipadx=80, padx=5, ipady=50, pady=10)

###

###  4th row

n4_btn = Button(root, text="4", font=("Calibri", 10), command=n4).grid(row=103, sticky="w", ipadx=78, padx=5, ipady=50, pady=10)

n5_btn = Button(root, text="5", font=("Calibri", 10), command=n5).grid(row=103, sticky="n", ipadx=45, padx=5, ipady=50, pady=10)

n6_btn = Button(root, text="6", font=("Calibri", 10), command=n6).grid(row=103, sticky="e", ipadx=80, padx=5, ipady=50, pady=10)

###

###  5th row

n1_btn = Button(root, text="1", font=("Calibri", 10), command=n1).grid(row=104, sticky="w", ipadx=78, padx=5, ipady=50, pady=10)

n2_btn = Button(root, text= "2", font=("Calibri", 10), command=n2).grid(row=104, sticky="n", ipadx=45, padx=5, ipady=50, pady=10)

n3_btn = Button(root, text="3", font=("Calibri", 10), command=n3).grid(row=104, sticky="e", ipadx=80, padx=5, ipady=50, pady=10)

###

### 6th row

n0_btn = Button(root, text="0", font=("Calibri", 10), command=n0).grid(row=105, sticky="w", ipadx=78, padx=5, ipady=50, pady=10)

point_btn = Button(root, text=".", font=("Calibri", 10), command=point).grid(row=105, sticky="n", ipadx=50, padx=5, ipady=50, pady=10)

equals_btn = Button(root, text="=", font=("Calibri", 10), command=equal).grid(row=105, sticky="e", ipadx=80, padx=5, ipady=50, pady=10)

###

###

root.mainloop()
