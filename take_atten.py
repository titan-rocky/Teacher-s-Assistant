from tkinter import *
from tkinter import messagebox
import mysql.connector
from tkinter import ttk
import csv
# date
from datetime import date
import time

def take_attn(sqlcon,user):
    today = date.today()
    today=str(today.day)+'_'+str(today.month)+'_'+str(today.year)

    atte = Toplevel()
    atte.title('Attendence')
    atte.config(background='#101f2f')
    atte.title('Take Attendence')
    scwid=atte.winfo_screenwidth()
    schei=atte.winfo_screenheight()
    winwid=515
    winhei=420
    xcor=scwid/2-winwid/2-20
    ycor=schei/2-winhei/2-30
    atte.geometry('515x420+%d+%d'%(xcor,ycor))
    atte.resizable(0,0)
    #color
    canvas_color='#101f2f'
    frame1_color='#101f2f'
    button_bg='#3caea3'
    button_fg='#101f2f'



    # connector
    mycursor = sqlcon.cursor()


    #taking info of class in which the teacher is in charge
    file=open('login.csv','r')
    j=csv.reader(file)
    for i in j:
        if i[0]==user:
            cj=i[2]
    file.close()

    #window

    var= IntVar()

    atte.title('Attendence')

    frame1 = Frame(atte,bg=frame1_color)
    frame2 = Frame(atte,bg=frame1_color)
    frame3 = Frame(atte,bg=frame1_color)
    frame1.grid(row=0,column=0,)
    frame2.grid(row=1,column=0)
    frame3.grid(row=2,column=0)



    a = Label(frame1, text=f'Class {cj}', font=('bebas neue',30),fg='#3caea3',bg=frame1_color)
    a.grid(row=0, column=0,padx=186)
    s1 = Label(atte, text='       ')
    s1.grid(row=1)
    t1='Date:',today
    b = Label(frame1, text=t1,font=('garamond',14),fg='#c4b480',bg=frame1_color)
    b.grid(row=2,column=0,pady=5)


    frame= Frame(atte,bg='light cyan')
    frame.grid(row=1,column=0)

    #canvas
    can=Canvas(frame,background='light cyan')
    can.pack(side=LEFT, fill=BOTH, expand=1)

    save=0
    #add scroll
    scroll= ttk.Scrollbar(frame,orient=VERTICAL, command=can.yview,)

    scroll.pack(side=RIGHT, fill=Y)
    s = ttk.Style()
    s.configure('Vertical.TScrollbar', background='maroon',troughcolor='black')

    #config canvas
    can.configure(yscrollcommand=scroll.set)
    can.bind('<Configure>', lambda e: can.configure(scrollregion=can.bbox('all')))

    #create frame in canvas
    f2= Frame(can,bg='light cyan')

    #add frame to winodw in canvas
    can.create_window((0,0),window=f2, anchor='nw')


    r='select studentname from attendence'
    mycursor.execute(r)
    data=[i for i in mycursor.fetchall()]

    dk=Label(atte,text='Hi')
    dk.grid(row=4,column=2)
    valuelist=[]

    def attend(connector,valuelist):
        svalue=[]
        for i in valuelist:
            svalue.append(i.get())
        dk.config(text=f'{svalue}')
        q = "ALTER TABLE attendence ADD {0} varchar(1)".format(today)
        connector.commit()
        j=connector.cursor()
        try:
            j.execute(q)
            for p in range(len(data)):
                j.execute(f'update attendence set {today} = {svalue[p]} where studentname=\'{data[p][0]}\' ;')
                connector.commit()
                nonlocal save
                save=1
        except mysql.connector.Error as err:
            if err.errno==1060:
                btn.config(text=f'Record already exists for today',state='disabled',bg='#101f2f')
                atte.update()
                time.sleep(2)
                atte.destroy()
                from attendence import attn
                attn(sqlcon,user)

        

    for i in range(len(data)):
        cur=IntVar()
        Checkbutton(f2,text=f'{data[i][0].capitalize()}',variable=cur,font=('garamond',13,),fg='#001616',bg='light cyan',activeforeground='light cyan',activebackground='light cyan').grid(row=i,column=0,sticky='w')
        valuelist.append(cur)
    
    def on_back():
        atte.destroy()
        from attendence import attn
        attn(sqlcon,sqlcon.user)


    btn= Button(frame3,text='Save Attendence',font=('garamond',13),fg=button_fg,bg=button_bg,command=lambda : attend(sqlcon,valuelist))
    btn.grid(row=4,column=0,pady=10,padx=10)
    btn2= Button(frame3,text='Back',font=('garamond',13),fg=button_fg,bg=button_bg,command=on_back)
    btn2.grid(row=4,column=1,pady=10,padx=10)



    def onclose():
        if save==1:
            atte.destroy()
            from attendence import attn
            attn(sqlcon,user)

        elif messagebox.askokcancel('Quit','Do you want to quit without saving ?') :
            atte.destroy()
            

    atte.protocol('WM_DELETE_WINDOW',onclose)

    atte.mainloop()


czv=mysql.connector.connect(user='jeff',password='thexactr',database='jeff_db')
take_attn(czv,'jeff')