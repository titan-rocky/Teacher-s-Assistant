'''
this is the main page that loads all
the app starts with login
'''
import sys
import csv
import time
import mysql.connector
import tkinter as tk
from tkinter import messagebox

def login():
    logindoc=open('login.csv','r',newline='\n')
    l2reader=csv.reader(logindoc)
    loginreader=[i for i in l2reader][1:]
    root=tk.Tk()
    root.resizable(False, False)
    bgd='#101f2f'

    try:
        mycon=mysql.connector.connect(user='root',password='manager',host='localhost')
    except mysql.connector.errors.DatabaseError:
        print('Can\'t Connect to Server')
        root.destroy()
        sys.exit()
    #main config
    root.iconbitmap('icon.ico')
    root.title('Teacher\'s Assistant')
    root.config(background=bgd)
    scwidth=root.winfo_screenwidth()
    scheight=root.winfo_screenheight()
    winwid=570
    winhei=380
    xcor=scwidth/2-winwid/2-20
    ycor=scheight/2-winhei/2-30
    root.geometry('%dx%d+%d+%d'%(winwid,winhei,xcor,ycor))

    label_fg='#992c2d'
    #title text
    titleof_font='bebas neue'
    titleof=tk.Label(root,text="Welcome to",font=('garamond',18),fg='#3caea3',bg=bgd)
    titleof.grid(row=0,column=0,columnspan=3,padx=25,sticky='s')
    titleof2=tk.Label(root,text="Teacher\'s Assistant",font=(titleof_font,30),fg='#3caea3',bg=bgd)
    titleof2.grid(row=1,column=0,columnspan=3,padx=25)

    userframe=tk.Frame(root,bg=bgd)
    userframe.grid(row=2,column=0,columnspan=3,padx=25,pady=10)
    #username
    userempty=tk.Label(userframe,text='             ',fg=label_fg,bg=bgd,font=('century gothic italic',15))
    userempty.grid(row=0,column=1,pady=15)
    userlabel=tk.Label(userframe,text='Enter the username : ',fg=label_fg,bg=bgd,font=('garamond',18))
    userlabel.grid(row=0,column=0,pady=15,sticky='w')
    username=tk.Entry(userframe,fg='#000000',font=('arial',9))
    username.grid(row=0,column=2,padx=10,pady=15,columnspan=2,sticky='w')

    #password
    passlabel=tk.Label(userframe,text='Enter the password : ',fg=label_fg,bg=bgd,font=('garamond',18))
    passlabel.grid(row=1,column=0,pady=15)
    password=tk.Entry(userframe,fg='#000000',font=('arial',9),show='*')
    password.grid(row=1,column=2,padx=10,pady=15,columnspan=2,sticky='w')

    d_fg='#4d99ba'
    d_font='blackchancery'
    d_font_size=17
    d_pady=10

    d=tk.Label(root,text='Note: The credentials are case sensitive!',font=(d_font,d_font_size),fg=d_fg,bg=bgd,pady=d_pady)
    d.grid(row=3,column=0,columnspan=3)

    #login button function
    def on_login_click(*a):
        global userdata;global passdata
        userdata=username.get()
        passdata=password.get()
        #d.grid_forget()
        found=0
        for j in loginreader:
            #username
            if userdata==j[0] and userdata!='' :
                found=1
                #password
                if j[1]==passdata:
                    d.config(text=f'Welcome {userdata} !')
                    root.update()
                    time.sleep(2)
                    from welcome import welcometo
                    root.withdraw()
                    welcometo(userdata,passdata)
                    return 

                elif passdata=='':
                    d.config(text='Please enter a valid Password') 
                    found=1
                    break
                else:
                    d.config(text='Incorrect Password')
                    found=1
                    break

            elif userdata=='':
                d.config(text='Please enter a valid Username')
                found=1
                break

            else:
                found=0

        if found==0:
            d.config(text=f'Username {userdata} is not found !')
            pass
        username.delete('0','end')
        password.delete('0','end')


    #buttonframe
    buttonframe=tk.Frame(root,bg=bgd)
    buttonframe.grid(row=5,columnspan=3,padx=20,pady=20)
    button_fg='#124183'
    button_bg='#c4b480'
    button_font='garamond'
    button_activebg=bgd
    button_activefg='#c4b480'
    button_size=12
    #login button
    loginb=tk.Button(buttonframe,text='Login',command=on_login_click,bg=button_bg,fg=button_fg,activebackground=button_activebg,activeforeground=button_activefg,font=(button_font,button_size),padx=20,pady=5)
    loginb.grid(row=3,column=0,pady=10,padx=10)

    #create account button function
    def on_create_click():
        time.sleep(1.5)
        from creaccnt import click
        root.withdraw()
        B=click(mycon,root)
        if B==1:
            root.deiconify()

    #create account button 
    loginb2=tk.Button(buttonframe,text='Create a New Account',command=on_create_click,bg=button_bg,fg=button_fg,activebackground=button_activebg,activeforeground=button_activefg,font=(button_font,button_size),padx=30,pady=5)
    loginb2.grid(row=3,column=1,pady=10,padx=10)


    #import forgotpsw
    #forgot psw button function
    def on_forgot_click():
        root.withdraw()
        from forgotpsw import forgotpswd
        forgotpswd(root)


    #forgot psw account button 
    loginb3=tk.Button(buttonframe,text='Forgot Password',command=on_forgot_click,bg=button_bg,fg=button_fg,activebackground=button_activebg,activeforeground=button_activefg,font=(button_font,button_size),padx=20,pady=5)
    loginb3.grid(row=3,column=2,pady=10,padx=10)

    def onclose():
        d=messagebox.askokcancel('Quit','Do you want to quit ?')
        if d:
            mycon.close()
            logindoc.close()
            root.destroy()
            sys.exit()



    root.protocol('WM_DELETE_WINDOW',onclose)

    tk.mainloop()
