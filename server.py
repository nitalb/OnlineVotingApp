import cx_Oracle
con=cx_Oracle.connect('nehanital/nehanital@10.1.0.177/xe')
cur=con.cursor()
from tkinter import messagebox
from tkinter import *

top = Tk()
top.configure(bg='White')
top.anchor(CENTER)
def Reset():
    cur.execute("update voter set logincount=0")
    cur.execute("commit")
    cur.execute("update gsvoter set logincount=0")
    cur.execute("commit")
    cur.execute("delete from Candidate")
    cur.execute("commit")

def Hisdata():
    candname=[]
    votecount=[]
    top.anchor(N)
    top.geometry("600x500")
    top.title('Past Elections')
    def hist():
        cur.execute("select name, branch, election ,count from History where curr_year='"+yeartb.get()+"' and election='"+election.get()+"'order by count desc")
        r=6
        c=1

        if(election.get()=='General Secretary'):
            tname=Label(top, text="Name", font=("TIMES NEW ROMAN",12),bg="White",bd=10,height=1,width=15).grid(row=5,column=1)
            telt=Label(top, text="Count", font=("TIMES NEW ROMAN",12),bg="White",bd=10,height=1,width=15).grid(row=5,column=2)
            cur.execute("select name,count from history where election='General Secretary' and curr_year='"+yeartb.get()+"' order by count desc")
            for name, count in cur :
                candname.append(Label(top, text= name , font=("TIMES NEW ROMAN",12),bg="White",bd=10,height=1,width=15))
                candname[len(candname)-1].grid(row=r,column=c)
                c+=1
                votecount.append(Label(top, text=count, font=("TIMES NEW ROMAN",12),bg="White",bd=10,height=1,width=15))
                votecount[len(candname)-1].grid(row=r,column=c)
                c-=1
                r+=1
        elif(election.get()=="Ladies Representative"):
            tname=Label(top, text="Year", font=("TIMES NEW ROMAN",12),bg="White",bd=10,height=1,width=15).grid(row=5,column=1)
            telt=Label(top, text="Count", font=("TIMES NEW ROMAN",12),bg="White",bd=10,height=1,width=15).grid(row=5,column=2)
            cur.execute("select name,count from history where election='Ladies Representative' and curr_year='"+yeartb.get()+"' order by count desc")
            for name, count in cur :
                candname.append(Label(top, text= name , font=("TIMES NEW ROMAN",12),bg="White",bd=10,height=1,width=15))
                candname[len(candname)-1].grid(row=r,column=c)
                c+=1
                votecount.append(Label(top, text=count, font=("TIMES NEW ROMAN",12),bg="White",bd=10,height=1,width=15))
                votecount[len(candname)-1].grid(row=r,column=c)
                c-=1
                r+=1
    for child in top.winfo_children():
        child.grid_forget()
    election=StringVar()
    Button(top,text="Home",font=("TIMES NEW ROMAN",12),bg="White",bd=10,height=2,width=10,command=Home).grid(row=0,column=7)
    year=Label(top,text="Year:",font=("TIMES NEW ROMAN",12),bg="White",bd=10,height=3,width=15)
    year.grid(row=1,column=1)
    yeartb=Entry(top,width=15, bd=5)
    yeartb.grid(row=1,column=2)
    election.set("General Secretary")
    Label(top,text="Election:",font=("TIMES NEW ROMAN",12),bg="White",bd=10,height=3,width=15).grid(row=2,column=1)
    election.set("General Secretary")
    R1 = Radiobutton(top, text="General Secretary", variable= election ,  value = "General Secretary", font=("TIMES NEW ROMAN",12), bg="White")
    R2 = Radiobutton(top, text="Ladies Representative", variable= election, value = "Ladies Representative", font=("TIMES NEW ROMAN",12), bg="White")
    Button(top,text="OK",font=("TIMES NEW ROMAN",12),bg="White",bd=10,height=2,width=10,command=hist).grid(row=4,column=2)
    R1.grid(row=2,column=2)
    R2.grid(row=2,column=3)

