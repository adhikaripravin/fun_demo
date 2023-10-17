from tkinter import *
from tkinter import messagebox
import random
# class Demo:
#     def __init__(self,root):
        # pass
        
        
        
def no():
    messagebox.showinfo(' ','Thanks bro')
    quit()
        
def motionMouse(event) :
    btnYes.place(x=random.randint(0, 500), y=random.randint(0, 500))
    
    
root=Tk()
root.geometry('600x600')
root.title('testing')
root.resizable(width=False, height=False)
root['bg'] = 'blue'
        
label = Label(root, text='Are you gay ?', font='Arial 20 bold', bg='red')
label.pack()

btnYes = Button(root, text='No', font='Arial 20 bold')
btnYes.place(x=170,y=100)
btnYes.bind('<Enter>', motionMouse)
    
btnNo = Button(root, text='Yes', font='Arial 20 bold', command=no)
btnNo.place(x=350, y=100)
        
# obj = Demo(root)
root.mainloop()