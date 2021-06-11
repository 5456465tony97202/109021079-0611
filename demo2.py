from tkinter import*

op=0
a=0
opflag=False
def Text(n):
    if int(lab["text"]) !=0 and opFlag==False:
       lab["text"]=lab["text"]+n
    else:
        lab["text"]=n

def set(Value):
    global op
    global a
    global opflag
    opflag=True
    a=int(lab["text"])
    op=Value
def computer():
    b=int(lab["text"])
    global op
    if op==1:
        lab["text"]=a+b
    elif op==2:
        lab["text"]=a-b
    elif op==3:
        lab["text"]=a*b
    elif op==4:
        lab["text"]=a/b

window=Tk()
window.title("Label demo")
window.geometry("500x400+100+50")
window.rowconfigure(1,weight=1)
window.rowconfigure(2,weight=1)
window.rowconfigure(3,weight=1)
window.rowconfigure(4,weight=1)
window.columnconfigure(0,weight=1)
window.columnconfigure(1,weight=1)
window.columnconfigure(2,weight=1)
window.rowconfigure(3,weight=1)

lab=Label(window,text="0",justify=RIGHT,anchor=W,font=("Monaco",30,"bold"),bg="#DCDCDC")
lab.grid(row=0,column=0,columnspan=4,sticky=EW)


btn1=Button(window,text="1",font=("Monaco",30,"bold"),relief="raised",command=lambda:Text("1"))
btn1.grid(row=1,column=0,sticky=NSEW)
btn2=Button(window,text="2",font=("Monaco",30,"bold"),relief="raised",command=lambda:Text("2"))
btn2.grid(row=1,column=1,sticky=NSEW)
btn3=Button(window,text="3",font=("Monaco",30,"bold"),relief="raised",command=lambda:Text("3"))
btn3.grid(row=1,column=2,sticky=NSEW)
btn4=Button(window,text="4",font=("Monaco",30,"bold"),relief="raised",command=lambda:Text("4"))
btn4.grid(row=2,column=0,sticky=NSEW)
btn5=Button(window,text="5",font=("Monaco",30,"bold"),relief="raised",command=lambda:Text("5"))
btn5.grid(row=2,column=1,sticky=NSEW)
btn6=Button(window,text="6",font=("Monaco",30,"bold"),relief="raised",command=lambda:Text("6"))
btn6.grid(row=2,column=2,sticky=NSEW)
btn7=Button(window,text="7",font=("Monaco",30,"bold"),relief="raised",command=lambda:Text("7"))
btn7.grid(row=3,column=0,sticky=NSEW)
btn8=Button(window,text="8",font=("Monaco",30,"bold"),relief="raised",command=lambda:Text("8"))
btn8.grid(row=3,column=1,sticky=NSEW)
btn9=Button(window,text="9",font=("Monaco",30,"bold"),relief="raised",command=lambda:Text("9"))
btn9.grid(row=3,column=2,sticky=NSEW)
btn0=Button(window,text="0",font=("Monaco",30,"bold"),relief="raised",command=lambda:Text("0"))
btn0.grid(row=4,column=0,sticky=NSEW)
btn10=Button(window,text=".",font=("Monaco",30,"bold"),relief="raised",command=lambda:Text("."))
btn10.grid(row=4,column=1,sticky=NSEW)
btn11=Button(window,text="=",font=("Monaco",30,"bold"),relief="raised",command=lambda:Text(""))
btn11.grid(row=4,column=2,sticky=NSEW)
btn12=Button(window,text="+",font=("Monaco",30,"bold"),relief="raised",command=lambda:computer("1"))
btn12.grid(row=1,column=3,sticky=NSEW)
btn13=Button(window,text="-",font=("Monaco",30,"bold"),relief="raised",command=lambda:computer("2"))
btn13.grid(row=2,column=3,sticky=NSEW)
btn14=Button(window,text="*",font=("Monaco",30,"bold"),relief="raised",command=lambda:computer("3"))
btn14.grid(row=3,column=3,sticky=NSEW)
btn15=Button(window,text="/",font=("Monaco",30,"bold"),relief="raised",command=lambda:computer("4"))
btn15.grid(row=4,column=3,sticky=NSEW)

window.mainloop()