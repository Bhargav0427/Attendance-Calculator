from tkinter import *
import tkinter.messagebox

def calculate1() :

    pat1=pata.get()
    st1=sta.get()
    sa1=saa.get()
    var1=vara.get()
    name1=namea.get()

    if var1=="" or name1=="" or st1=="" or sa1=="" or pat1=="" :
        tkinter.messagebox.showinfo("MESSAGEBOX","PLEASE FILL ALL THE FIELDS.")

    pat1=float(pat1)
    st1=int(st1)
    sa1=int(sa1)
    i=0
    a=(sa1/st1)*100

    if pat1!=a :
        tkinter.messagebox.showinfo("MESSAGEBOX", ("PLEASE","ENTER","CORRECT","DATA",",","YOUR","NUMBERS","AREN'T","ADDING","UP","TO","YOUR","PRESENT","ATTENDANCE","."))

    if pat1==a :
        while a<75 :
            a=((sa1+1)/(st1+1))*100
            sa1=sa1+1
            st1=st1+1
            i=i+1

        if i!=0 :
            tkinter.messagebox.showinfo("MESSAGEBOX", (
            "HELLO", name1.upper(), "!", "YOU", "HAVE", "TO", "ATTEND", i , var1, "CLASSES", "TO", "GET", "75%",
            "ATTENDENCE", "GOOD", "LUCK!"))

        elif  pat1==75 :

            tkinter.messagebox.showinfo("MESSAGEBOX",("CONGRATS", name1.upper(),"!", "YOUR","ATTENDANCE","IN",var1,"IS","ALREADY","EQUAL","TO","75%."))

        elif  pat1>75 :

            tkinter.messagebox.showinfo("MESSAGEBOX",("CONGRATS", name1.upper(),"!", "YOUR","ATTENDANCE","IN",var1,"IS","ALREADY","ABOVE","75%."))


def calculate2() :
    ts2 = tsb.get()
    sa2 = sab.get()
    var2 = varb.get()
    name2 = nameb.get()
    sta2=stab.get()

    if var2=="" or name2=="" or ts2=="" or sa2=="" or sta2=="" :
        tkinter.messagebox.showinfo("MESSAGEBOX","PLEASE FILL ALL THE FIELDS")

    ts2 = int(ts2)
    sa2 = int(sa2)
    sta2= int(sta2)

    fa= ((sa2+sta2)/ts2)*100

    tkinter.messagebox.showinfo("MESSAGEBOX",("YOUR","ATTENDANCE","IN",var2,"AT","THE","END","OF","THE","SEM","WILL","BE",fa))

def clear1() :
    entry1.delete("0","20")
    entry3.delete("0","20")
    entry5.delete("0","20")
    entry6.delete("0","20")
    entry7.delete("0","20")
    entry8.delete("0","20")
    entry2.delete("0","20")
    entry9.delete("0","20")
    vara.set("")
    varb.set("")


root=Tk()


root.title("ATTENDANCE CALCULATOR")

label1= Label(root,text="ATTENDENCE TO 75%",font=("Times New Roman",20))
label1.grid(row=0,column=0,sticky=W)

label2= Label(root,text="NAME",font=("Times New Roman",15))
label2.grid(row=2,column=0,sticky=W)

label3= Label(root,text="CURRENT ATTENDACE(%)",font=("Times New Roman",15))
label3.grid(row=4,column=0,sticky=W)

label4= Label(root,text="SELECT SUBJECT",font=("Times New Roman",15))
label4.grid(row=3,column=0,sticky=W)

label25= Label(root,text="NO OF CLASSES DONE",font=("Times New Roman",15))
label25.grid(row=5,column=0,sticky=W)

label26= Label(root,text="NO OF CLASSES ATTENDED",font=("Times New Roman",15))
label26.grid(row=6,column=0,sticky=W)


namea=StringVar()
pata=StringVar()
sta=StringVar()
saa=StringVar()
entry1= Entry(root,textvariable=namea)
entry2= Entry(root,textvariable=pata)
entry7= Entry(root,textvariable=sta)
entry8= Entry(root,textvariable=saa)
entry1.grid(row=2,column=1)
entry2.grid(row=4,column=1)
entry7.grid(row=5,column=1)
entry8.grid(row=6,column=1)


