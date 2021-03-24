import tkinter as tk
import csv
import mysql.connector
from tkinter import messagebox
import sys


def attn(sqlcon,user):
	bgd='#101f2f'
	att=tk.Tk()
	att.iconbitmap('icon.ico')
	att.title('Attendence')
	att.resizable(width=False, height=False)
	att.config(background=bgd)
	scwidth=att.winfo_screenwidth()
	scheight=att.winfo_screenheight()
	winwid=570
	winhei=410
	xcor=scwidth/2-winwid/2-20
	ycor=scheight/2-winhei/2-30
	att.geometry('%dx%d+%d+%d'%(winwid,winhei,xcor,ycor))


	file=open('login.csv','r')
	readobj=csv.reader(file)
	for i in readobj:
		if i[0]==user:
			userclass=i[2]

	dz=tk.Label(att,text='Attendence',fg='light pink',bg=bgd,font=('bebas neue',40));dz.grid(row=0,padx=175,pady=20)
	dz2=tk.Label(att,text=f'{sqlcon.user}',fg='light blue',bg=bgd,font=('bebas neue',20));dz2.grid(row=1)
	dz3=tk.Label(att,text=f'class {userclass}',fg='light blue',bg=bgd,font=('bebas neue',15));dz3.grid(row=2)

	att_button_fg='#124183'
	att_button_bg='#c4b480'
	att_button_font='garamond'
	att_button_activebg=bgd
	att_button_activefg='#c4b480'
	att_button_size=15



	def take_attendence():
		att.withdraw()
		from take_atten import take_attn
		take_attn(sqlcon,user)
	def view_attendence():
		att.withdraw()
		from view_atten import view_attn
		view_attn(sqlcon,user)
	def quit_attendence():
		att.withdraw()
		from welcome import welcometo
		welcometo(sqlcon.user,sqlcon._password)


	butframe=tk.Frame(att,bg=bgd);butframe.grid(row=3,pady=40,columnspan=2)
	but1=tk.Button(butframe,text='View Attendence',command=view_attendence,bg=att_button_bg,fg=att_button_fg,activebackground=att_button_activebg,activeforeground=att_button_activefg,font=(att_button_font,att_button_size))
	but1.grid(row=0,column=0,padx=10)
	but2=tk.Button(butframe,text='Take Attendence',command=take_attendence,bg=att_button_bg,fg=att_button_fg,activebackground=att_button_activebg,activeforeground=att_button_activefg,font=(att_button_font,att_button_size))
	but2.grid(row=0,column=1,padx=10)
	but3=tk.Button(butframe,text='Welcome Page',command=quit_attendence,bg=att_button_bg,fg=att_button_fg,activebackground=att_button_activebg,activeforeground=att_button_activefg,font=(att_button_font,att_button_size))
	but3.grid(row=1,column=0,padx=10,pady=15,columnspan=2)
	def onclose():
		if messagebox.askokcancel('Quit','Do you want to quit ?') :
			sys.exit()
			#welc.destroy()
			#beforewindow.destroy()
			print('quit')
			

	att.protocol('WM_DELETE_WINDOW',onclose)

	att.mainloop()

#mycon=mysql.connector.connect(user='jeff',password='thexactr',database='jeff_db')
#attn(mycon,mycon.user)