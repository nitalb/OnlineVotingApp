import cx_Oracle
dsn_tns = cx_Oracle.makedsn('10.1.0.177', 1521, 'xe')
con=cx_Oracle.connect('nehanital','nehanital',dsn_tns)
from tkinter import messagebox
from tkinter import *
top = Tk()
top.title('Client')
top.geometry("500x500")
top.configure(bg='White')
top.anchor(CENTER)
cur=con.cursor()
global radiovar
radiovar=IntVar()
def strtele():
    def val():
        if(uidtb.get()=="admin" and pwdtb.get()=="admin"):
            admin.destroy()
            regbtn.config(state=DISABLED)
            signin.config(state=NORMAL)
        else:
            uidtb.delete(first=0,last='end')
            pwdtb.delete(first=0,last='end')
            Label(admin,text="Invalid Id or Password", fg="Red").grid(row=7,column=1)
    admin=Toplevel()
    admin.configure(bg='White')
    Label(admin,text="UserName:",font=("TIMES NEW ROMAN",12),bg="White",bd=10,height=3,width=15).grid(row=1,column=1)
    uidtb=Entry(admin, bd=5, width=50)
    uidtb.grid(row=1,column=3)
    Label(admin,text="Password:",font=("TIMES NEW ROMAN",12),bg="White",bd=10,height=3,width=15).grid(row=3,column=1)
    pwdtb=Entry(admin, show="*", bd=5, width=50)
    pwdtb.grid(row=3,column=3)
    Label(admin, text="Election:",font=("TIMES NEW ROMAN",12),bg="White",bd=10,height=3,width=15).grid(row=5, column=1,rowspan=2)
    radiovar.set(1)
    R1=Radiobutton(admin,text="Ladies Representative", variable=radiovar, value=1, font=("TIMES NEW ROMAN",12), bg="White")
    R2=Radiobutton(admin,text="General Secretary", variable=radiovar, value=2, font=("TIMES NEW ROMAN",12), bg="White")
    R1.grid(row=5, column=2,rowspan=2,columnspan=2)
    R2.grid(row=5, column=4,rowspan=2, columnspan=2)
    Button(admin,text="Validate",command=val,font=("TIMES NEW ROMAN",12),bg="coral1",bd=10,height=2,width=15).grid(row=7,column=2,columnspan=2)

def strtreg():
    def val():
        if(uidtb.get()=="admin" and pwdtb.get()=="admin"):
            admin.destroy()
            signin.config(state=DISABLED)
            regbtn.config(state=NORMAL)
        else:
            uidtb.delete(first=0,last='end')
            pwdtb.delete(first=0,last='end')
            Label(admin,text="Invalid Id or Password", fg="Red").grid(row=7,column=1)
    admin=Tk()
    admin.configure(bg='White')
    Label(admin,text="UserName:",font=("TIMES NEW ROMAN",12),bg="White",bd=10,height=3,width=15).grid(row=1,column=1)
    uidtb=Entry(admin,bd=5, width=50)
    uidtb.grid(row=1,column=3)
    Label(admin,text="Password:",font=("TIMES NEW ROMAN",12),bg="White",bd=10,height=3,width=15).grid(row=3,column=1)
    pwdtb=Entry(admin, show="*",bd=5, width=50)
    pwdtb.grid(row=3,column=3)
    Button(admin,text="Validate",command=val,font=("TIMES NEW ROMAN",12),bg="coral1",bd=10,height=2,width=15).grid(row=5,column=2,columnspan=2)

