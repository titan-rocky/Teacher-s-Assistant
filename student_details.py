import tkinter as tk
import mysql.connector
import csv
from tkinter import messagebox
import sys

def st_details(mycon):
	bgd='#101f2f';fgd='light green'
	det=tk.Tk()
	det.iconbitmap('icon.ico')
	det.title('Student Details')
	det.resizable(width=False, height=False)
	det.config(background=bgd)
	scwidth=det.winfo_screenwidth()
	scheight=det.winfo_screenheight()
	winwid=570
	winhei=410
	xcor=scwidth/2-winwid/2-20
	ycor=scheight/2-winhei/2-30
	det.geometry('%dx%d+%d+%d'%(winwid,winhei,xcor,ycor))

	cur=mycon.cursor()

	cur.execute('SELECT * FROM student_details')



	title=tk.Label(det,text='STUDENT DETAILS',fg='light blue',bg=bgd,font=('bebas neue',40))
	title.grid(row=0,column=0,columnspan=2,padx=130,pady=20)

	detframe1=tk.Frame(det,bg=bgd)
	detframe1.grid(row=1,column=0,columnspan=2,pady=20)

	stname_label=tk.Label(detframe1,text='Name of the Student : ',fg=fgd,bg=bgd,font=('garamond',16))
	stname_label.grid(row=1,column=0,padx=10,sticky='we',pady=10)
	student_ent=tk.Entry(detframe1);student_ent.grid(row=1,column=1)
	stadmin_label=tk.Label(detframe1,text='Admission Number of the student : ',fg=fgd,bg=bgd,font=('garamond',16))
	stadmin_label.grid(row=2,column=0,padx=10,pady=10)
	stadmin_ent=tk.Entry(detframe1);stadmin_ent.grid(row=2,column=1)
	stnote=tk.Label(detframe1,text=' * Either one of the information is enough , both can be given for confirmation',fg='light pink',bg=bgd,font=('garamond',12))
	stnote.grid(row=3,column=0,columnspan=2,sticky='we',pady=10)

	data=cur.fetchall()

	def display():
		name=student_ent.get()
		admn=stadmin_ent.get()
		print(name)
		student_ent.delete(0,'end')
		stadmin_ent.delete(0,'end')
		det.update()
		bgd='#101f2f';fgd='light green'
		jk=tk. Toplevel()
		jk.iconbitmap('icon.ico')
		jk.title('Student Details')
		jk.resizable(width=False, height=False)
		jk.config(background=bgd)
		scwidth=jk.winfo_screenwidth()
		scheight=jk.winfo_screenheight()
		winwid=800
		winhei=510
		xcor=scwidth/2-winwid/2-20
		ycor=scheight/2-winhei/2-30
		jk.geometry('%dx%d+%d+%d'%(winwid,winhei,xcor,ycor))
		


		dtitle=tk.Label(jk,text='STUDENT DETAILS',fg='light blue',bg=bgd,font=('bebas neue',40))
		dtitle.grid(row=0,padx=250,pady=15)	
		dtext=tk.Label(jk,text='',fg=fgd,bg=bgd,font=('blackchancery',20))
		dtext.grid(row=1)


		dtfont='berlin sans'

		dtframe=tk.Frame(jk,bg=bgd)
		dtframe.grid(row=2,pady=15)
		dt1=tk.Label(dtframe,fg=fgd,bg=bgd,font=(dtfont,15))
		dt1.grid(row=0,column=0,padx=10,sticky='w')
		dt2=tk.Label(dtframe,fg=fgd,bg=bgd,font=(dtfont,15))
		dt2.grid(row=1,column=0,padx=10,sticky='w')
		dt3=tk.Label(dtframe,fg=fgd,bg=bgd,font=(dtfont,15))
		dt3.grid(row=2,column=0,padx=10,sticky='w')
		dt4=tk.Label(dtframe,fg=fgd,bg=bgd,font=(dtfont,15))
		dt4.grid(row=3,column=0,padx=10,sticky='w')
		dt5=tk.Label(dtframe,fg=fgd,bg=bgd,font=(dtfont,15))
		dt5.grid(row=4,column=0,padx=10,sticky='w')
		dt6=tk.Label(dtframe,fg=fgd,bg=bgd,font=(dtfont,15))
		dt6.grid(row=5,column=0,padx=10,sticky='w')
		dt7=tk.Label(dtframe,fg=fgd,bg=bgd,font=(dtfont,15))
		dt7.grid(row=6,column=0,padx=10,sticky='w')
		dt8=tk.Label(dtframe,fg=fgd,bg=bgd,font=(dtfont,15))
		dt8.grid(row=7,column=0,padx=10,sticky='w')

		de1=tk.Label(dtframe,fg=fgd,bg=bgd,font=(dtfont,15))
		de1.grid(row=0,column=1,padx=10,sticky='w')
		de2=tk.Label(dtframe,fg=fgd,bg=bgd,font=(dtfont,15))
		de2.grid(row=1,column=1,padx=10,sticky='w')
		de3=tk.Label(dtframe,fg=fgd,bg=bgd,font=(dtfont,15))
		de3.grid(row=2,column=1,padx=10,sticky='w')
		de4=tk.Label(dtframe,fg=fgd,bg=bgd,font=(dtfont,15))
		de4.grid(row=3,column=1,padx=10,sticky='w')
		de5=tk.Label(dtframe,fg=fgd,bg=bgd,font=(dtfont,15))
		de5.grid(row=4,column=1,padx=10,sticky='w')
		de6=tk.Label(dtframe,fg=fgd,bg=bgd,font=(dtfont,15))
		de6.grid(row=5,column=1,padx=10,sticky='w')
		de7=tk.Label(dtframe,fg=fgd,bg=bgd,font=(dtfont,15))
		de7.grid(row=6,column=1,padx=10,sticky='w')
		de8=tk.Label(dtframe,fg=fgd,bg=bgd,font=(dtfont,15))
		de8.grid(row=7,column=1,padx=10,sticky='w')

		print(admn)

		def show(tup):
			dt1.config(text='Student Name : ')
			dt2.config(text='Admission Number : ')
			dt3.config(text='Father\'s Name : ')
			dt4.config(text='Gender : ')
			dt5.config(text='Contact Number : ')
			dt6.config(text='Address : ')
			dt7.config(text='Blood Group : ')
			dt8.config(text='Disciplinary Records : ')

			if tup[0]:
				de1.config(text=tup[0].capitalize())
			else:
				de1.config(text='None')
			if tup[1]:
				de2.config(text=tup[1])
			else:
				de2.config(text='None')
			if tup[2]:
				de3.config(text=tup[2])
			else:
				de3.config(text='None')
			if tup[3]:
				de4.config(text=tup[3])
			else:
				de4.config(text='None')
			if tup[4]:
				de5.config(text=tup[4])
			else:
				de5.config(text='None')
			if tup[5]:
				de6.config(text=tup[5])
			else:
				de6.config(text='None')
			if tup[6]:
				de7.config(text=tup[6])
			else:
				de7.config(text='None')
			if tup[7]:
				de8.config(text=tup[7])
			else:
				de8.config(text='None')
			print(i)

		for i in data :
			if name==i[0]:
				if admn==i[1]:
					dtext.config(text='Found Perfectly')
					show(i)
				elif admn=='':
					dtext.config(text='Found By Name')
					show(i)
				else:
					dtext.config(text='Name does not match with Admission Number')
				break
			else:
				dtext.config(text='No records Found ! :( ')
			jk.update()

		dbutt=tk.Button(jk,text='Close',command=jk.destroy,bg=fgd,font=('blackchancery',15),padx=20)
		dbutt.grid(row=3,column=0)

		pass
	def back():
		det.destroy()
		from welcome import welcometo
		welcometo(mycon.user,mycon._password)

	detbut1=tk.Button(det,text='Display',font=('garamond',15),bg=fgd,activebackground=bgd,activeforeground=fgd,padx=20,command=display)
	detbut1.grid(row=2,column=0,pady=20,sticky='e',padx=30)
	detbut2=tk.Button(det,text='Welcome Page',font=('garamond',15),bg=fgd,activebackground=bgd,activeforeground=fgd,command=back)
	detbut2.grid(row=2,column=1,pady=20,sticky='w')


	def onclose():
		if messagebox.askokcancel('Quit','Do you want to quit ?') :
			sys.exit()
			#welc.destroy()
			#beforewindow.destroy()
			print('quit')
			

	det.protocol('WM_DELETE_WINDOW',onclose)

	det.mainloop()