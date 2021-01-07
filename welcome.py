import tkinter as tk
import mysql.connector
from tkinter import messagebox
from tkinter import ttk
import sys
import csv
# date
from datetime import date

def welcometo(loginusername,loginpassword):
	global time_untill
	time_untill=1
	#loginusername='234214'
	#loginpassword='325758'
	bgd='#101f2f'
	welc=tk.Tk()
	welc.iconbitmap('icon.ico')
	welc.title('Home Page')
	welc.resizable(width=False, height=False)
	welc.config(background=bgd)
	scwidth=welc.winfo_screenwidth()
	scheight=welc.winfo_screenheight()
	winwid=570
	winhei=410
	xcor=scwidth/2-winwid/2-20
	ycor=scheight/2-winhei/2-30
	welc.geometry('%dx%d+%d+%d'%(winwid,winhei,xcor,ycor))
	welc.iconbitmap('icon.ico')



	welc_title=tk.Label(welc,text="Teacher\'s Assistant",font=('Bebas Neue',30),fg='#3caea3',bg=bgd)
	welc_title.grid(row=0,column=1)
	empty1=tk.Label(welc,text='                     ',bg=bgd,fg='#101f2f',font=('bebas neue',20))
	empty1.grid(row=0,column=0)
	#welc_title.grid(row=0,column=0,columnspan=3,padx=140)
	import time
	from datetime import date

	frame1=tk.Frame(welc,bg='aquamarine')
	frame1.grid(row=1,column=1,pady=12)
	welc_con=mysql.connector.connect(username=loginusername,password=loginpassword,database=f'{loginusername}_db')
	title=tk.Label(frame1,text="Welcome\n"+loginusername,bg='aquamarine',fg='#101f2f',font=('bebas neue',20))
	title.grid(row=0,column=1,sticky='we')
	empty2=tk.Label(frame1,text='|\n|',bg='aquamarine',fg='#101f2f',font=('bebas neue',20))
	empty2.grid(row=0,column=2)
	dor=tk.Label(frame1,text='hi',bg='aquamarine',fg='#101f2f',font=('bebas neue',20))
	dor.grid(row=0,column=3)

	def clock(n=1):
		if n==0:
			print('clock over')
			return 	welc.update()
		s=time.strftime('%H:%M:%S')
		md=str(date.today()).split('-');md.reverse()
		st='%s-%s-%s'%(md[0],md[1],md[2])
		dor.config(text=f'{st}\n{s}')
		dor.after(1000,clock)

	clock()


	welc_button_frame=tk.Frame(welc,bg=bgd)
	welc_button_frame.grid(row=2,column=1)
	welc_button_fg='#124183'
	welc_button_bg='#c4b480'
	welc_button_font='garamond'
	welc_button_activebg=bgd
	welc_button_activefg='#c4b480'
	welc_button_size=12

	def attendencefn():
		welc.withdraw()
		from attendence import attn
		attn(welc_con,loginusername)


	def detail():
		from student_details import st_details
		stdetails()
	def timetclick():
		from timetable2 import timetab
		timetab(welc_con)
	def logout():
		try:
			global time_untill
			waraccept=messagebox.askokcancel('Log Out','Do you want to log out ?')
			if time_untill:
				time_untill=0
			print(time_untill)
			if time_untill==0 and waraccept:
				import login_page
				print('exit')
				clock(0)
				welc.withdraw()
				login_page.login()
		except:
			pass #not major error skipping , only invalid command name after destroy of window
	proverbfile=open('proverbs.txt','r')
	proverbs=[i for i in proverbfile.readlines() if i!='\n']
	import random
	#button
	attp=tk.Label(welc,wraplength=400,text=proverbs[random.randint(0,len(proverbs)-1)][4:],font=('garamond','12'),fg='white',bg=bgd)
	attp.grid(row=3,column=1,pady=18)
	attendb=tk.Button(welc_button_frame,text='Attendence',command=attendencefn,bg=welc_button_bg,fg=welc_button_fg,activebackground=welc_button_activebg,activeforeground=welc_button_activefg,font=(welc_button_font,welc_button_size),padx=20,pady=5)
	attendb.grid(row=1,column=0,pady=10,padx=10,sticky='we')
	msgb=tk.Button(welc_button_frame,text='Student Details',command=detail,bg=welc_button_bg,fg=welc_button_fg,activebackground=welc_button_activebg,activeforeground=welc_button_activefg,font=(welc_button_font,welc_button_size),padx=20,pady=5)
	msgb.grid(row=1,column=1,pady=10,padx=10)
	timetb=tk.Button(welc_button_frame,text='Class Time Table',command=timetclick,bg=welc_button_bg,fg=welc_button_fg,activebackground=welc_button_activebg,activeforeground=welc_button_activefg,font=(welc_button_font,welc_button_size),padx=20,pady=5)
	timetb.grid(row=2,column=0,pady=10,padx=10)
	lgoutb=tk.Button(welc_button_frame,text='Log out',command=logout,bg=welc_button_bg,fg=welc_button_fg,activebackground=welc_button_activebg,activeforeground=welc_button_activefg,font=(welc_button_font,welc_button_size),padx=20,pady=5)
	lgoutb.grid(row=2,column=1,pady=10,padx=10,sticky='w'+'e')
	def onclose():
		if messagebox.askokcancel('Quit','Do you want to quit ?') :
			sys.exit()
			print('quit')
			

	welc.protocol('WM_DELETE_WINDOW',onclose)
	welc.mainloop()