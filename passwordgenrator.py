from tkinter import *
import string
import random
win=Tk()

def retry():
	global con
	pwd=[]
	for i in range(n):
			pwd.append(random.choice(con))
	pwd1="".join(pwd)
	ent.delete(0,END)
	ent.insert(0,pwd1)
	b.config(text="copy")
	b['state']=NORMAL
	

def trynew():
	gbutton['state']=NORMAL
	sl.set(0)
	cb.set(0)
	cb1.set(0)
	cb2.set(0)
	cb3.set(0)
	ent.delete(0,END)
	cbutton['state']=NORMAL
	cbutton1['state']=NORMAL
	cbutton2['state']=NORMAL
	cbutton3['state']=NORMAL
	slid['state']=NORMAL
	ent['state']=DISABLED
	b['state']=DISABLED
	b1['state']=DISABLED
	b2['state']=DISABLED
	b.config(text="copy")

		
def gen():
	global con
	global n
	pwd=[]
	alp=[]
	num=[]
	Alp=[]
	spe=[]
	if cb.get()==1:
		alp=list(string.ascii_lowercase)
	if cb1.get()==1:
		num=list(string.digits)
	if cb2.get()==1:
		spe=list(string.punctuation)
	if cb3.get()==1:
		Alp=list(string.ascii_uppercase)
	con=alp+num+Alp+spe
	if cb.get()==1 or cb1.get()==1 or cb2.get()==1 or cb3.get()==1:
		n=int(sl.get())
		ent['state']=NORMAL
		for i in range(n):
			pwd.append(random.choice(con))
		pwd1="".join(pwd)
		ent.delete(0,END)
		ent.insert(0,pwd1)
		gbutton['state']=DISABLED
		b1['state']=NORMAL
		b['state']=NORMAL
		b.config(text='copy')
		b2['state']=NORMAL
		cbutton['state']=DISABLED
		cbutton1['state']=DISABLED
		cbutton2['state']=DISABLED
		cbutton3['state']=DISABLED
		slid['state']=DISABLED
		blabel['text']=""
	if cb.get()==0 and cb1.get()==0 and cb2.get()==0 and cb3.get()==0:
		blabel['text']="PLEASE SELECT ANY ONE!!"
		
	
def copy():
	text=ent.get()
	win.clipboard_clear()
	win.clipboard_append(text)
	b.config(text="copied!")
	b.config(state=DISABLED)

#widgets
l=Label(win,text="RANDOM PASSWORD GENRATOR",bg="lime",fg='black',pady=20,padx=20)
ent=Entry(win,width=10,font=('Arial',25),state=DISABLED)
b=Button(win,text="copy",width=10,font=('Arial',10),command=copy,bg="skyblue",fg="black",activeforeground='white',activebackground='black',state=DISABLED,relief=RAISED,bd=10)
b1=Button(win,text='Retry',bg="grey",fg='white',command=retry,state=DISABLED,relief=RAISED,bd=10)
blabel=Label(win,fg="black")
b2=Button(win,text='TRY ANOTHER!',relief=RAISED,bd=10,command=trynew,state=DISABLED,bg="crimson",fg="white")
sl=DoubleVar()#slider
slid=Scale(win,variable=sl,from_=1,to=10,orient=HORIZONTAL,width=30,font=('Arial',10),sliderlength=50,length=300,bd=6,troughcolor="black")
l1=Label(win,text="PASSWORD LENGTH",bg='yellow',fg='black')
l2=Label(win,text="PASSWORD TYPES",bg='yellow',fg="black",font=("",8))
cb=IntVar()
cbutton=Checkbutton(win,text="abc",variable=cb,onvalue=1,offvalue=0)
cb1=IntVar()
cbutton1=Checkbutton(win,text="123",variable=cb1,onvalue=1,offvalue=0)
cb2=IntVar()
cbutton2=Checkbutton(win,text="@#$",variable=cb2,onvalue=1,offvalue=0)
cb3=IntVar()
cbutton3=Checkbutton(win,text='ABC',variable=cb3,onvalue=1,offvalue=0)
gbutton=Button(win,text="GENERATE",width=10,font=('Arial',12),bg='purple',fg='white',command=gen,relief=RAISED,bd=10)
#packing
l.grid(row=0,column=0,padx=10,columnspan=3,pady=(40,10))
ent.grid(row=1,column=0,padx=120,pady=50,columnspan=3)
b.grid(row=3,column=1,pady=20)
b1.grid(row=2,column=1)
b2.grid(row=12,column=1,pady=(80,0),padx=(20,0))
slid.grid(row=5,column=1)
l1.grid(row=4,column=1,pady=(100,10))
l2.grid(row=6,column=1,pady=(100,10))
cbutton.grid(row=7,column=1,pady=(30,0))
cbutton1.grid(row=8,column=1,pady=(30,0))
cbutton2.grid(row=9,column=1,pady=(30,0),padx=(15,0))
cbutton3.grid(row=10,column=1,pady=(30,0),padx=(10,0))
blabel.grid(row=11,column=1,pady=(80,0),padx=(25,0))
gbutton.grid(row=13,column=1,pady=(40,0),padx=(20,0))

win.mainloop()