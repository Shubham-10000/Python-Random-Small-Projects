from AI.simple_interest import Simple_interest
import random
from tkinter.constants import Y


x=float(input('enter value:'))
y=float(input('enter value:'))

op = input("do you want all arithmetic operations done on this numbers,press'y':")
if op =='y':
    def values():
        #addition
        z=x+y
        z=int(z)
        print("the addition of two number is: ",z)

        #subtraction
        z=x-y
        z=int(z)
        print("the subtraction of two number is: ",z)

        #multiplication
        z=x*y
        z=int(z)
        print("the multiplicaton of two number is: ",z)

        #divide
        z=x/y
    
        print("the divide of two number is: ",z)

        #remainder
        z=x//y
    
        print("the remainder of two number is: ",z)
    




#def values():


    #addition
    z=x+y
    z=int(z)
    print("the addition of two number is: ",z)

    #subtraction
    z=x-y
    z=int(z)
    print("the subtraction of two number is: ",z)

    #multiplication
    z=x*y
    z=int(z)
    print("the multiplicaton of two number is: ",z)

    #divide
    z=x/y
    
    print("the divide of two number is: ",z)

    #remainder
    z=x//y
    
    print("the remainder of two number is: ",z)

#dice code 

def dice():
    x='y'
    while x=='y':
        no=random.randint(1,6)


        if no == 1:
            print("[--------]")
            print("[        ]")
            print("[   0    ]")
            print("[        ]")
            print("[--------]")
        
        if no == 2:
            print("[--------]")
            print("[ 0      ]")
            print("[        ]")
            print("[      0 ]")
            print("[--------]")

        if no == 3:
            print("[--------]")
            print("[ 0      ]")
            print("[   0    ]")
            print("[      0 ]")
            print("[--------]")

        if no == 4:
            print("[--------]")
            print("[ 0    0 ]")
            print("[        ]")
            print("[ 0    0 ]")
            print("[--------]")

        if no == 5:
            print("[--------]")
            print("[ 0    0 ]")
            print("[    0   ]")
            print("[ 0    0 ]")
            print("[--------]")

        if no == 6:
            print("[--------]")
            print("[ 0    0 ]")
            print("[ 0    0 ]")
            print("[ 0    0 ]")
            print("[--------]")

        x=input("press y to roll again and n to exit:")
        print("\n")


# code for clock 
from tkinter import *
from tkinter.ttk import *
from time import strftime

root = Tk()
root.title("Clock")

def time():
    string=strftime('%H:%M:%S.%p')
    label.config(text=string)
    label.after(1000, time)



label=Label(root,font=("ds_digital",80),background='white',foreground='black')
label.pack(anchor='center')


time()
values()
dice()
mainloop()


