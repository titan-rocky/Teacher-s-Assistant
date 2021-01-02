import tkinter as tk
import sys
import time
import mysql.connector
import csv
def click(sqlconnector,root):
	# this function is for creating a new account
	creacc_bgd='#101f2f'
	creacc=tk.Tk()
	creacc.resizable(False, False)
	scwidth=creacc.winfo_screenwidth()
	scheight=creacc.winfo_screenheight()
	winwid=644
	winhei=400
	xcor=scwidth/2-winwid/2-20
	ycor=scheight/2-winhei/2-30
	creacc.geometry('%dx%d+%d+%d'%(winwid,winhei,xcor,ycor))
	creacc.iconbitmap('icon.ico')
	creacc.title('Create Account')
	creacc.config(background=creacc_bgd)


	cac_label_fg='#d3c1a3'


	cac2_title=tk.Label(creacc,text='Create a New account',bg=creacc_bgd,font=('bebas neue',30),fg='#77b9c1')
	cac2_title.grid(row=1,column=0,columnspan=3,padx=170,pady=10)




	cac_userframe=tk.Frame(creacc,bg=creacc_bgd)
	cac_userframe.grid(row=2,column=0,columnspan=3,padx=55,pady=10)
	#username
	cac_userempty=tk.Label(cac_userframe,text='            ',fg=cac_label_fg,bg=creacc_bgd,font=('century gothic italic',15))
	cac_userempty.grid(row=0,column=1,pady=15)
	cac_userlabel=tk.Label(cac_userframe,text='Enter the username : ',fg=cac_label_fg,bg=creacc_bgd,font=('garamond',18),justify='left')
	cac_userlabel.grid(row=0,column=0,pady=15,sticky='w')
	cac_username=tk.Entry(cac_userframe,fg='#000000',font=('arial',9),borderwidth=2)
	cac_username.grid(row=0,column=2,padx=10,pady=15,columnspan=2,sticky='w')

	#password
	cac_passlabel=tk.Label(cac_userframe,text='Enter the password : ',fg=cac_label_fg,bg=creacc_bgd,font=('garamond',18),justify='left')
	cac_passlabel.grid(row=1,column=0,pady=15)
	cac_password=tk.Entry(cac_userframe,fg='#000000',font=('arial',9),borderwidth=2)
	cac_password.grid(row=1,column=2,padx=10,pady=15,columnspan=2,sticky='w')

	caclass=None
	creacc_d_fg='#4d99ba'
	creacc_d_font='blackchancery'
	creacc_d_font_size=17
	creacc_d_pady=10
	creacc_d=tk.Label(creacc,text='',font=(creacc_d_font,creacc_d_font_size),fg=creacc_d_fg,bg=creacc_bgd,pady=creacc_d_pady)
	creacc_d.grid(row=3,column=0,columnspan=3)

	success=0
	def cac_on_click():
		time.sleep(0.7)
		cau=cac_username.get()
		cap=cac_password.get()

		#checking
		checkcsv=open('login.csv','r',newline='\n')
		checkread=csv.reader(checkcsv)
		csvre=[i for i in checkread]
		checkcsv.close()

		creacc_cur=sqlconnector.cursor()
		verify=0
		for i in cau:
			if i.isalnum() or i.isspace() or i=='_':
				verify=1

			else:
				verify=0
				break
		def signup_process(causer,capass,sign_con,signcon_cur,creacc):
			creacc_d.config(text='Processing');creacc.update()
			causer=str(causer)
			capass=str(capass)
			global sqlconnector
			usercsv=open('login.csv','a',newline='\n')
			userwrite=csv.writer(usercsv)
			userwrite.writerow([cau,cap,caclass])
			usercsv.close()
			cac_querybox=[f'create user \'{str(cau)}\'@\'localhost\' identified by \'{str(cap)}\';',f'create database {str(cau)}_db ;',f'use {str(cau)}_db ;',f'GRANT ALL ON {str(cau)}_db.* TO \'{str(cau)}\'@\'localhost\';','flush privileges;','CREATE TABLE timet (Day_Period varchar(32),Period1 varchar(4),Period2 varchar(4),Period3 varchar(4),Break1 varchar(4),Period4 varchar(4),Period5 varchar(4),LunchB varchar(4),Period6 varchar(4),Period7 varchar(4),Break2 varchar(4),Period8 varchar(4),Period9 varchar(4));','INSERT INTO timet(Day_Period) VALUES(\'Monday\'),(\'Tuesday\'),(\'Wednesday\'),(\'Thursday\'),(\'Friday\') ;','CREATE TABLE attendence (studentname varchar(32),admn_no char(6) PRIMARY KEY);','update timet set LunchB=\'\'','update timet set Break1=\'\'','update timet set Break2=\'\'']
			for i in cac_querybox:
				print(i)
				signcon_cur.execute(i)
				sign_con.commit()
			creacc_d.config(text='Successfully Signed Up !');creacc.update()
			time.sleep(1)
			creacc.withdraw()
			from login_page import login
			login()
			success=1


		if len(cau)<=32:
			if verify==1:
				if cau in csvre:
					creacc_d.config(text=f'Username {cau} already exists')
					creacc.update()
				elif cap!='' and len(cap)+1>8:
					try:
						signup_process(cau,cap,sqlconnector,creacc_cur,creacc)
						return 1
					except mysql.connector.errors.DatabaseError:
						creacc_d.config(text=f'Username {cau} already exists');creacc.update()
						return 0

				elif cap=='':
					creacc_d.config(text='Enter a Valid Password')
					creacc.update()
				elif len(cap)+1<8:
					creacc_d.config(text='Password must be more than 8 characters')
					creacc.update()
			else:
				creacc_d.config(text='Please enter a valid Username ! ')

			creacc_cur.close()
		elif len(cau)>32:
			creacc_d.config(text='Username cannot exceed 32 characters !')


	#button
	cac_but_fg=creacc_bgd
	cac_but_bg='#748188'
	cac_but_actfg='#77b9c1'
	cac_but_actbg=creacc_bgd


	return_to_login=0
	def cac_close():
		time.sleep(1.7)
		creacc.withdraw()
		import login_page
		login_page.login()

	cac_signin=tk.Button(creacc,text='Sign Up',font=('garamond',14),padx=25,command=cac_on_click,fg=cac_but_fg,bg=cac_but_bg,activebackground=cac_but_actbg,activeforeground=cac_but_actfg)
	cac_signin.grid(row=4,column=0,pady=10,sticky='n')

	cac_close=tk.Button(creacc,text='Log in',font=('garamond',14),padx=25,command=cac_close,fg=cac_but_fg,bg=cac_but_bg,activebackground=cac_but_actbg,activeforeground=cac_but_actfg)
	cac_close.grid(row=4,column=2,pady=10,sticky='n')

	creacc.mainloop()
	creacc_mycon.close()
	if success==1:
		return 1