def stpreg():
    def val():
        if(uidtb.get()=="admin" and pwdtb.get()=="admin"):
            admin.destroy()
            regbtn.config(state=DISABLED)
        else:
            uidtb.delete(first=0,last='end')
            pwdtb.delete(first=0,last='end')
            Label(admin,text="Invalid Id or Password", fg="Red").grid(row=7,column=1)
    admin=Tk()
    admin.configure(bg='White')
    Label(admin,text="UserName:",font=("TIMES NEW ROMAN",12),bg="White",bd=10,height=3,width=15).grid(row=1,column=1)
    uidtb=Entry(admin,bd=5, width=50)
    uidtb.grid(row=1,column=3)
    Label(admin,text="Password:",font=("TIMES NEW ROMAN",12),bg="White",bd=10,height=3,width=15).grid(row=3,column=1)
    pwdtb=Entry(admin, show="*",bd=5, width=50)
    pwdtb.grid(row=3,column=3)
    Button(admin,text="Validate",command=val,font=("TIMES NEW ROMAN",12),bg="coral1",bd=10,height=2,width=15).grid(row=5,column=2,columnspan=2)

def stpele():
    def val():
        if(uidtb.get()=="admin" and pwdtb.get()=="admin"):
            admin.destroy()
            signin.config(state=DISABLED)
        else:
            uidtb.delete(first=0,last='end')
            pwdtb.delete(first=0,last='end')
            l= Label(admin,text="Invalid Id or Password", fg="Red")
            l.grid(row=7,column=1,columnspan=2)
    admin=Tk()
    admin.configure(bg='White')
    Label(admin,text="UserName:",font=("TIMES NEW ROMAN",12),bg="White",bd=10,height=3,width=15).grid(row=1,column=1)
    uidtb=Entry(admin,bd=5, width=50)
    uidtb.grid(row=1,column=3)
    Label(admin,text="Password:",font=("TIMES NEW ROMAN",12),bg="White",bd=10,height=3,width=15).grid(row=3,column=1)
    pwdtb=Entry(admin, show="*",bd=5, width=50)
    pwdtb.grid(row=3,column=3)
    Button(admin,text="Validate",command=val,font=("TIMES NEW ROMAN",12),bg="coral1",bd=10,height=2,width=15).grid(row=5,column=2,columnspan=2)

