# -*- coding: utf-8 -*-
"""
Created on Wed Dec 28 11:07:14 2022

@author: ragur
"""

from tkinter import *
import tkinter as tk
from geopy.geocoders import Nominatim
from tkinter import ttk,messagebox
from timezonefinder import TimezoneFinder
from datetime import *
import requests
import pytz
from PIL import Image,ImageTk

root=Tk()

root.title("My Weather app")
root.geometry("890x470+300+300")
root.configure(bg='#333')
root.resizable(False,False)


def getWeather():
    city=textfield.get()
    geolocator=Nominatim(user_agent="geoapiExercises")
    location=geolocator.geocode(city)
    obj=TimezoneFinder()
    
    result=obj.timezone_at(lng=location.longitude, lat=location.latitude)
    timezone.config(text=result)
    log_lat.config(text=f"{round(location.latitude,4)}°N,{round(location.longitude,4)}°E")
    
    home=pytz.timezone(result)
    local_time=datetime.now(home)
    current_time=local_time.strftime("%I:%M %p")
    clock.config(text=current_time)
    
    api="https://api.openweathermap.org/data/3.0/onecall?lat="+str(location.latitude)+"&lon="+str(location.longitude)+"&units=metric&exclude=hourly&appid=7b95cd9e2d4fea1d84580fc0864ea1cd"
    json_data=requests.get(api).json()
    #print(json_data)
    temp=json_data['current']['temp']
    humidity=json_data['current']['humidity']
    pressure=json_data['current']['pressure']
    wind=json_data['current']['wind_speed']
    description=json_data['current']['weather'][0]['description']
    #print(temp)
    
    t.config(text=(temp,"°C"))
    h.config(text=(humidity,"%"))
    p.config(text=(pressure,"hPa"))
    w.config(text=(wind,"m/s"))
    d.config(text=(description))
    
    first=datetime().now()
    day1.config(text=first.strftime("%A"))
    
    second=first+timedelta(days=1)
    day2.config(text=second.strftime("%A"))
    
    third=first+timedelta(days=2)
    day3.config(text=third.strftime("%A"))
    
    fourth=first+timedelta(days=3)
    day4.config(text=fourth.strftime("%A"))
    
    fifth=first+timedelta(days=4)
    day5.config(text=fifth.strftime("%A"))
    
    sixth=first+timedelta(days=5)
    day6.config(text=sixth.strftime("%A"))
    
    seventh=first+timedelta(days=6)
    day7.config(text=seventh.strftime("%A"))
    
image_icon=PhotoImage(file="Images/logo.png")
root.iconphoto(False,image_icon)

Round_box=PhotoImage(file="Images/Rounded Rectangle 1.png")
Label(root,image=Round_box,bg="#333").place(x=30,y=110)

label1=Label(root,text="Temperature",font=('Helvetica',11),fg="#fff",bg='#203243')
label1.place(x=50,y=120)

label2=Label(root,text="Humidity",font=('Helvetica',11),fg="#fff",bg='#203243')
label2.place(x=50,y=140)

label3=Label(root,text="Pressure",font=('Helvetica',11),fg="#fff",bg='#203243')
label3.place(x=50,y=160)

label4=Label(root,text="Wind",font=('Helvetica',11),fg="#fff",bg='#203243')
label4.place(x=50,y=180)

label5=Label(root,text="Description",font=('Helvetica',11),fg="#fff",bg='#203243')
label5.place(x=50,y=200)

search_image=PhotoImage(file="Images/Rounded Rectangle 3.png")
myimage=Label(image=search_image,bg="#333")
myimage.place(x=270,y=120)

weat_img=PhotoImage(file="Images/Layer 7.png")
weather_img=Label(root,image=weat_img,bg="#203243")
weather_img.place(x=290,y=127)

textfield=tk.Entry(root,justify='center',width=15,font=('poppins',25,'bold'),bg='#203243',border=0,fg='white')
textfield.place(x=370,y=130)
textfield.focus()

search_icon=PhotoImage(file="Images/Layer 6.png")
img_icon=Button(image=search_icon,borderwidth=0,cursor='hand2',bg="#203243",command=getWeather)
img_icon.place(x=645,y=125)

frame=Frame(root,width=900,height=180,bg="#212120")
frame.pack(side=BOTTOM)

firstbox=PhotoImage(file="Images/Rounded Rectangle 2.png")
secondbox=PhotoImage(file="Images/Rounded Rectangle 2 copy.png")

Label(frame,image=firstbox,bg="#212120").place(x=30,y=20)

Label(frame,image=secondbox ,bg="#212120").place(x=300,y=30)
Label(frame,image=secondbox ,bg="#212120").place(x=400,y=30)
Label(frame,image=secondbox ,bg="#212120").place(x=500,y=30)
Label(frame,image=secondbox ,bg="#212120").place(x=600,y=30)
Label(frame,image=secondbox ,bg="#212120").place(x=700,y=30)
Label(frame,image=secondbox ,bg="#212120").place(x=800,y=30)



clock=Label(root,font=("Helvetica",30,"bold"),fg="#fff",bg="#333")
clock.place(x=30,y=20)

timezone=Label(root,font=("Helvetica",20),fg="#fff",bg="#333")
timezone.place(x=700,y=20)

log_lat=Label(root,font=("Helvetica",10),fg="#fff",bg="#333")
log_lat.place(x=700,y=50)

t=Label(root,font=("Helvetica",11),fg="#fff",bg="#203243")
t.place(x=150,y=120)
h=Label(root,font=("Helvetica",11),fg="#fff",bg="#203243")
h.place(x=150,y=140)
p=Label(root,font=("Helvetica",11),fg="#fff",bg="#203243")
p.place(x=150,y=160)
w=Label(root,font=("Helvetica",11),fg="#fff",bg="#203243")
w.place(x=150,y=180)
d=Label(root,font=("Helvetica",11),fg="#fff",bg="#203243")
d.place(x=150,y=200)

firstframe=Frame(root,width=230,height=132,bg="#282829")
firstframe.place(x=35,y=315)

day1=Label(firstframe,font="arial 20",bg='#282829',fg="#fff")
day1.place(x=100,y=5)

firstimage=Label(firstframe,bg="#282829")
firstimage.place(x=1,y=15)

secondframe=Frame(root,width=70,height=115,bg="white")
secondframe.place(x=305,y=325)

da2=Label(firstframe,font="arial 20",bg='#282829',fg="#fff")
day2.place(x=10,y=5)

thirdframe=Frame(root,width=70,height=115,bg="white")
thirdframe.place(x=405,y=325)

day3=Label(firstframe,font="arial 20",bg='#282829',fg="#fff")
day3.place(x=10,y=5)

fourthframe=Frame(root,width=70,height=115,bg="white")
fourthframe.place(x=505,y=325)

day4=Label(firstframe,font="arial 20",bg='#282829',fg="#fff")
day4.place(x=10,y=5)

fifthframe=Frame(root,width=70,height=115,bg="white")
fifthframe.place(x=605,y=325)

day5=Label(firstframe,font="arial 20",bg='#282829',fg="#fff")
day5.place(x=10,y=5)

sixthframe=Frame(root,width=70,height=115,bg="white")
sixthframe.place(x=705,y=325)

day6=Label(firstframe,font="arial 20",bg='#282829',fg="#fff")
day6.place(x=10,y=5)

seventhframe=Frame(root,width=70,height=115,bg="white")
seventhframe.place(x=805,y=325)

day7=Label(firstframe,font="arial 20",bg='#282829',fg="#fff")
day7.place(x=10,y=5)

root.mainloop()