def Home():
    for child in top.winfo_children():
        child.grid_forget()
    top.title('Home')
    top.geometry("800x600")
    top.anchor(CENTER)
    count=Button(top,text="Count", command=Count,font=("TIMES NEW ROMAN",12),bg="coral1",bd=10,height=5,width=30)
    addc=Button(top,text='Add Candidate Details', command=AddCandidate,font=("TIMES NEW ROMAN",12),bg="coral1",bd=10,height=5,width=30)
    delc=Button(top,text="Delete Candidates", command=DeleteCandidates,font=("TIMES NEW ROMAN",12),bg="coral1",bd=10,height=5,width=30)
    delv=Button(top, text="Delete Voter Details", command=DeleteVoters,font=("TIMES NEW ROMAN",12),bg="coral1",bd=10,height=5,width=30)
    gsv=Button(top,text="Add Voters for General Secretary" ,command=GSVoter,font=("TIMES NEW ROMAN",12),bg="coral1",bd=10,height=5,width=30)
    rtrvhis = Button(top,text="Retrieve Election Data of Past Years" ,command=Hisdata,font=("TIMES NEW ROMAN",12),bg="coral1",bd=10,height=5,width=30)
    view=Button(top,text="View Voters Registered", command=viewvoters, font=("TIMES NEW ROMAN",12),bg="coral1",bd=10,height=5,width=30 )
    addhist=Button(top,text="Add Election Data to Backup", command=History, font=("TIMES NEW ROMAN",12),bg="coral1",bd=10,height=5,width=30)
    count.grid(row=1,column=1,columnspan=2,rowspan=2)
    addc.grid(row=3,column=6,columnspan=2,rowspan=1)
    delc.grid(row=5,column=1,columnspan=2,rowspan=2)
    delv.grid(row=1,column=6,columnspan=2,rowspan=1)
    gsv.grid(row=3,column=1,columnspan=2,rowspan=2)
    rtrvhis.grid(row=5,column=6,columnspan=2,rowspan=1)
    view.grid(row=7,column=1,columnspan=2,rowspan=2)
    addhist.grid(row=7,column=6,columnspan=2,rowspan=2)