def Reg():
    for child in top.winfo_children():
        child.grid_forget()
    top.geometry("1000x1000")
    branch = StringVar()
    top.title('Registration')
    gender=StringVar()
    Label(top,text="Name:",font=("TIMES NEW ROMAN",12),bg="White",bd=10,height=3,width=15).grid(row=1,column=1)
    nmtb=Entry(top, bd=5)
    nmtb.grid(row=1,column=2)
    Label(top,text="Branch:",font=("TIMES NEW ROMAN",12),bg="White",bd=10,height=3,width=15).grid(row=2,column=1)
    Label(top,text="Expected Passing year:",font=("TIMES NEW ROMAN",12),bg="White",bd=10,height=3,width=15).grid(row=4,column=1)
    yeartb=Entry(top, bd=5)
    yeartb.grid(row=4,column=2)
    branch.set("Computer Science and Engineering")
    BR1= Radiobutton(top, text="Computer Science and Engineering", variable= branch ,  value = "Computer Science and Engineering", font=("TIMES NEW ROMAN",12), bg="White")
    BR2= Radiobutton(top, text="Civil Engineering", variable= branch ,  value = "Civil Engineering", font=("TIMES NEW ROMAN",12), bg="White")
    BR3= Radiobutton(top, text="Information Technology", variable= branch ,  value = "Information Technology", font=("TIMES NEW ROMAN",12), bg="White")
    BR4= Radiobutton(top, text="Mechanical Engineering", variable= branch ,  value = "Mechanical Engineering", font=("TIMES NEW ROMAN",12), bg="White")
    BR5= Radiobutton(top, text="Electronics Engineering", variable= branch ,  value = "Electronics Engineering", font=("TIMES NEW ROMAN",12), bg="White")
    BR1.grid(row=2,column=2)
    BR2.grid(row=2,column=3)
    BR3.grid(row=3,column=2)
    BR4.grid(row=3,column=3)
    BR5.grid(row=2,column=4)
    Label(top,text="Gender",font=("TIMES NEW ROMAN",12),bg="White",bd=10,height=3,width=15).grid(row=5,column=1)
    Label(top,text="UserId",font=("TIMES NEW ROMAN",12),bg="White",bd=10,height=3,width=15).grid(row=6,column=1)
    Label(top,text="Password",font=("TIMES NEW ROMAN",12),bg="White",bd=10,height=3,width=15).grid(row=7,column=1)
    gender.set("Male")
    GR1 = Radiobutton(top, text="Male", variable= gender ,  value = "Male", font=("TIMES NEW ROMAN",12), bg="White")
    GR2 = Radiobutton(top, text="Female", variable= gender, value = "Female", font=("TIMES NEW ROMAN",12), bg="White")
    GR1.grid(row=5,column=2)
    GR2.grid(row=5,column=3)
    uidtb=Entry(top, bd=5)
    pwdtb=Entry(top, bd=5, show="*")
    uidtb.grid(row=6,column=2)
    pwdtb.grid(row=7,column=2)
    def VoterDetail():
        name=nmtb.get()
        cur.execute("insert into Voter values('"+name+"','"+yeartb.get()+"','"+gender.get()+"','"+branch.get()+"','"+uidtb.get()+"','"+pwdtb.get()+"',0)")
        cur.execute("commit")
        nmtb.delete(first=0,last='end')
        yeartb.delete(first=0,last='end')
        uidtb.delete(first=0,last='end')
        pwdtb.delete(first=0,last='end')
        messagebox.showinfo("Success", "You are registered successfully.")
        for child in top.winfo_children():
            child.grid_forget()
        regbtn=Button(top,text="Register Here",state=DISABLED, command=Reg,font=("TIMES NEW ROMAN",12),bg="coral1",bd=10,height=5,width=15)
        regbtn.grid(row=1,column=1,rowspan=2)
        signin=Button(top,text="Sign In", command=Signin, state=DISABLED,font=("TIMES NEW ROMAN",12),bg="coral1",bd=10,height=5,width=15)
        signin.grid(row=3,column=1,rowspan=2)
        top.geometry("500x500")
        regbtn.configure(state=NORMAL)

    submitbtn=Button(top,text="Submit", command=VoterDetail,font=("TIMES NEW ROMAN",12),bg="coral1",bd=10,height=3,width=15);
    submitbtn.grid(row=9,column=2,rowspan=2)

