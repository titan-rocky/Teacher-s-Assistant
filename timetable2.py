import tkinter as tk
import mysql.connector
from datetime import datetime
import csv

def timetab(mycon):
	

	d=mycon.cursor()
	d.execute('SELECT * FROM timet')
	m=d.fetchall()


	file=open('login.csv','r')
	fileobj=csv.reader(file)
	for i in fileobj:
		if i[0]==mycon.user:
			dd=i[2]
	file.close()


	heading_font='bebas neue'
	ttablefont='sans bold'
	
	ttab=tk.Tk()
	scwid=ttab.winfo_screenwidth()
	schei=ttab.winfo_screenheight()
	winwid=1090
	winhei=512
	xcor=scwid/2-winwid/2-20
	ycor=schei/2-winhei/2-30
	ttab.geometry('%dx%d+%d+%d'%(winwid,winhei,xcor,ycor))
	ttab.resizable(0,0)
	ttab.title('Time Table')
	ttab.iconbitmap('icon.ico')

	heading=tk.Label(ttab,text='TIME TABLE',bg='#101f2f',fg='light blue',font=(heading_font,48));heading.grid(row=0,column=0,columnspan=2,pady=20)
	h=tk.Label(ttab,text=mycon.user.capitalize(),bg='#101f2f',fg='cyan',font=(heading_font,25));h.grid(row=1,column=0)
	d=tk.Frame(ttab,highlightbackground='#0b1d24',highlightthickness=4)
	h2=tk.Label(ttab,text=f'Class {dd}',bg='#101f2f',fg='cyan',font=(heading_font,25));h2.grid(row=1,column=1,)
	d.grid(row=2,column=0,columnspan=2,sticky='e',pady=10,padx=20)
	ttab.config(bg='#101f2f')


	def timetoindex():
		if datetime.now():
			pass

	f=['Day/Period','1','2','3','Break1','4','5','Lunch','6','7','Break2','8','9']




	for i in range(len(f)):
		name=tk.Label(d,text=f[i],fg='white',bg='#203E5E',padx=25,pady=5,font=(ttablefont,10),highlightbackground='cyan')
		name.grid(row=0,column=i,sticky='nswe')
		if i%2==0:
			pass
			name.config(bg='#2A4E75')
		if f[i] in ['Break1','Lunch','Break2'] :
			name.config(padx=10)

	bre=['B','R','E','A','K'];lun=['L','U','N','C','H']
	for i in range(len(m)):
		for j in range(len(m[i])):
			if m[i][j]==None:
				ab='    '
			else:
				ab=m[i][j]	
			s=tk.Label(d,text=ab,fg='#101f2f',bg='#5FABFD',padx=25,pady=5,font=('sans',10))
			s.grid(row=i+1,column=j,sticky='nswe')
			if j%2==0:
				s.config(bg='#D8E6F5')
			if j in [4,7,10] :
				if j==7:
					s.config(text=lun[i])
				else:
					s.config(text=bre[i])
				s.config(bg='#9AC7F6')
	def closel(topwin):
		topwin.destroy()
		return

	jj=tk.Button(ttab,text='close',command=lambda:closel(ttab),padx=20,pady=5,font=('garamond',15))
	jj.grid(row=4,column=0,columnspan=2,pady=10)
	ttab.mainloop()

#mycon=mysql.connector.connect(user='jeff',password='thexactr',database='jeff_db')
#timetab(mycon)