vara=StringVar()
sub1=OptionMenu(root,vara,"MATHS","PHYSICS","CHEMISTRY","COMPUTER PROGRAMING","ENVIRONMENTAL SCIENCE","ENGINEERING GRAPHICS","WORKSHOP","ENGLISH","ENGLISH LAB","ENGINEERING GRAPHICS LAB","WORKSHOP LAB")
sub1.configure(font=("Times New Roman",15))
sub1.grid(row=3,column=1)

cal1=Button(root,text="CALCULATE",font=("Times New Roman",15))
cal1.configure(command=calculate1)
cal1.grid(row=9,column=0)

label7= Label(root,text="   ||   ",font=25)
label7.grid(row=1,column=3)

label8= Label(root,text="   ||   ",font=25)
label8.grid(row=2,column=3)

label9= Label(root,text="   ||   ",font=25)
label9.grid(row=3,column=3)

label10= Label(root,text="   ||   ",font=25)
label10.grid(row=4,column=3)

label11= Label(root,text="   ||   ",font=25)
label11.grid(row=5,column=3)

label12= Label(root,text="   ||   ",font=25)
label12.grid(row=6,column=3)

label22= Label(root,text="   ||   ",font=25)
label22.grid(row=7,column=3)

label23= Label(root,text="   ||   ",font=25)
label23.grid(row=8,column=3)

label21= Label(root,text="   ||   ",font=25)
label21.grid(row=0,column=3)

label24= Label(root,text="   ||   ",font=25)
label24.grid(row=9,column=3)

label28= Label(root,text="   ||   ",font=25)
label28.grid(row=10,column=3)


label13= Label(root,text="ATTENDANCE(%) AT SEM END",font=("Times New Roman",20))
label13.grid(row=0,column=4,sticky=W)

label14= Label(root,text="NAME",font=("Times New Roman",15))
label14.grid(row=2,column=4,sticky=W)

label15= Label(root,text="CURRENT ATTENDACE(%)",font=("Times New Roman",15))
label15.grid(row=4,column=4,sticky=W)

label16= Label(root,text="SELECT SUBJECT",font=("Times New Roman",15))
label16.grid(row=3,column=4,sticky=W)

label17= Label(root,text="TOTAL CLASSES IN THAT SEM",font=("Times New Roman",15))
label17.grid(row=4,column=4,sticky=W)

label27= Label(root,text="NO OF CLASSES ATTENDED",font=("Times New Roman",15))
label27.grid(row=5,column=4,sticky=W)

label18= Label(root,text="NO OF CLASSES YOU WILL ATTEND",font=("Times New Roman",15))
label18.grid(row=6,column=4,sticky=W)

nameb=StringVar()
patb=StringVar()
tsb=StringVar()
sab=StringVar()
stab=StringVar()

entry3= Entry(root,textvariable=nameb)
entry5= Entry(root,textvariable=tsb)
entry6= Entry(root,textvariable=sab)
entry9= Entry(root,textvariable=stab)
entry3.grid(row=2,column=5)
entry5.grid(row=4,column=5)
entry6.grid(row=5,column=5)
entry9.grid(row=6,column=5)

varb=StringVar()
sub2=OptionMenu(root,varb,"MATHS","PHYSICS","CHEMISTRY","COMPUTER PROGRAMING","ENVIRONMENTAL SCIENCE","ENGINEERING GRAPHICS","WORKSHOP","ENGLISH","ENGLISH LAB","ENGINEERING GRAPHICS LAB","WORKSHOP LAB")
sub2.configure(font=("Times New Roman",15))
sub2.grid(row=3,column=5)

cal2=Button(root,text="CALCULATE",font=("Times New Roman",15))
cal2.configure(command=calculate2)
cal2.grid(row=9,column=4)

clear=Button(root,text="CLEAR",font=("Times New Roman",15))
clear.configure(command=clear1)
clear.grid(row=11,column=3)

root.mainloop()