def Signin():
    uid=''
    si=Toplevel()
    si.configure(bg='White')
    uid=Label(si, text="User ID",font=("TIMES NEW ROMAN",12),bg="White",bd=10,height=3,width=15)
    uidtb=Entry(si,bd=5, width=50)
    uid.grid(row=1,column=1,rowspan=2)
    uidtb.grid(row=1,column=2,rowspan=2)
    pwd=Label(si, text="Password",font=("TIMES NEW ROMAN",12),bg="White",bd=10,height=3,width=15)
    pwdtb=Entry(si,show="*",bd=5, width=50)
    pwd.grid(row=3,column=1,rowspan=2)
    pwdtb.grid(row=3,column=2,rowspan=2)
    def Votedb(nam):
        name=nam.get()
        cur1=con.cursor()
        cur1.execute("select count from Candidate where name='"+name+"'")
        for results in cur1:
            for c in results:
                count=c
                count=count+1 ;
                cur.execute("update Candidate set count=" + str(count) + " where name='" +name+"'")
                cur.execute("commit")
                print(radiovar.get(),uidtb.get())
        if(radiovar.get()==1):
            cur1.execute("update voter set logincount=1 where userid='"+uidtb.get()+"'")
            cur1.execute("commit")
        else:
            cur1.execute("update GSvoter set logincount=1 where userid='"+uidtb.get()+"'")
            cur1.execute("commit")
        si.forget(si);

    def Vote():
        candname=[]
        uid=uidtb.get()
        vote_to = StringVar()
        if(radiovar.get()==1):
            pd=' '
            g=''
            sc=''
            cur1=con.cursor()
            cur1.execute("select password,logincount,gender from Voter where userid='"+uidtb.get()+"'")
            for password,logincount,gender in cur1:
                pd=password
                sc=logincount
                g=gender
            if(pwdtb.get()==pd and sc==0 and g=='Female'):
                for child in si.winfo_children():
                    child.grid_forget()
                cur1.execute("select name from Candidate where election='Ladies Representative'")
                r=2
                for name in cur1:
                    for nm in name:
                        candname.append(Radiobutton(si,variable=vote_to, value=nm, text=nm, font=("TIMES NEW ROMAN",12), bg="White"))
                        candname[len(candname)-1].grid(row=r, column=1)
                        r+=1
                cast=Button(si,text="Cast Vote",font=("TIMES NEW ROMAN",12),bg="coral1",bd=10,height=3,width=15, command=lambda vote_to=vote_to:Votedb(vote_to))
                cast.grid(row=r,column=1,rowspan=2,columnspan=2)

            else:
                if(sc!=0 or g!='Female'):
                    messagebox.showinfo("Error","You already casted your vote or you cannot vote for this election",icon='warning')
                    si.forget(si)
                else:
                    print("error")
                    messagebox.showinfo("Error","Invalid userid or password ",icon='warning')
                    uidtb.delete(first=0,last='end')
                    pwdtb.delete(first=0,last='end')
        elif(radiovar.get()==2):
            pd=' '
            vote_to=StringVar()
            cur1=con.cursor()
            cur1.execute("select password,logincount from GSVoter where userid='"+uidtb.get()+"'")
            for password,logincount in cur1:
                pd=password
                sc=logincount
            if(pwdtb.get()==pd and sc==0):
                for child in si.winfo_children():
                    child.grid_forget()
                cur1.execute("select name from Candidate where election='General Secretary'")
                r=2
                for name in cur1:
                    for nm in name:
                        candname.append(Radiobutton(si,variable=vote_to, value=nm, text=nm, font=("TIMES NEW ROMAN",12), bg="White"))
                        candname[len(candname)-1].grid(row=r, column=1)
                        r+=1
                cast=Button(si,text="Cast Vote",font=("TIMES NEW ROMAN",12),bg="coral1",bd=10,height=5,width=15, command=lambda vote_to=vote_to:Votedb(vote_to))
                cast.grid(row=r,column=1,rowspan=2,columnspan=2)

            else:
                if(sc!=0):
                    messagebox.showinfo("Error","You already casted your vote",icon='warning')
                    si.forget(si)
                else:
                    print("error")
                    messagebox.showinfo("Error","Invalid userid or password ",icon='warning')
                    uidtb.delete(first=0,last='end')
                    pwdtb.delete(first=0,last='end')
    signinbtn=Button(si,text="Sign In", command=Vote,font=("TIMES NEW ROMAN",12),bg="coral1",bd=10,height=5,width=15)
    signinbtn.grid(row=5,column=1,rowspan=2)

menubar=Menu(top);
ActionMenu=Menu(menubar,tearoff=0,font=50,bg="White")
ActionMenu.add_command(label='Start Registration',command=strtreg)
ActionMenu.add_command(label='Start Election',command=strtele)
ActionMenu.add_command(label='Stop Registration',command=stpreg)
ActionMenu.add_command(label='Stop Election',command=stpele)
ActionMenu.add_separator()
ActionMenu.add_command(label="Exit", command=top.quit)
regbtn=Button(top,text="Register Here",state=DISABLED, command=Reg,font=("TIMES NEW ROMAN",12),bg="coral1",bd=10,height=5,width=15)
regbtn.grid(row=1,column=1,rowspan=2)
signin=Button(top,text="Sign In", command=Signin, state=DISABLED,font=("TIMES NEW ROMAN",12),bg="coral1",bd=10,height=5,width=15)
signin.grid(row=3,column=1,rowspan=2)
menubar.add_cascade(label="Action", menu=ActionMenu)
top.resizable(width=False, height=False)
top.config(menu=menubar);
top.mainloop()
