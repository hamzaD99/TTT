#This project made by Hamza Daoud - Jordan 9/7/2019
#Inspired by this video on youtube with some changes:
#https://www.youtube.com/watch?v=ZSPCURHGtmQ&list=PLF8OvnCBlEY1j4hxoqXqJk08ASU7D_W87&index=48
#Enjoy!

from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from random import randint
ActivePlayer=1
p1=[]
p2=[]
CM = False

root=Tk()
root.title("Tic Tac Toy: Player 1")
style=ttk.Style()
style.theme_use('classic')
style.map('Info.TButton',foreground=[('disabled','Green') ,('!disabled','blue')],background=[('disabled','#212121')])
style.map('PressX.TButton',foreground=[('disabled','Black')],background=[('disabled','#817F7F')])
style.configure('PressX.TButton',font=('Arial',30))
style.map('PressO.TButton',foreground=[('disabled','red')],background=[('disabled','#817F7F')])
style.configure('PressO.TButton',font=('Arial',30))
#Button 1
bu1=ttk.Button(root,text=' ')
bu1.grid(row=1,column=0,sticky='snew',ipadx=30,ipady=30)
bu1.config(command=lambda :BuClick(1))
#Button 2
bu2=ttk.Button(root,text=' ')
bu2.grid(row=1,column=1,sticky='snew',ipadx=30,ipady=30)
bu2.config(command=lambda :BuClick(2))

#Button 3
bu3=ttk.Button(root,text=' ')
bu3.grid(row=1,column=2,sticky='snew',ipadx=30,ipady=30)
bu3.config(command=lambda :BuClick(3))

#Button 4
bu4=ttk.Button(root,text=' ')
bu4.grid(row=2,column=0,sticky='snew',ipadx=30,ipady=30)
bu4.config(command=lambda :BuClick(4))

#Button 5
bu5=ttk.Button(root,text=' ')
bu5.grid(row=2,column=1,sticky='snew',ipadx=30,ipady=30)
bu5.config(command=lambda :BuClick(5))

#Button 6
bu6=ttk.Button(root,text=' ')
bu6.grid(row=2,column=2,sticky='snew',ipadx=30,ipady=30)
bu6.config(command=lambda :BuClick(6))

#Button 7
bu7=ttk.Button(root,text=' ')
bu7.grid(row=3,column=0,sticky='snew',ipadx=30,ipady=30)
bu7.config(command=lambda :BuClick(7))

#Button 8
bu8=ttk.Button(root,text=' ')
bu8.grid(row=3,column=1,sticky='snew',ipadx=30,ipady=30)
bu8.config(command=lambda :BuClick(8))

#Button 9
bu9=ttk.Button(root,text=' ')
bu9.grid(row=3,column=2,sticky='snew',ipadx=30,ipady=30)
bu9.config(command=lambda :BuClick(9))

#Reset
bu10=ttk.Button(root,text='Reset')
bu10.grid(row=0,column=1,sticky='snew',ipadx=35,ipady=10)
bu10.config(command=lambda :Reset())

#C1
bu11=ttk.Button(root,text='Comp')
bu11.grid(row=0,column=0,sticky='snew',ipadx=35,ipady=10)
bu11.config(command=lambda :Mode(1))
bu11.configure(style='Info.TButton')
#C2
bu12=ttk.Button(root,text='P2')
bu12.grid(row=0,column=2,sticky='snew',ipadx=35,ipady=10)
bu12.config(command=lambda :Mode(2))
bu12.state(['disabled'])
bu12.configure(style='Info.TButton')

def Reset():
    global ActivePlayer
    global p1
    global p2
    ActivePlayer = 1
    root.title("Tic Tac Toy: Player 1")
    Mode(2)
    p1 = []
    p2 = []
    for x in range(9):
        SetLayout(x+1,' ','!disabled')
def BuClick(id):
    global ActivePlayer
    global p1
    global p2
    global CM
    if(ActivePlayer==1):
        SetLayout(id,'X','disabled')
        p1.append(id)
        root.title("Tic Tac Toy: Player 2")
        ActivePlayer=2
        #print('P1: {}'.format(p1))
        if CM == True:
            AutoPlay()
    elif(ActivePlayer==2):
        SetLayout(id,'O','disabled')
        p2.append(id)
        root.title("Tic Tac Toy: Player 1")
        ActivePlayer=1
        #print('P2: {}'.format(p2))
    CheckWinner()
