import tkinter as tk
from tkcalendar import *
from datetime import datetime
import mysql.connector
from mysql.connector import errorcode
import sys

def view_attn(sqlcon,user):
    dt=tk.Tk()
    g=datetime.today()
    bgd='#101f2f';fgd='light pink'
    scwid=dt.winfo_screenwidth()
    schei=dt.winfo_screenheight()
    winwid=1000
    winhei=450
    xcor=scwid/2-winwid/2-20
    ycor=schei/2-winhei/2-30
    dt.geometry('%dx%d+%d+%d'%(winwid,winhei,xcor,ycor))
    dt.config(background=bgd)
    dt.resizable(0,0)
    dt.iconbitmap('icon.ico')
    dt.title('View Attendence')
    #color
    canvas_color='#101f2f'
    frame1_color='#101f2f'
    button_bg='#3caea3'
    button_fg='#101f2f'

    title=tk.Label(dt,text='View Attenence',font=('bebas neue',40),fg=fgd,bg=bgd);title.grid(row=0)
    calenframe=tk.Frame(dt,pady=40,bg=bgd);calenframe.grid(row=1,pady=10,padx=60)
    calen=Calendar(calenframe,selectmode='day',year=g.year,month=g.month,day=g.day,fg=fgd,bg=bgd);calen.grid(row=0,column=0,padx=100)
    calendetails=tk.Label(calenframe,text='Selet the date\nfor which you need\nthe attendence details',bg=bgd,fg=fgd,font=('bebas neue',30))
    calendetails.grid(row=0,column=1,padx=50)
    flag=0;info_frame=0
    def getdate(calendarobj):
    	calendetails.destroy()
    	nonlocal flag;nonlocal info_frame
    	if info_frame:
    		info_frame.destroy()
    	flag=0
    	calendate=calendarobj.get_date().split('/')
    	d=f'{calendate[1]}_{calendate[0]}_20{calendate[2]}'
    	m=sqlcon.cursor()
    	info_frame=tk.Frame(calenframe,bg=bgd);info_frame.grid(row=0,column=1,pady=10,padx=130)
    	try:
    		m.execute(f'SELECT studentname,{d} FROM attendence ')
    		k=m.fetchall()
    		def countofstudents(lis):
	    		total=len(lis);absent=0;absent_list=[]
	    		for i in lis:
	    			if i[1]=='0':
	    				absent+=1
	    				absent_list.append(i[0])
    			return total,absent,absent_list
    		k=countofstudents(k)
    		info1=tk.Label(info_frame,text=f'Total Number of Students  : {k[0]}',fg=fgd,bg=bgd);info1.grid(row=0,column=0)
    		info2=tk.Label(info_frame,text=f'Total Number of Absentees  : {k[1]}',fg=fgd,bg=bgd);info2.grid(row=1)
    		jk=k[2]
    		info3=tk.Label(info_frame,text=f'Absentees  :',fg=fgd,bg=bgd);info3.grid(row=2,pady=3)
    		l1=[];l2=[]
    		for i in jk:
    			l2.append(i)
    			if len(l2)==3:
    				l1.append(l2)
    				l2=[]
    			elif i==jk[-1]:
    				l1.append(l2)
    				l2=[]
    		
    		for p in range(len(l1)):
    			absframe=tk.Frame(info_frame,bg=bgd);absframe.grid(row=3+p)
    			for m in range(len(l1[p])):
    				absprint=tk.Label(absframe,text=f' {l1[p][m].capitalize()} ',bg=bgd,fg=fgd);absprint.grid(row=0,column=m)
    		flag=1

    		

    	except mysql.connector.Error as err:
    		if err.errno==1054:
    			jbk=calendarobj.get_date();jbk=jbk.split('/');jbk[0],jbk[1]=jbk[1],jbk[0];jbk='/'.join(jbk)

    			info_frame=tk.Frame(calenframe,bg=bgd);info_frame.grid(row=0,column=1,pady=10,padx=130)
    			info=tk.Label(info_frame,text=f'There are no Records on\n{jbk}',fg=fgd,bg=bgd,font=('garamond',15))
    			info.grid(row=0,column=1)


    butframe=tk.Frame(dt,bg=bgd);butframe.grid(row=2)
    but1=tk.Button(butframe,text='Get Date',command=lambda : getdate(calen),fg='light cyan',bg=bgd,padx=25,font=('garamond',15))
    but1.grid(row=0,column=1,padx=10)
   
    def on_back():
        dt.destroy()
        from attendence import attn
        attn(sqlcon,sqlcon.user)

    but2= tk.Button(butframe,text='Back',fg='light cyan',bg=bgd,padx=25,font=('garamond',15),command=on_back)
    but2.grid(row=0,column=2,padx=10)

    from tkinter import messagebox
    def onclose():
    	if messagebox.askokcancel('Quit','Do you want to quit ?') :
    		sys.exit()
    dt.protocol('WM_DELETE_WINDOW',onclose)
    dt.mainloop()

#mycon=mysql.connector.connect(user='jeff',password='thexactr',database='jeff_db')
#view_attn(mycon,mycon.user)
