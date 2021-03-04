import tkinter as tk
from tkinter import filedialog,Text
import tkinter.font as tkFont
import os
from PIL import ImageTk,Image
import pyglet#different library for gif
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,NavigationToolbar2Tk)
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure
import matplotlib.animation as animation#for gif color
from matplotlib import style
from sklearn.preprocessing import PolynomialFeatures  
from sklearn import linear_model
from pygame import quit


root=tk.Tk()
style.use('ggplot')


def perform():
	if v1.get() is 1:
		animation=pyglet.image.load_animation('covid.gif')
		animSprite=pyglet.sprite.Sprite(animation)
		w=animSprite.width
		h=animSprite.height
		window=pyglet.window.Window(width=w,height=h)
		pyglet.gl.glClearColor(0.5,0.5,0.8,0.5)
		@window.event
		def on_draw():
			window.clear()
			animSprite.draw()
		pyglet.app.run()# for run
	elif v1.get() is 2:#2 is option 2
		win=tk.Tk()
		w1= tk.Canvas(win, bg="purple",height=800,width=700)
		w1.place(x=300,y=10) 
		f=Figure(figsize=(5,5),dpi=100)

		data=pd.read_csv(r"C:\Users\Pratiksha\Downloads\total_cases.csv",sep =',')
		data=data[['id','World']]
		x=np.array(data['id']).reshape(-1,1)
		y=np.array(data['World']).reshape(-1,1)
		f.clear()
		f.add_subplot(111).plot(x,y,"-m")# csv file values before prediction - means --line
		polyFeat=PolynomialFeatures(degree=4)#polynominal equation for degree for cut cut line degree 4
		x=polyFeat.fit_transform(x)#for line
		model=linear_model.LinearRegression()#we use multiple values of x multiple=polynomial
		model.fit(x,y)#value puted x,y
		accurency=model.score(x,y)#it told how accurate the prediction
		y0 =model.predict(x)#x=total cases y0 predicted 
		f.add_subplot(111).plot(y0,"--b")
		chart=FigureCanvasTkAgg(f,win)
		chart.get_tk_widget().place(x=400,y=50)
		main = tk.Label(win,text='PREDICTION',bg='black',fg='white',padx=20,font=fontStyle,height=2,width=60)
		main.place(x=302,y=0)
		lab = tk.Label(win,text='Enter days:',bg='black',fg='white',padx=20)
		lab.place(x=460,y=580)
		e1=tk.Entry(win)
		def number():
			try:
				days=int(e1.get())
				pre=(round(int(model.predict(polyFeat.fit_transform([[293+days]])))/1000000,2),'M')#uses polynominal regression 293 becz according data on file 10000000,2 for mean calculations x and y it is polynolial formula M=concat
				lab2.config(text=pre)
				x1=np.array(list(range(1,234+days))).reshape(-1,1)
				y1=model.predict(polyFeat.fit_transform(x1))
				f.add_subplot(111).plot(y1,"--r")#days
				f.add_subplot(111).plot(y0,"--b")#y0 clean 
				chart=FigureCanvasTkAgg(f,win)
				chart.get_tk_widget().place(x=400,y=50)
			except ValueError:
				lab1.config(text='Not A Number')
				lab2.config(text='    ')
		e1.place(x=570,y=580)
		but=tk.Button(win,text='SHOW',bg='black',fg='white',padx=20,command=number)
		but.place(x=610,y=620)
		lab1 = tk.Label(win,text='PREDICTION :',bg='black',fg='white',padx=20)
		lab1.place(x=700,y=580)
		lab2=tk.Label(win,text='    ',bg='white',fg='purple')
		lab2.place(x=820,y=580)
	elif v1.get() is 3:
		root1=tk.Tk()
		
		def prv():
		
			fontStyle2=tk.font.Font(family="Lucida Grande",size=60)
			label=tk.Label(root1,text="To prevent infection and to slow transmission of COVID-19,take the following precautions :\n\n\n*Wash your hands regularly with soap and water, or clean them with alcohol-based hand rub.""\t\n\n*Maintain 1 metre distance between you & people coughing or sneezing.Avoid touching your face.\n\n*Cover your mouth and nose when coughing or sneezing.Stay home if you feel unwell.\n\n*Refrain from smoking and other activities that weaken the lungs.\n\n*Practice physical distancing by avoiding unnecessary travel \nand staying away from large groups of people.",
			foreground="purple",
    		background="black",
    		font="fontStyle2",
    		width=90,height=23
    		)
			label.place(x=160,y=70)
			l1=tk.Label(root1,text="PREVENTION",foreground='black',background='purple',width=90,height=3,font=fontStyle2)
			l1.place(x=160,y=70)
		prv()
	elif v1.get() is 4:
		root1=tk.Tk();
		def sym():
			
			fontStyle2=tk.font.Font(family="Lucida Grande",size=40)
			label=tk.Label(root1,text="## COVID-19 affects different people in different ways ## \t\n\n\n*Most common symptoms : fever , dry cough , tiredness .\t\n\n\n*Less common symptoms:aches and pains , sore throat , diarrhoea , conjunctivitis , headache ,\n\n\t loss of taste or smell , a rash on skin, or discolouration of fingers or toes.\t\n\n\n*Serious symptoms:difficulty breathing or shortness of breath , chest pain , loss of speech or movement.",
    		foreground="purple",
    		background="black",
    		font="fontStyle2",
    		width=90,height=23)
			label.place(x=160,y=70)
			l1=tk.Label(root1,text="SYMPTOMS",foreground='black',background='purple',width=90,height=3,font=fontStyle2)
			l1.place(x=160,y=70)
		sym()
	elif v1.get() is 5:
		root1=tk.Tk()
		def info():
			
			fontStyle1=tk.font.Font(family="Lucida Grande",size=40)
			label=tk.Label(root1,text="*Coronavirus disease (COVID-19) is an infectious disease caused by a newly discovered coronavirus.\t\n\n*Most people infected with the COVID-19 virus will experience mild to moderate respiratory illness and \nrecover without requiring special treatment. \n\n*Older people, and those with underlying medical problems like cardiovascular disease,diabetes,\nchronic respiratory disease,and cancer are more likely to develop serious illness.\n\n*The best way to prevent and slow down transmission is to be well informed about the COVID-19 virus,\nthe disease it causes and how it spreads.Protect yourself and others from infection by frequently.\n\n*The COVID-19 virus spreads primarily through droplets of saliva or discharge from the nose when an \ninfected person coughs or sneezes,so it’s important that you also practice respiratory etiquette \n(for example, by coughing into a flexed elbow).",
    		foreground="purple",
    		background="black",
    		font="fontStyle1",
    		width=90,height=23)
			label.place(x=160,y=70)
			l1=tk.Label(root1,text="INFORMATION",foreground='black',background='purple',height=3,width=90,font=fontStyle1)
			l1.place(x=160,y=70)
		info()

      
     
		
