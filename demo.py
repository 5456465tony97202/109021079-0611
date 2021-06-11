from tkinter import *

flag=True

def test(n):
    global flag
    if n==1:
        if flag:
           btn1.config(text="O")
        else:
            btn1.config(text="X")
        btn1.config(state="disable")
    elif n==2:
        if flag:
           btn2.config(text="O")
        else:
            btn2.config(text="X")
        btn2.config(state="disable")
    elif n==3:
       if flag:
           btn3.config(text="O")
       else:
            btn3.config(text="X")
       btn3.config(state="disable")
    elif n==4:
       if flag:
           btn4.config(text="O")
       else:
            btn4.config(text="X")
       btn4.config(state="disable")
    elif n==5:
       if flag:
           btn5.config(text="O")
       else:
            btn5.config(text="X")
       btn5.config(state="disable")
    elif n==6:
       if flag:
           btn6.config(text="O")
       else:
            btn6.config(text="X")
       btn6.config(state="disable")
    elif n==7:
       if flag:
           btn7.config(text="O")
       else:
            btn7.config(text="X")
       btn7.config(state="disable")
    elif n==8:
        if flag:
           btn8.config(text="O")
        else:
            btn8.config(text="X")
        btn8.config(state="disable")
    elif n==9:
        if flag:
           btn9.config(text="O")
        else:
            btn9.config(text="X")
        btn9.config(state="disable")
    flag= not flag

    if btn1.cget("text")==btn2.cget("text") and btn1.cget("text")==btn3.cget("text"):
       if btn1.cget("text")=="O":
           print("player 1 win")
       elif btn1.cget("text")=="X":
           print("player 2 win")
    if btn1.cget("text")==btn4.cget("text") and btn4.cget("text")==btn7.cget("text"):
          if btn1.cget("text")=="O":
           print("player 1 win")
          elif btn1.cget("text")=="X":
           print("player 2 win")
    if btn2.cget("text")==btn5.cget("text") and btn2.cget("text")==btn8.cget("text"):
           if btn2.cget("text")=="O":
              print("player 1 win")
           elif btn2.cget("text")=="X":
                print("player 2 win")
    if btn4.cget("text")==btn5.cget("text") and btn4.cget("text")==btn6.cget("text"):
       if btn4.cget("text")=="O":
           print("player 1 win")
       elif btn4.cget("text")=="X":
           print("player 2 win")
    if btn3.cget("text")==btn6.cget("text") and btn3.cget("text")==btn9.cget("text"):
       if btn3.cget("text")=="O":
           print("player 1 win")
       elif btn3.cget("text")=="X":
           print("player 2 win")
    if btn3.cget("text")==btn5.cget("text") and btn3.cget("text")==btn7.cget("text"):
       if btn3.cget("text")=="O":
           print("player 1 win")
       elif btn3.cget("text")=="X":
           print("player 2 win")
    if btn7.cget("text")==btn8.cget("text") and btn7.cget("text")==btn9.cget("text"):
       if btn7.cget("text")=="O":
           print("player 1 win")
       elif btn7.cget("text")=="X":
           print("player 2 win")
    if btn1.cget("text")==btn5.cget("text") and btn9.cget("text")==btn9.cget("text"):
       if btn1.cget("text")=="O":
           print("player 1 win")
       elif btn1.cget("text")=="X":
           print("player 2 win")

window=Tk()
window.title("Label demo")
window.geometry("500x400+100+50")
window.rowconfigure(0,weight=1)
window.rowconfigure(1,weight=1)
window.rowconfigure(2,weight=1)
window.columnconfigure(0,weight=1)
window.columnconfigure(1,weight=1)
window.columnconfigure(2,weight=1)


btn1=Button(window,text="",command=lambda:test(1),relief="raised")
btn1.grid(row=0,column=0,sticky=NSEW)

btn2=Button(window,text="",command=lambda:test(2),relief="raised")
btn2.grid(row=0,column=1,sticky=NSEW)

btn3=Button(window,text="",command=lambda:test(3),relief="raised")
btn3.grid(row=0,column=2,sticky=NSEW)

btn4=Button(window,text="",command=lambda:test(4),relief="raised")
btn4.grid(row=1,column=0,sticky=NSEW)

btn5=Button(window,text="",command=lambda:test(5),relief="raised")
btn5.grid(row=1,column=1,sticky=NSEW)

btn6=Button(window,text="",command=lambda:test(6),relief="raised")
btn6.grid(row=1,column=2,sticky=NSEW)

btn7=Button(window,text="",command=lambda:test(7),relief="raised")
btn7.grid(row=2,column=0,sticky=NSEW)

btn8=Button(window,text="",command=lambda:test(8),relief="raised")
btn8.grid(row=2,column=1,sticky=NSEW)

btn9=Button(window,text="",command=lambda:test(9),relief="raised")
btn9.grid(row=2,column=2,sticky=NSEW)

window.mainloop()