def viewvoters():
    CheckVar1 = IntVar()
    CheckVar2 = IntVar()
    for child in top.winfo_children():
        child.grid_forget()
    l=[]
    top.geometry("1000x600")
    top.anchor(N)
    top.title('Voters Registered')
    top2=Canvas(top, height=300, width=900, confine=FALSE, bg='White')
    top1=Frame(top2,bg="White")
    vbar=Scrollbar(top,orient=VERTICAL, bg='WHITE', troughcolor='WHITE')
    vbar.grid(column=16,row=8,sticky=NS)
    top2.config(yscrollcommand=vbar.set)
    top2.create_window(0,0,window=top1, anchor=NW)
    vbar.config(command=top2.yview)
    top2.grid(column=0,row=8,columnspan=15)
    Button(top,text="Home",font=("TIMES NEW ROMAN",12),bg="White",bd=10,height=2,width=10,command=Home).grid(row=0,column=12)
    def DisplayV():
        cur1=con.cursor()
        if(CheckVar1.get()==1 and CheckVar2.get()==0):
            r=7
            i=5
            cur1.execute(" select distinct gsvoter.name,gsvoter.gender,gsvoter.branch,gsvoter.post,voter.year from gsVoter, voter where gsvoter.name=voter.name" )
            for(name,gender,branch,post,year) in cur1:
                l.append(Label(top1,text=name,font=("TIMES NEW ROMAN",12),bg="White",bd=10,height=3,width=15))
                l[i].grid(row=r,column=1)
                i+=1
                l.append(Label(top1,text=gender,font=("TIMES NEW ROMAN",12),bg="White",bd=10,height=3,width=15))
                l[i].grid(row=r,column=2)
                i+=1
                l.append(Label(top1,text=branch,font=("TIMES NEW ROMAN",12),bg="White",bd=10,height=3,width=25))
                l[i].grid(row=r,column=3,columnspan=10)
                i+=1
                l.append(Label(top1,text=year,font=("TIMES NEW ROMAN",12),bg="White",bd=10,height=3,width=15))
                l[i].grid(row=r,column=14)
                i+=1
                l.append(Label(top1,text=post ,font=("TIMES NEW ROMAN",12),bg="White",bd=10,height=3,width=15))
                l[i].grid(row=r,column=15)
                r+=1
                i+=1
            top2.configure(scrollregion=top2.bbox("all"))
        elif(CheckVar1.get()==0 and CheckVar2.get()==1):
            cur1.execute(" select distinct voter.name,voter.gender,voter.branch,voter.year from Voter where voter.gender='Female'" )
            r=7
            i=5
            for(name,gender,branch,year) in cur1:
                l.append(Label(top1,text=name,font=("TIMES NEW ROMAN",12),bg="White",bd=10,height=3,width=15))
                l[i].grid(row=r,column=1)
                i+=1
                l.append(Label(top1,text=gender,font=("TIMES NEW ROMAN",12),bg="White",bd=10,height=3,width=15))
                l[i].grid(row=r,column=2)
                i+=1
                l.append(Label(top1,text=branch,font=("TIMES NEW ROMAN",12),bg="White",bd=10,height=3,width=25))
                l[i].grid(row=r,column=3,columnspan=10)
                i+=1
                l.append(Label(top1,text=year,font=("TIMES NEW ROMAN",12),bg="White",bd=10,height=3,width=15))
                l[i].grid(row=r,column=14)
                r+=1
                i+=1
            top2.configure(scrollregion=top2.bbox("all"))
        elif(CheckVar1.get()==1 and CheckVar2.get()==1):
            r=7
            i=5
            cur1.execute(" select distinct voter.name,voter.gender,voter.branch,voter.year,gsvoter.post from Voter FULL OUTER JOIN GSVoter on voter.name=gsvoter.name")
            for(name,gender,branch,year,post) in cur1:
                l.append(Label(top1,text=name,font=("TIMES NEW ROMAN",12),bg="White",bd=10,height=3,width=15))
                l[i].grid(row=r,column=1)
                i+=1
                l.append(Label(top1,text=gender,font=("TIMES NEW ROMAN",12),bg="White",bd=10,height=3,width=15))
                l[i].grid(row=r,column=2)
                i+=1
                l.append(Label(top1,text=branch,font=("TIMES NEW ROMAN",12),bg="White",bd=10,height=3,width=25))
                l[i].grid(row=r,column=3,columnspan=10)
                i+=1
                l.append(Label(top1,text=year,font=("TIMES NEW ROMAN",12),bg="White",bd=10,height=3,width=15))
                l[i].grid(row=r,column=14)
                i+=1
                l.append(Label(top1,text=post ,font=("TIMES NEW ROMAN",12),bg="White",bd=10,height=3,width=15))
                l[i].grid(row=r,column=15)
                r+=1
                i+=1
            top2.configure(scrollregion=top2.bbox("all"))
    l.append(Label(top1,text="Name",font=("TIMES NEW ROMAN",12),bg="White",bd=10,height=3,width=15))
    l[0].grid(row=5,column=1)
    l.append(Label(top1,text="Gender",font=("TIMES NEW ROMAN",12),bg="White",bd=10,height=3,width=15))
    l[1].grid(row=5,column=2)
    l.append(Label(top1,text="Branch",font=("TIMES NEW ROMAN",12),bg="White",bd=10,height=3,width=15))
    l[2].grid(row=5,column=3,columnspan=10)
    l.append(Label(top1,text="Expected year \nof passout",font=("TIMES NEW ROMAN",12),bg="White",bd=10,height=3,width=15))
    l[3].grid(row=5,column=14)
    l.append(Label(top1,text="Post in Student \nCouncil(if any)",font=("TIMES NEW ROMAN",12),bg="White",bd=10,height=3,width=15))
    l[4].grid(row=5,column=15)
    C1 = Checkbutton(top, text = "General Secretary", variable = CheckVar1,onvalue=1, offvalue=0 , font=("TIMES NEW ROMAN",12),bg="White",bd=10,height=3,width=15)
    C2 = Checkbutton(top, text = "Ladies Representative", variable = CheckVar2, onvalue=1, offvalue=0 , font=("TIMES NEW ROMAN",12),bg="White",bd=10,height=3,width=15)
    C1.grid(row=1, column=2)
    C2.grid(row=1, column=3)
    Election_type=Label(top, text="Election Type",font=("TIMES NEW ROMAN",12),bg="White",bd=10,height=3,width=15)
    Election_type.grid(row=1, column=1)
    Button(top,text="OK",font=("TIMES NEW ROMAN",12),bg="White",bd=10,height=2,width=10,command=DisplayV).grid(row=2,column=2)