def SetLayout(id,t,state):
    if(id==1):
        bu1.config(text=t)
        bu1.state([state])
        if t=='X':
            bu1.configure(style='PressX.TButton')
        elif t=='O':
            bu1.configure(style='PressO.TButton')
    elif(id==2):
        bu2.config(text=t)
        bu2.state([state])
        if t=='X':
            bu2.configure(style='PressX.TButton')
        elif t=='O':
            bu2.configure(style='PressO.TButton')
    elif(id==3):
        bu3.config(text=t)
        bu3.state([state])
        if t=='X':
            bu3.configure(style='PressX.TButton')
        elif t=='O':
            bu3.configure(style='PressO.TButton')
    elif(id==4):
        bu4.config(text=t)
        bu4.state([state])
        if t=='X':
            bu4.configure(style='PressX.TButton')
        elif t=='O':
            bu4.configure(style='PressO.TButton')
    elif(id==5):
        bu5.config(text=t)
        bu5.state([state])
        if t=='X':
            bu5.configure(style='PressX.TButton')
        elif t=='O':
            bu5.configure(style='PressO.TButton')
    elif(id==6):
        bu6.config(text=t)
        bu6.state([state])
        if t=='X':
            bu6.configure(style='PressX.TButton')
        elif t=='O':
            bu6.configure(style='PressO.TButton')
    elif(id==7):
        bu7.config(text=t)
        bu7.state([state])
        if t=='X':
            bu7.configure(style='PressX.TButton')
        elif t=='O':
            bu7.configure(style='PressO.TButton')
    elif(id==8):
        bu8.config(text=t)
        bu8.state([state])
        if t=='X':
            bu8.configure(style='PressX.TButton')
        elif t=='O':
            bu8.configure(style='PressO.TButton')
    elif(id==9):
        bu9.config(text=t)
        bu9.state([state])
        if t=='X':
            bu9.configure(style='PressX.TButton')
        elif t=='O':
            bu9.configure(style='PressO.TButton')
def CheckWinner():
    win=-1
    EC = []
    for cell in range(9):
        if (not ((cell + 1 in p1) or (cell + 1 in p2))):
            EC.append(cell + 1)
   # print(EC[0])
    if len(EC) == 0:
        win = -1
        messagebox.showinfo(title='Try Again!', message='TIE')
    elif(len(EC) != 0):
        #Row 1
        if((1 in p1) and (2 in p1) and (3 in p1)):
            win = 1
        if((1 in p2) and (2 in p2) and (3 in p2)):
            win = 2
        #Row 2
        if((4 in p1) and (5 in p1) and (6 in p1)):
            win = 1
        if((4 in p2) and (5 in p2) and (6 in p2)):
            win = 2
        #Row 3
        if((7 in p1) and (8 in p1) and (9 in p1)):
            win = 1
        if((7 in p2) and (8 in p2) and (9 in p2)):
            win = 2

        #Col 1
        if((1 in p1) and (4 in p1) and (7 in p1)):
            win = 1
        if((1 in p2) and (4 in p2) and (7 in p2)):
            win = 2
        #Col 2
        if((2 in p1) and (5 in p1) and (8 in p1)):
            win = 1
        if((2 in p2) and (5 in p2) and (8 in p2)):
            win = 2
        #Col 3
        if((3 in p1) and (6 in p1) and (9 in p1)):
            win = 1
        if((3 in p2) and (6 in p2) and (9 in p2)):
            win = 2
        #Q 1
        if((1 in p1) and (5 in p1) and (9 in p1)):
            win = 1
        if((1 in p2) and (5 in p2) and (9 in p2)):
            win = 2
        #Q 1
        if((3 in p1) and (5 in p1) and (7 in p1)):
            win = 1
        if((3 in p2) and (5 in p2) and (7 in p2)):
            win = 2
        if (win!=-1):
            messagebox.showinfo(title='We have winner!', message='Player {} is winner!'.format(win))
            for x in range(len(EC)):
                if EC[x] == 1:
                    bu1.state(['disabled'])
                if EC[x] == 2:
                    bu2.state(['disabled'])
                if EC[x] == 3:
                    bu3.state(['disabled'])
                if EC[x] == 4:
                    bu4.state(['disabled'])
                if EC[x] == 5:
                    bu5.state(['disabled'])
                if EC[x] == 6:
                    bu6.state(['disabled'])
                if EC[x] == 7:
                    bu7.state(['disabled'])
                if EC[x] == 8:
                    bu8.state(['disabled'])
                if EC[x] == 9:
                    bu9.state(['disabled'])
def AutoPlay():
    global p1
    global p2
    EC=[]
    for cell in range(9):
        if(not((cell+1 in p1) or (cell+1 in p2))):
            EC.append(cell+1)
    if len(EC) != 0:
        RandIdx = randint(0,len(EC)-1)
        BuClick(EC[RandIdx])
def Mode(x):
    global CM
    if x==1:
        CM = True
        bu11.state(['disabled'])
        bu11.configure(style='Info.TButton')
        bu12.state(['!disabled'])
    elif x==2:
        CM=False
        bu11.state(['!disabled'])
        bu12.state(['disabled'])
        bu12.configure(style='Info.TButton')

root.rowconfigure(0,weight=1)
root.rowconfigure(1,weight=1)
root.rowconfigure(2,weight=1)
root.columnconfigure(0,weight=1)
root.columnconfigure(1,weight=1)
root.columnconfigure(2,weight=1)
root.mainloop()