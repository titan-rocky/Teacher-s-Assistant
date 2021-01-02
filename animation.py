import tkinter as tk
import time
from playsound import playsound
import threading
import sys

ovfont='vhiena strip shadow'
ovbg='#101f2f';ovfg='#3caea3'
root=tk.Tk()
scwid=root.winfo_screenwidth()
schei=root.winfo_screenheight()
winwid=1200
winhei=600
xcor=scwid/2-winwid/2-20
ycor=schei/2-winhei/2-30
root.geometry('1200x600+%d+%d'%(xcor,ycor))
root.config(bg=ovbg)
root.iconbitmap('icon.ico')
j=tk.Label(root,text='Welcome To\nTeacher\'s Assistant',font=(ovfont,100),fg=ovfg,bg=ovbg)
j.grid(row=0,column=0,columnspan=2,pady=75)
root.resizable(0,0)
def on_click():
	import login_page
	root.withdraw()
	login_page.login()
def anim():
	try:
		for i in range(185):
			time.sleep(0.005)
			j.grid_configure(padx=i)
			root.update()
		for k in range(25):
			time.sleep(0.034)
			j.grid_configure(padx=i-k)
			root.update()
		for l in range(5):
			time.sleep(0.4)
			if l%2!=0:
				root.config(bg=ovbg)
				j.config(bg=ovbg,fg=ovfg)
			else:
				root.config(bg=ovfg)
				j.config(bg=ovfg,fg=ovbg)
			root.update()
		lm=tk.Label(root,text='Press Start !',font=('vhiena regular',45),fg=ovbg,bg=ovfg);lm.grid(row=1,column=0,columnspan=2)
		lb=tk.Button(root,text='start',state='normal',command=on_click,font=('vhiena regular',20),fg=ovbg,bg=ovfg,border=5,padx=20,highlightbackground='black',activeforeground=ovfg,activebackground=ovbg);lb.grid(row=2,padx=520,pady=20)
		root.update()
	except tk.TclError:
		print('quit')
		thread1.join()
		exit()
		sys.exit()

def music():
	playsound('intro.mp3')
def musicthread():
	global thread1
	thread1=threading.Thread(target=music)
	thread1.start()
musicthread()
anim()
root.mainloop()