def GSVoter():
    for child in top.winfo_children():
        child.grid_forget()
    top.geometry("850x600")
    top.title('GS Voters Details')
    branch = StringVar()
    gender=StringVar()
    Button(top,text="Home",font=("TIMES NEW ROMAN",12),bg="White",bd=10,height=2,width=10,command=Home).grid(row=0,column=7)
    Label(top,text="Name:",font=("TIMES NEW ROMAN",12),bg="White",bd=10,height=3,width=15).grid(row=1,column=1)
    nmtb=Entry(top, bd=5)
    nmtb.grid(row=1,column=2)
    Label(top,text="Branch:",font=("TIMES NEW ROMAN",12),bg="White",bd=10,height=3,width=15).grid(row=2,column=1)
    Label(top,text="Post:",font=("TIMES NEW ROMAN",12),bg="White",bd=10,height=3,width=15).grid(row=4,column=1)
    posttb=Entry(top, bd=5)
    posttb.grid(row=4,column=2)
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
    gender.set("Male")
    Label(top,text="Gender",font=("TIMES NEW ROMAN",12),bg="White",bd=10,height=3,width=15).grid(row=5,column=1)
    GR1 = Radiobutton(top, text="Male", variable= gender ,  value = "Male", font=("TIMES NEW ROMAN",12), bg="White")
    GR2 = Radiobutton(top, text="Female", variable= gender, value = "Female", font=("TIMES NEW ROMAN",12), bg="White")
    GR1.grid(row=5,column=2)
    GR2.grid(row=5,column=3)
    def CandidateDetail():
        name=nmtb.get()
        uid=''
        pwd=''
        cur.execute("Select userid, password from Voter where name='"+name+"'")
        for userid,password in cur:
            uid=userid
            pwd=password
        cur.execute("insert into GSVoter values('"+name+"','"+gender.get()+"','"+branch.get()+"','"+posttb.get()+"','"+uid+"','"+pwd+"',0)")
        cur.execute("commit")

        nmtb.delete(first=0,last='end')
        posttb.delete(first=0,last='end')
        messagebox.showinfo("Success", "You are registered successfully.")
    submitbtn=Button(top,text="Submit", command=CandidateDetail,font=("TIMES NEW ROMAN",12),bg="coral1",bd=10,height=3,width=15);
    submitbtn.grid(row=6,column=2,rowspan=2)

