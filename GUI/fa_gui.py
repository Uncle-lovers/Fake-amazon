import tkinter as tk  #Imports tkinter; the gui package
from tkinter import messagebox #imports the messagebox module within tkinter
import sys                     #required for sys.exit()
import time
#import {backend module}     #custom made sql connectivity module


HEIGHT=700  #var for height and width  (makes life easier by specifying here)
WIDTH=800


mainbg='#8AFF33' #pick hexadecimal code for colour later guys)


uname=""        #global variable for username
phonenum=""     #global variable for phone num
pid=""          #global variable for product ID



def on_closing():          #function activates when window is closed
    if messagebox.askokcancel("Quit", "Do you want to quit?"):    #spawns messagebox asking if willing to quit
        root.destroy()             #destroys root window
        sys.exit()                   #exits






#functions for switching pages

def storefunc():       #goes to store
	page=storepg()
			    

def item(x):				#goes to specified item
    page=itempg(x)

def buy(x):                   #does to buy page of specified item
    page=buypg(x)



#Python Object Oriented Programming; also known as POOP


class homepg():   #a class created for the homepage, check out POOP if you dont understand this; or ask me, i know a lot about POOP!

    def __init__(self): # runs when object is created

        def verify(username,passcode):           #checks if entered credentials are correct
			#"cred={collect tuples from database}"

            if username=="admin" and passcode=="root":
                print('root mode activated') # add root account functionality
			
            elif username=="pranav" and passcode=="pass": #just for debugging
                uname=username           
                phonenum=passcode
                storefunc()

            else:
                mainlabel['text']="Please enter valid credentials"
		
			#elif if (username,passcode) in cred:
			
				#global uname
				#global phonenum
				#uname=username			
				#phonenum={value form rishi}

				#storefunc()  #goes to store page
        
        def signup(username,passcode):

            #add details to database
            global uname
            global phonenum
            uname=username           
            phonenum=passcode


            mainlabel['text']="Successful...redirecting"    #fancy hoohoooo
            time.sleep(0.5) 
            mainlabel['text']="Successful...redirecting."
            time.sleep(0.5)
            mainlabel['text']="Successful...redirecting.."
            time.sleep(0.5)
            mainlabel['text']="Successful...redirecting..."
            time.sleep(0.5)
            storefunc()

        try:               #deletes previous frames if any previous frames exist
            frame.destroy()		 
        except:			
            pass
    
        frame=tk.Frame(root,bg=mainbg)#creates a frame  (
        frame.place(relx=0,rely=0,relwidth=1,relheight=1)  #width and height goes from 0-1 where 1 is filling the entire thing

        
        mainlabel=tk.Label(frame,text="Welcome to Uncle's market!",font="Roboto 40",bg="green")#creates text area
        mainlabel.place(relx=0,rely=0,relwidth=1,relheight=0.2)#places it in frame

        uentry=tk.Entry(frame,bg="white",fg="black",font="Roboto 15") #entry field
        uentry.place(relx=0.25,rely=0.4,relwidth=0.5,relheight=0.075)

        pentry=tk.Entry(frame,bg="white",fg="black",font="Roboto 15") #entry field
        pentry.place(relx=0.25,rely=0.5,relwidth=0.5,relheight=0.075)

        startbutt=tk.Button(frame,text="Log in",font="Roboto 20",bg="white",fg="black",command=lambda:verify(uentry.get(),pentry.get()))
        startbutt.place(relx=0.55,rely=0.75,relwidth=0.3,relheight=0.1) #places button in the window

        signbutt=tk.Button(frame,text="sign up",font="Roboto 20",bg="white",fg="black",command=lambda:signup(uentry.get(),pentry.get()))
        signbutt.place(relx=0.15,rely=0.75,relwidth=0.3,relheight=0.1) #places button in the window


class storepg():   #a class created for the store

    def __init__(self): 

        try:               #deletes previous frames if any previous frames exist
            frame.destroy()		 
        except:			
            pass
    
    
        frame=tk.Frame(root,bg=mainbg)
        frame.place(relx=0,rely=0,relwidth=1,relheight=1)  

        
        label=tk.Label(frame,text="Store",font="Roboto 40",bg="green")
        label.place(relx=0,rely=0,relwidth=1,relheight=0.2)


        item1=tk.Button(frame,text="Item1",bg="white",fg="black",command=lambda:item(1))
        item1.place(relx=0.45,rely=0.5,relwidth=0.1,relheight=0.1)


class itempg():
    def __init__(self,itemno):

        try:               #deletes previous frames if any previous frames exist
            frame.destroy()		 
        except:			
            pass
        
                       
        frame=tk.Frame(root,bg=mainbg)
        frame.place(relx=0,rely=0,relwidth=1,relheight=1)   

        if itemno==1:
            global pid

            pid="item1"

            label=tk.Label(frame,text=f"item{itemno}",font="Roboto 40",bg="green")                    
            label.place(relx=0,rely=0,relwidth=1,relheight=0.2)


            buybutt=tk.Button(frame,text="buy",bg="white",fg="black",command=lambda:buy(1))
            buybutt.place(relx=0.45,rely=0.5,relwidth=0.1,relheight=0.1)


def buypg():
    def __init__(self,itemno):
        
        if not(messagebox.askyesno(f"Do you want to purchase item{itemno}")):    #spawns messagebox asking if willing to quit
            pass


        else:

                
        
            try:               #deletes previous frames if any previous frames exist
                frame.destroy()		 
            except:			
                pass
    	

        frame=tk.Frame(root,bg=mainbg)
        frame.place(relx=0,rely=0,relwidth=1,relheight=1)   

        label=tk.Label(frame,text=f"Enter your details",font="Roboto 40",bg="green")                    
        label.place(relx=0,rely=0,relwidth=1,relheight=0.2)




root=tk.Tk()   #makes a root window 
root.title("Name of our company") #changes the title of the window (PICK NAME PLEASE)
#root.iconbitmap("logo.ico")      #sets window icon (please make ideas for icon)

canvas=tk.Canvas(root, height=HEIGHT,width=WIDTH) #creates a canvas
canvas.pack()#adds the canvas to the root window



page=homepg() #creates page object


root.protocol("WM_DELETE_WINDOW", on_closing)  #checks if close button is pressed or not
root.mainloop() #runs app
