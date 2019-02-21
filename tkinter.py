from tkinter import*
import webbrowser
import cx_Oracle
def show():
  name=text1.get()
  name1=text2.get()
  if name=="pavi" and name1=="kapa":
      print("hello")
      webbrowser.open("http://www.google.co.in")
  else:
      print("invalid password")
main=Tk()
main.title("STC")
main.geometry("300x300")
main.configure(background="skyblue")
Label(main,text="username",font=60,fg="white",bg="pink").grid(row=1,column=1)
Label(main,text="password",font=60,fg="white",bg="pink").grid(row=2,column=1)
text1=Entry(main,width=20,bg="white")
text1.grid(row=1,column=2)
text2=Entry(main,width=20,bg="white")
text2.grid(row=2,column=2)
e=Button(main,width=10,text="submit",bg="black",fg="white",font=20,command=show)
e.grid(row=5,column=2)