def DeleteCandidates():
    for child in top.winfo_children():
        child.grid_forget()
    top.anchor(N)
    top.title('Delete Candidates')
    top.geometry("800x500")
    Button(top,text="Home",font=("TIMES NEW ROMAN",12),bg="White",bd=10,height=2,width=10,command=Home).grid(row=0,column=7)
    CheckVar1 = IntVar()
    CheckVar2 = IntVar()
    def displaynames():
        tname=Label(top, text="Name", font=("TIMES NEW ROMAN",12),bg="White",bd=10,height=1,width=15).grid(row=4,column=0)
        telt=Label(top, text="Election_Type", font=("TIMES NEW ROMAN",12),bg="White",bd=10,height=1,width=15).grid(row=4,column=1)
        tdelb=Label(top, text=" ", font=("TIMES NEW ROMAN",12),bg="White",bd=10,height=1,width=15).grid(row=4,column=2)
        top2=Canvas(top, height=200, width=600, confine=FALSE, bg='White')
        top1=Frame(top2,bg="White")
        vbar=Scrollbar(top,orient=VERTICAL, bg='WHITE', troughcolor='WHITE')
        vbar.grid(column=5,row=8,sticky=NS)
        top2.config(yscrollcommand=vbar.set)
        top2.create_window(0,0,window=top1, anchor=NW)
        vbar.config(command=top2.yview)
        top2.grid(column=0,row=8,columnspan=6)
        candlist=[]
        candname=[]
        candelec=[]
        def find_in_grid(frame, r):
            for children in frame.children.values():
                info = children.grid_info()
                if len(info)!=0 and info["row"] == r:
                    return int(r)

        def deleterow(row):
            cur2=con.cursor()
            print(row)
            r=int(find_in_grid(top1, row))
            r=r-5
            cur2.execute("delete from Candidate where name='"+candname[r].cget("text")+"'")
            res=messagebox.askyesno("Confirmation","Are you sure you want to delete "+candname[r].cget("text")+"?",icon='warning')
            if(res==True):
                cur2.execute("commit")
                candname[r].grid_forget()
                candelec[r].grid_forget()
                candlist[r].grid_forget()

        if (CheckVar1.get()==1 and CheckVar2.get()==1) :
            r=5
            c=1
            cur.execute("select name from Candidate")
            for name in cur :
                for cn in name:
                    candname.append(Label(top1, text= cn , font=("TIMES NEW ROMAN",12),bg="White",bd=10,height=1,width=15))
                    candname[len(candname)-1].grid(row=r,column=c)
                    c+=1
                    cur1=con.cursor()
                    cur1.execute("select election from Candidate where name='"+cn+"'")
                    for election in cur1:
                        for el in election:
                            candelec.append(Label(top1, text= el, font=("TIMES NEW ROMAN",12),bg="White",bd=10,height=1,width=15))
                            candelec[len(candname)-1].grid(row=r,column=c)
                    c+=1
                    candlist.append(Button(top1, text="Delete" ,font=("TIMES NEW ROMAN",12), command=lambda r=r:deleterow(r),bg="coral1",bd=10,height=2,width=15,fg="White"))
                    candlist[len(candname)-1].grid(row=r,column=c)
                    r+=1
                    c-=2
            top2.configure(scrollregion=top2.bbox("all"))

        elif (CheckVar1.get()==1 and CheckVar2.get()==0):
            r=5
            c=1
            cur.execute("select name from Candidate where election='General Secretary'")
            for name in cur :
                for cn in name:
                    candname.append(Label(top1, text= cn , font=("TIMES NEW ROMAN",12),bg="White",bd=10,height=1,width=15))
                    candname[len(candname)-1].grid(row=r,column=c)
                    c+=1
                    cur1=con.cursor()
                    cur1.execute("select election from Candidate where name='"+cn+"'")
                    for election in cur1:
                        for el in election:
                            candelec.append(Label(top1, text= el, font=("TIMES NEW ROMAN",12),bg="White",bd=10,height=1,width=15))
                            candelec[len(candname)-1].grid(row=r,column=c)
                    c+=1
                    candlist.append(Button(top1, text="Delete" ,font=("TIMES NEW ROMAN",12),command=lambda r=r:deleterow(r),bg="coral1",bd=10,height=2,width=15,fg="White"))
                    candlist[len(candname)-1].grid(row=r,column=c)
                    r+=1
                    c-=2
            top2.configure(scrollregion=top2.bbox("all"))
        elif(CheckVar1.get()==0 and CheckVar2.get()==1):
            r=5
            c=1
            cur.execute("select name from Candidate where election='Ladies Representative'")
            for name in cur :
                for cn in name:
                    candname.append(Label(top1, text= cn , font=("TIMES NEW ROMAN",12),bg="White",bd=10,height=1,width=15))
                    candname[len(candname)-1].grid(row=r,column=c)
                    c+=1
                    cur1=con.cursor()
                    cur1.execute("select election from Candidate where name='"+cn+"'")
                    for election in cur1:
                        for el in election:
                            candelec.append(Label(top1, text= el, font=("TIMES NEW ROMAN",12),bg="White",bd=10,height=1,width=15))
                            candelec[len(candname)-1].grid(row=r,column=c)
                    c+=1
                    candlist.append(Button(top1, text="Delete" ,font=("TIMES NEW ROMAN",12), command=lambda r=r:deleterow(r),bg="coral1",bd=10,height=2,width=15,fg="White"))
                    candlist[len(candname)-1].grid(row=r,column=c)
                    r+=1
                    c-=2
            top2.configure(scrollregion=top2.bbox("all"))
    Election_type=Label(top, text="Election Type",font=("TIMES NEW ROMAN",12),bg="White",bd=10,height=3,width=15)
    Election_type.grid(row=1, column=0)
    C1 = Checkbutton(top, text = "General Secretary", variable = CheckVar1,onvalue=1, offvalue=0 , font=("TIMES NEW ROMAN",12),bg="White",bd=10,height=3,width=15)
    C2 = Checkbutton(top, text = "Ladies Representative", variable = CheckVar2, onvalue=1, offvalue=0 , font=("TIMES NEW ROMAN",12),bg="White",bd=10,height=3,width=15)
    delbutton=Button(top,text="OK", command=displaynames,font=("TIMES NEW ROMAN",12),bg="coral1",bd=10,height=3,width=15,fg="White")
    C1.grid(row=1, column=1)
    C2.grid(row=1, column=2)
    delbutton.grid(row=2, column=0,columnspan=2);
    def delall():
       cur.execute("delete from Candidate")
       result = messagebox.askquestion("Confirmation", "Are you sure you want to delete all data?", icon='warning')
       if result == 'yes':
           cur.execute("delete from Candidate")
           messagebox.showinfo("Success", "All Candidate details deleted successfully.")
           cur.execute("commit")
    delallbutton=Button(top, text="ALL", command=delall,font=("TIMES NEW ROMAN",12),bg="coral1",bd=10,height=3,width=15,fg="White").grid(row=2,column=1,columnspan=2)

