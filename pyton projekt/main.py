import tkinter
import sqlite3
from tkinter import messagebox
from tkinter import ttk
import json
cnt=sqlite3.connect("unversit.db")
cursor=cnt.cursor()
#-----------sign up----------
def login():
    user=txt_user.get()
    pas=txt_pas.get()
    if user==user and pas==pas:
       
        lbl_msg.configure(text="login succeseful")
        win=tkinter.Tk()
        win.title("choose units")
        win.geometry("400x300")
        #------------------------
        lbl_units=tkinter.Label(win,text="choose units")
        lbl_units.pack()
        txt_units=tkinter.Entry(win)
        txt_units.pack()
        #-----------READ JSON
        with open ('final.json')as f:
            
            z=cursor.execute('''SELECT *FROM units WHERE id=? AND studies=? AND number=? 
                              AND time=? AND teacher=? ''')
           
            rows=cursor.fetchall()            
            
            json.dump(z,f)
        #-----------------------
        btn_pik=tkinter.Button(win,text="choose")
        btn_pik.pack()
        
        #--------------------------------
        btn_show=tkinter.Button(win,text="show")
        btn_show.pack()
        #-----------READ JSON
        with open ('final.json')as f:
            final=json.load(f)
        print(final)
        win.mainloop
        #-------------------------------
        win=tkinter.Tk()
        win.title("all units")
        win.geometry("600x500")
        #------------------------
        
        tree=ttk.Treeview(win,columns=('id','studies','number','time','teacher')
        ,show='headings')
        tree.heading('id',text='id')
        tree.heading('studies',text='studies')
        tree.heading('number',text='number')
        tree.heading('time',text='time')
        tree.heading('teacher',text='teacher')
        tree.pack()
        cursor.execute('''SELECT * FROM units''')
        rows=cursor.fetchall()
        for row in rows:
            tree.insert('','end','values=row')
        win.mainloop()
    else:
        lbl_msg.configure(text="wrong password or username!")
    #-----------read sql-----------
    cursor.execute('''SELECT * FROM student ''')
    rows=cursor.fetchall()   
    
    
    
#----------submit-----------
def submit(): 
    user=txt_user.get()
    pas=txt_pas.get()
    
    cursor.execute('''INSERT INTO student(user,pas)VALUES(?,?),(user,pas)''')
    cnt.execute(cursor(user,pas))
    cnt.commit()
    
    

win= tkinter.Tk()
win.title("azad unversit")
win.geometry("600x500")

lbl_user=tkinter.Label(win,text="user")
lbl_user.pack()
txt_user=tkinter.Entry(win)
txt_user.pack()
#------------------------------
lbl_pas=tkinter.Label(win,text="pas")
lbl_pas.pack()
txt_pas=tkinter.Entry(win)
txt_pas.pack()
#---------bottun-----------
btn_login=tkinter.Button(win,text="login",command=login)
btn_login.pack()
btn_submit=tkinter.Button(win,text="submit",command=submit)
btn_submit.pack()

lbl_msg=tkinter.Label(win,text="")
lbl_msg.pack()


win.mainloop()
#ostad man va dostam dige harkari kardim natonestim beyn database va tkinter etesal dorost konim
#khastim as tkinter berizim to note bad az onja berizim to sql vali khob soal ino nakhaste bood