

def savedata():

    print(Name.get())
    print(Lastname.get()) 
    print(Amt_Withdrawn.get())
    print(Amt_Remaning.get())
    print(Reason.get())
    print(Date.get())
    print(Time.get())

    fullrow = [Name.get(), Lastname.get(),Amt_Withdrawn.get(), Amt_Remaning.get(), Reason.get(), Date.get(), Time.get()]
    sheet01.append_row(fullrow)

    saveddata.set(f'Thank you Mr./Ms. {Name.get()}. Your data has been updated')

from tkinter import *
screen=Tk()
screen.title('Bank of the World')
Label(text="UserName:")
UserName=Entry()
UserName.pack()
Label(text="Pincode=     ")
Pincode=Entry()
Pincode.pack()
Label(text="Name:  ").pack()
Name=Entry()
Name.pack()
Label(text="Lastname  ").pack()
Lastname=Entry()
Lastname.pack()
Label(text="Amt_Withdrawn:   ").pack()
Amt_Withdrawn=Entry()
Amt_Withdrawn.pack()
Label(text="Amt.Remaning:   ").pack()
Amt_Remaning=Entry()
Amt_Remaning.pack()
Label(text="Reason:    ").pack()
Reason=Entry()
Reason.pack()
Label(text="Date:    ").pack()
Date=Entry()
Date.pack()
Label(text="Time:    ").pack()
Time=Entry()
Time.pack()
Button(text="Submit",command=savedata).pack()


saveddata=StringVar()
Label(text="",textvariable=saveddata).pack()


screen.mainloop()