def DeleteVoters():
    for child in top.winfo_children():
        child.grid_forget()
    top.title('Delete Voters')
    top.geometry("450x450")
    top.anchor(N)
    home=Button(top,text="Home",font=("TIMES NEW ROMAN",12),bg="White",bd=10,height=2,width=10,command=Home)
    home.grid(row=0,column=8)
    def delbatch():
        import datetime
        i = datetime.datetime.now()
        cur.execute("delete from Voter where year="+str(i.year))
        cur.execute("delete from GSVoter")
        res=messagebox.askyesno("Confirmation","Are you sure you want to delete the " +str(i.year)+" passout batch voter details?",icon='warning')
        if(res==True):
            cur.execute("commit")
    Button(top,text="Batch",command=delbatch,font=("TIMES NEW ROMAN",12),bg="coral1",bd=10,height=2,width=15,fg="White").grid(row=1,column=1)
    radiovar = StringVar()
    nmentry=Entry(top,state=DISABLED, bd=5)
    l=[]
    def rad():
        if(radiovar.get()=="select"):
            nmentry.config(state=NORMAL)
            okb.config(state=NORMAL)
    def details():
        namec=nmentry.get()
        okb.grid(row=3,column=3)
        def delselect():
            cur.execute("delete from Voter where name='"+namec+"'")
            cur.execute("commit")
            cur.execute("delete from GSVoter where name='"+namec+"'")
            cur.execute("commit")
            messagebox.showinfo("Success", "Voter details deleted successfully.")
            for i in range(0,10):
                l[i].grid_forget()
            dels.grid_forget()
            okb.grid(row=5,column=1)
        top.geometry("850x850")
        home.grid_forget()
        home.grid(row=0, column=15)
        cur1=con.cursor()
        cur1.execute(" select distinct voter.name,voter.gender,voter.branch,voter.year,gsvoter.post from Voter FULL OUTER JOIN GSVoter on voter.name=gsvoter.name where voter.name='"+namec+"'")
        l.insert(1,Label(top,text="Name",font=("TIMES NEW ROMAN",12),bg="White",bd=10,height=3,width=15))
        l[0].grid(row=5,column=1)
        l.insert(2,Label(top,text="Gender",font=("TIMES NEW ROMAN",12),bg="White",bd=10,height=3,width=15))
        l[1].grid(row=5,column=2)
        l.insert(3,Label(top,text="Branch",font=("TIMES NEW ROMAN",12),bg="White",bd=10,height=3,width=15))
        l[2].grid(row=5,column=3,columnspan=10)
        l.insert(4,Label(top,text="Expected year \nof passout",font=("TIMES NEW ROMAN",12),bg="White",bd=10,height=3,width=15))
        l[3].grid(row=5,column=14)
        l.insert(5,Label(top,text="Post in Student \nCouncil(if any)",font=("TIMES NEW ROMAN",12),bg="White",bd=10,height=3,width=15))
        l[4].grid(row=5,column=15)
        for(name,gender,branch,year,post) in cur1:
            l.insert(6,Label(top,text=name,font=("TIMES NEW ROMAN",12),bg="White",bd=10,height=3,width=15))
            l[5].grid(row=7,column=1)
            l.insert(7,Label(top,text=gender,font=("TIMES NEW ROMAN",12),bg="White",bd=10,height=3,width=15))
            l[6].grid(row=7,column=2)
            l.insert(8,Label(top,text=branch,font=("TIMES NEW ROMAN",12),bg="White",bd=10,height=3,width=25))
            l[7].grid(row=7,column=3,columnspan=10)
            l.insert(9,Label(top,text=year,font=("TIMES NEW ROMAN",12),bg="White",bd=10,height=3,width=15))
            l[8].grid(row=7,column=14)
            l.insert(10,Label(top,text=post ,font=("TIMES NEW ROMAN",12),bg="White",bd=10,height=3,width=15))
            l[9].grid(row=7,column=15)
            dels.configure(command=delselect)
            dels.grid(row=9,column=3,columnspan=2)
            nmentry.delete(first=0,last='end')
    R1 = Radiobutton(top, text="Select", variable= radiovar ,  value = "select", font=("TIMES NEW ROMAN",12),bg="White",bd=10,height=3,width=15, command=rad)
    R1.grid(row=2,column=1)
    Label(top,text="Name:",font=("TIMES NEW ROMAN",12),bg="White",bd=10,height=3,width=15).grid(row=3,column=1)
    nmentry.grid(row=3,column=2)
    okb=Button(top,text="OK",state=DISABLED,font=("TIMES NEW ROMAN",12),bg="coral1",bd=10,height=2,width=15,fg="White",command=details)
    okb.grid(row=5,column=1)
    dels=Button(top,text="Delete",font=("TIMES NEW ROMAN",12),bg="coral1",bd=10,height=3,width=15,fg="White")