frame=tk.Frame(root,bg="purple")
w = tk.Canvas(root, bg="black",height=480,width=974) #
frame.place(relwidth=0.8,relheight=0.8,relx=0.1,rely=0.1)
w.place(x=148,y=88)
fontStyle = tkFont.Font(family="Lucida Grande", size=40)
fontStyle1 = tkFont.Font(family="Lucida Grande", size=12)
img = ImageTk.PhotoImage(Image.open("Capture1.png").resize((round(1010) , round(800))))      
w.create_image(470,100, image=img) 
  
label = tk.Label(
    text="COVID-19 DYNAMIC MAPPING OF PROGRESSION AND PREDICTION",
    foreground="purple",  
    background="white",
    font="fontStyle",
    width=88,height=4
    
)
l1 = tk.Label(
    text="  ",
    foreground="white",  
    background="purple"
    
   
    
)
l1.place(x=690,y=253)

l2 = tk.Label(
    text="  ",
    foreground="white",  
    background="purple"
    
   
    
)
l2.place(x=1100,y=253)
label.place(x=150,y=90)
label1 = tk.Label(
    text="Select Your Choice",
    foreground="black" ,
    background="white",
    width=40,
    padx=20,pady=3,
    font=fontStyle1,
    

)
label1.place(x=700,y=250)
v1= tk.IntVar() #to select only one radio button in needed only one int

r1=tk.Radiobutton(root, text='PROGRESSION', var=v1,value=1,bg="white",fg="black")
r2=tk.Radiobutton(root, text='PREDICTION',var=v1,value=2,bg="white",fg="black")
r3=tk.Radiobutton(root,text='PREVENTION',var=v1,value=3,bg='white',fg='black')
r4=tk.Radiobutton(root,text='SYMPTOMS',var=v1,value=4,bg='white',fg='black')
r5=tk.Radiobutton(root,text='INFORMATION',var=v1,value=5,bg='white',fg='black')
r1.place(x=780,y=320)
r2.place(x=920,y=320) 
r3.place(x=780,y=370)
r4.place(x=920,y=370)
r5.place(x=850,y=420)
click=tk.Button(root,text="SUBMIT",fg="white",bg="purple",padx=10,height=2,command=perform)
exit = tk.Button(root, 
                   text="QUIT", 
                   fg="white",bg="purple",height=2,padx=15,
                   command=quit)
exit.place(x=910,y=470)
click.place(x=820,y=470)



root.mainloop()