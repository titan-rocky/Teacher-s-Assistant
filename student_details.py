import tkinter as tk
import mysql.connector
import csv

#def st_detail():

bgd='#101f2f';fgd='magenta'
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

mycon=mysql.connector.connect(user='jeff',password='thexactr',database='jeff_db')
cur=mycon.cursor()

cur.execute('SELECT * FROM student_details')

stname_label=tk.Label(det,text='Enter the name of the student : ',fg=fgd,bg=bgd)
stname_label.grid(row=0,column=0,padx=10,sticky='we')
student_ent=tk.Entry(det);student_ent.grid(row=0,column=1)
stadmin_label=tk.Label(det,text='Enter the Admission Number of the student : ',fg=fgd,bg=bgd)
stadmin_label.grid(row=1,column=0,padx=10)
stadmin_ent=tk.Entry(det);stadmin_ent.grid(row=1,column=1)

for i in cur.fetchall():
	pass


det.mainloop()