def AddCandidate():
    for child in top.winfo_children():
        child.grid_forget()
    top.title('Add Candidates')
    Button(top,text="Home",font=("TIMES NEW ROMAN",12),bg="White",bd=10,height=2,width=10,command=Home).grid(row=0,column=7)
    top.geometry("850x600")
    branch = StringVar()
    election=StringVar()
    gender=StringVar()
    Label(top,text="Name:",font=("TIMES NEW ROMAN",12),bg="White",bd=10,height=3,width=15).grid(row=1,column=1)
    nmtb=Entry(top, bd=5, width=50)
    nmtb.grid(row=1,column=2,columnspan=2)
    Label(top,text="Branch:",font=("TIMES NEW ROMAN",12),bg="White",bd=10,height=3,width=15).grid(row=2,column=1)
    Label(top,text="Year:",font=("TIMES NEW ROMAN",12),bg="White",bd=10,height=3,width=15).grid(row=5,column=1)
    Label(top,text="Election:",font=("TIMES NEW ROMAN",12),bg="White",bd=10,height=3,width=15).grid(row=4,column=1)
    yeartb=Entry(top, bd=5)
    yeartb.grid(row=5,column=2)
    election.set("General Secretary")
    R1 = Radiobutton(top, text="General Secretary", variable= election ,  value = "General Secretary", font=("TIMES NEW ROMAN",12), bg="White")
    R2 = Radiobutton(top, text="Ladies Representative", variable= election, value = "Ladies Representative", font=("TIMES NEW ROMAN",12), bg="White")
    branch.set( "Computer Science and Engineering")
    BR1= Radiobutton(top, text="Computer Science and Engineering", variable= branch ,  value = "Computer Science and Engineering", font=("TIMES NEW ROMAN",12), bg="White")
    BR2= Radiobutton(top, text="Civil Engineering", variable= branch ,  value = "Civil Engineering", font=("TIMES NEW ROMAN",12), bg="White")
    BR3= Radiobutton(top, text="Information Technology", variable= branch ,  value = "Information Technology", font=("TIMES NEW ROMAN",12), bg="White")
    BR4= Radiobutton(top, text="Mechanical Engineering", variable= branch ,  value = "Mechanical Engineering", font=("TIMES NEW ROMAN",12), bg="White")
    BR5= Radiobutton(top, text="Electronics Engineering", variable= branch ,  value = "Electronics Engineering", font=("TIMES NEW ROMAN",12), bg="White")
    BR1.grid(row=2,column=4)
    BR2.grid(row=2,column=3)
    BR3.grid(row=3,column=2)
    BR4.grid(row=3,column=3)
    BR5.grid(row=2,column=2)
    R1.grid(row=4,column=2)
    R2.grid(row=4,column=3,columnspan=2)
    Label(top,text="Gender",font=("TIMES NEW ROMAN",12),bg="White",bd=10,height=3,width=15).grid(row=6,column=1)
    gender.set("Male")
    GR1 = Radiobutton(top, text="Male", variable= gender ,  value = "Male", font=("TIMES NEW ROMAN",12), bg="White")
    GR2 = Radiobutton(top, text="Female", variable= gender, value = "Female", font=("TIMES NEW ROMAN",12), bg="White")
    GR1.grid(row=6,column=2)
    GR2.grid(row=6,column=3)
    def CandidateDetail():
        name=nmtb.get()
        if(election.get()=="Ladies Representative" and gender.get()=="Male"):
            messagebox.showinfo("Err", "You cannot contest this election.", icon='warning')
            nmtb.delete(first=0,last='end')
            yeartb.delete(first=0,last='end')
        else:
            cur.execute("insert into Candidate values('"+name+"','"+election.get()+"','"+branch.get()+"',0,"+yeartb.get()+",'"+gender.get()+"')")
            cur.execute("commit")
            nmtb.delete(first=0,last='end')
            yeartb.delete(first=0,last='end')
            messagebox.showinfo("Success", "You are registered successfully.")
    submitbtn=Button(top,text="Submit", command=CandidateDetail,font=("TIMES NEW ROMAN",12),bg="coral1",bd=10,height=3,width=15);
    submitbtn.grid(row=7,column=2,rowspan=2)

