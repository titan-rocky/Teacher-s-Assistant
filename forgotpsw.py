import mysql.connector
import tkinter as tk
import csv
import time
from tkinter import messagebox
import sys


def forgotpswd(root):
	fps=tk.Tk()
	scwidth=fps.winfo_screenwidth()
	scheight=fps.winfo_screenheight()
	winwid=570
	winhei=380
	xcor=scwidth/2-winwid/2-20
	ycor=scheight/2-winhei/2-30
	fps.geometry('%dx%d+%d+%d'%(winwid,winhei,xcor,ycor))
	fps.config(bg='#101f2f')
	fps.resizable(0,0)
	fps.iconbitmap('icon.ico')
	fps.title('Forgot Password')

	bgd='#101f2f'

	label_fg='cyan'

	label_fg='#992c2d'
	#title text
	titleof_font='bebas neue'
	titleof=tk.Label(fps,text="Forgot Password",font=('bebas neue',32),fg='#3caea3',bg=bgd)
	titleof.grid(row=0,column=0,columnspan=3,padx=160,pady=20,sticky='s')

	userframe=tk.Frame(fps,bg=bgd)
	userframe.grid(row=2,column=0,columnspan=3,padx=25,pady=10)
	#username
	userempty=tk.Label(userframe,text='             ',fg=label_fg,bg=bgd,font=('',15))
	userempty.grid(row=0,column=1,pady=15)
	userlabel=tk.Label(userframe,text='Enter the username : ',fg=label_fg,bg=bgd,font=('garamond',18))
	userlabel.grid(row=0,column=0,pady=15,sticky='w')
	username=tk.Entry(userframe,fg='#000000',font=('arial',9))
	username.grid(row=0,column=2,padx=10,pady=15,columnspan=2,sticky='w')



	pat=tk.Label(userframe,text='',bg='#101f2f',fg='cyan',font=('garamond',18));pat.grid(row=3,column=0,columnspan=3)
	gg=0
	file=open('login.csv','r')
	b=csv.reader(file);l=[i for i in b]

	def jam():
		nonlocal gg;nonlocal username
		gz=username.get()
		fps.update()
		username.delete(0,'end')
		for p in l :
			if p[0]==gz:
				gg=1;k=p[2];
				break
		else:
			if len(gz)==0:
				pat.config(text=f'Please enter a valid username !')
				gg=0
			else:
				pat.config(text=f'Username {gz} is not found')
				gg=0

		username.delete(0,'end')
		if gg==1:
			nonlocal userframe
			userframe.destroy()
			passframe=tk.Frame(fps,bg=bgd)
			passframe.grid(row=2,column=0,columnspan=3,padx=25,pady=10)
			passtitle=tk.Label(fps,text=f'{gz.capitalize()}             Class:{k}',fg=label_fg,bg=bgd,font=(titleof_font,18));passtitle.grid(row=1,column=0,padx=10,columnspan=3,sticky='we')
			passempty=tk.Label(passframe,text='         ',fg=label_fg,bg=bgd,font=('century gothic italic',15))
			passempty.grid(row=1,column=1,pady=15)
			passlabel=tk.Label(passframe,text='Enter the password : ',fg=label_fg,bg=bgd,font=('garamond',18))
			passlabel.grid(row=1,column=0,pady=15,sticky='w')
			passname=tk.Entry(passframe,fg='#000000',font=('arial',11),show='*')
			passname.grid(row=1,column=2,padx=10,pady=15,columnspan=2,sticky='w')
			passempty2=tk.Label(passframe,text='        ',fg=label_fg,bg=bgd,font=('century gothic italic',15))
			passempty2.grid(row=2,column=1,pady=15)
			passlabel2=tk.Label(passframe,text='Re-Enter the password : ',fg=label_fg,bg=bgd,font=('garamond',18))
			passlabel2.grid(row=2,column=0,pady=15,sticky='w')
			passname2=tk.Entry(passframe,fg='#000000',font=('arial',11),show='*')
			passname2.grid(row=2,column=2,padx=10,pady=15,columnspan=2,sticky='w')


			def fame(entry1,entry2,user,password):
				if entry1==entry2:
					import csv
					file=open('login.csv','r')
					readerobj=csv.reader(file);content=[i for i in readerobj]
					for i in content:
						if gz==i[0]:
							i[1]=password
					print(content)
					file.close();file=open('login.csv','w',newline='\n')
					writerobj=csv.writer(file)
					writerobj.writerows(content)
					file.close()

					changecon=mysql.connector.connect(user='root',password='manager')
					j=changecon.cursor()
					j.execute(f'ALTER USER \'{user}\'@localhost IDENTIFIED BY \'{password}\'')
					changecon.commit();changecon.close()
					passframe.destroy()
					result=tk.Label(fps,text='Password Changed Successfully !',font=('garamond',18),fg='white',bg=bgd);result.grid(row=4,pady=10,column=0,columnspan=3)
					fps.update()
					time.sleep(1)
					fps.destroy()
					root.destroy()
					from login_page import login
					login()

				else:
					pin=tk.Label(passframe,text='Password does not match',font=('garamond',12),fg=label_fg,bg=bgd);pin.grid(row=4,column=0,columnspan=3)

			

			changebutt=tk.Button(passframe,text='Change',command= lambda : fame(passname.get(),passname2.get(),gz,passname.get()),padx=30,font=('garamond',15),fg='#124183',bg='#c4b480',activeforeground='#c4b480',activebackground=bgd);changebutt.grid(row=3,column=0,columnspan=3,padx=180,pady=10)

	def quitb():
		fps.destroy()
		root.destroy()
		from login_page import login
		login()
				
	butt=tk.Button(userframe,text='Confirm',command=jam,padx=30,font=('garamond',15),fg='#124183',bg='#c4b480',activeforeground='#c4b480',activebackground=bgd);butt.grid(row=4,column=0,padx=150,columnspan=3,pady=10,)
	butt=tk.Button(userframe,text='Login Page',command=quitb,padx=30,font=('garamond',15),fg='#124183',bg='#c4b480',activeforeground='#c4b480',activebackground=bgd);butt.grid(row=5,column=0,padx=150,columnspan=3,pady=10,)
	def onclose():
		d=messagebox.askokcancel('Quit','Do you want to quit ?')
		if d:
		    fps.destroy()
		    sys.exit()


	fps.protocol('WM_DELETE_WINDOW',onclose)

	fps.mainloop()


#forgotpswd()
'#124183''#c4b480''#c4b480'