def Count():
    for child in top.winfo_children():
        child.grid_forget()
    top.title('Count')
    Button(top,text="Home",font=("TIMES NEW ROMAN",12),bg="White",bd=10,height=2,width=10,command=Home).grid(row=0,column=7)
    top.geometry("625x400")
    top.anchor(N)
    radiovar = StringVar()
    radiovar.set("General Secretary")
    R1 = Radiobutton(top, text="General Secretary", variable= radiovar ,  value = "General Secretary", font=("TIMES NEW ROMAN",12),bg="White",bd=10,height=3,width=15)
    R2 = Radiobutton(top, text="Ladies Representative", variable= radiovar, value = "Ladies Representative", font=("TIMES NEW ROMAN",12),bg="White",bd=10,height=3,width=15)
    Label(top,text="Election",font=("TIMES NEW ROMAN",12),bg="White",bd=10,height=3,width=15).grid(row=1,column=1,rowspan=2);
    R1.grid(row=1,column=2,rowspan=2)
    R2.grid(row=1,column=3,rowspan=2)
    candname=[]
    votecount=[]
    def count1():
        r=6
        c=1

        if(radiovar.get()=='General Secretary'):
            tname=Label(top, text="Name", font=("TIMES NEW ROMAN",12),bg="White",bd=10,height=1,width=15).grid(row=5,column=1)
            telt=Label(top, text="Count", font=("TIMES NEW ROMAN",12),bg="White",bd=10,height=1,width=15).grid(row=5,column=2)
            cur.execute("select name,count from candidate where election='General Secretary' order by count desc")
            for name, count in cur :
                candname.append(Label(top, text= name , font=("TIMES NEW ROMAN",12),bg="White",bd=10,height=1,width=15))
                candname[len(candname)-1].grid(row=r,column=c)
                c+=1
                votecount.append(Label(top, text=count, font=("TIMES NEW ROMAN",12),bg="White",bd=10,height=1,width=15))
                votecount[len(candname)-1].grid(row=r,column=c)
                c-=1
                r+=1
        elif(radiovar.get()=="Ladies Representative"):
            tname=Label(top, text="Name", font=("TIMES NEW ROMAN",12),bg="White",bd=10,height=1,width=15).grid(row=5,column=1)
            telt=Label(top, text="Count", font=("TIMES NEW ROMAN",12),bg="White",bd=10,height=1,width=15).grid(row=5,column=2)
            cur.execute("select name,count from candidate where election='Ladies Representative' order by count desc")
            for name, count in cur :
                candname.append(Label(top, text= name , font=("TIMES NEW ROMAN",12),bg="White",bd=10,height=1,width=15))
                candname[len(candname)-1].grid(row=r,column=c)
                c+=1
                votecount.append(Label(top, text=count, font=("TIMES NEW ROMAN",12),bg="White",bd=10,height=1,width=15))
                votecount[len(candname)-1].grid(row=r,column=c)
                c-=1
                r+=1
    Button(top,text="OK",command=count1,font=("TIMES NEW ROMAN",12),bg="coral1",bd=10,height=2,width=15,fg="White").grid(row=3,column=2,columnspan=2)

def History():
    cur.execute("insert into history (select * from Candidate)")
    cur.execute("commit")
    messagebox.showinfo("Success", "Backup created")

menubar=Menu(top);
ActionMenu=Menu(menubar,tearoff=0,font=50,bg="White");
ActionMenu.add_command(label='Count',command=Count);
ActionMenu.add_separator();
ActionMenu.add_command(label='Add Candidates',command=AddCandidate);
ActionMenu.add_command(label='Add GS voters data',command=GSVoter);
ActionMenu.add_separator();
ActionMenu.add_command(label='Delete Candidates',command=DeleteCandidates);
ActionMenu.add_command(label='Delete Voters Details',command=DeleteVoters);
ActionMenu.add_separator();
ActionMenu.add_command(label='Add to History',command=History)
ActionMenu.add_command(label='Reset Voter data',command=Reset)
ActionMenu.add_command(label="Exit", command=top.quit)
menubar.add_cascade(label="Action", menu=ActionMenu)
top.config(menu=menubar);
Home()
top.mainloop()
