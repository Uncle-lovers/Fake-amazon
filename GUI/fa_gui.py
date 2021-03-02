import tkinter as tk  #Imports tkinter; the gui package
from tkinter import messagebox #imports the messagebox module within tkinter
import sys                     #required for sys.exit()
import time
#import {backend module}     #custom made sql connectivity module


HEIGHT=700  #var for height and width  (makes life easier by specifying here)
WIDTH=800


mainbg='#8AFF33' #pick hexadecimal code for colour later guys)


uname=""        #global variable for username

pid=""          #global variable for product ID

prodlist=["product1","product2","product3","product4","product5","product6"] #names of products

f=open("desc.txt",'r')
desclist=f.read()
desclist=desclist.split("|pogline|")        #collects product descriptions

f.close()

def on_closing():          #function activates when window is closed
    if messagebox.askokcancel("Quit", "Do you want to quit?"):    #spawns messagebox asking if willing to quit
        root.destroy()             #destroys root window
        sys.exit()                   #exits






#functions for switching pages

def storefunc():       #goes to store
	page=storepg()
			    

def item(x):				#goes to specified item
    page=itempg(x)

def buy(x):                   #goes to buy page of specified item
    page=buypg(x)



#Python Object Oriented Programming; also known as POOP


class homepg():   #a class created for the homepage, check out POOP if you dont understand this; or ask me, i know a lot about POOP!

    def __init__(self): # runs when object is created

        def helpinfo():
            messagebox.showinfo("Help","""Welcome to our store (fill this part)
cash on delivery only
Team members
============
Joshua Sheron
Pradeesh D
Pranav H P
Rishikeswaran (correct spelling if wrong)

                """)

        def verify(username,passcode):           #checks if entered credentials are correct
			#"cred={collect tuples from database}"

            if username=="admin" and passcode=="root":
                print('root mode activated') # add root account functionality
			
            elif username=="pranav" and passcode=="pass": #just for debugging
                global uname
                uname=username           
            

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
            if username.strip()=="" or passcode.strip()=="":
                messagebox.showinfo("Alert","Blank username/password found")
            
            #elif {check if username already exists in the database}:
                #messagebox.showinfo("Alert","user already exists")

            else: 
                print(f"user:{username}")
                print(f"pass:{passcode}")

                #add details to database
                global uname
                
                uname=username           
                


                mainlabel['text']="Successful...redirecting"    #fancy hoohoooo
                time.sleep(0.1) 
                mainlabel['text']="Successful...redirecting."
                time.sleep(0.1)
                mainlabel['text']="Successful...redirecting.."
                time.sleep(0.1)
                mainlabel['text']="Successful...redirecting..."
                time.sleep(0.1)
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

        helpbutt=tk.Button(frame,text="help",font="Roboto 20",bg="white",fg="black",command=lambda:helpinfo())
        helpbutt.place(relx=0.01,rely=0.21,relwidth=0.15,relheight=0.05) #places button in the window

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


        item1=tk.Button(frame,text="Item1",font="Roboto 20",bg="white",fg="black",command=lambda:item(1))
        item1.place(relx=0.15,rely=0.3,relwidth=0.2,relheight=0.1)

        item2=tk.Button(frame,text="Item2",font="Roboto 20",bg="white",fg="black",command=lambda:item(2))
        item2.place(relx=0.65,rely=0.3,relwidth=0.2,relheight=0.1)

        item3=tk.Button(frame,text="Item3",font="Roboto 20",bg="white",fg="black",command=lambda:item(3))
        item3.place(relx=0.15,rely=0.5,relwidth=0.2,relheight=0.1)

        item4=tk.Button(frame,text="Item4",font="Roboto 20",bg="white",fg="black",command=lambda:item(4))
        item4.place(relx=0.65,rely=0.5,relwidth=0.2,relheight=0.1)

        item5=tk.Button(frame,text="Item5",font="Roboto 20",bg="white",fg="black",command=lambda:item(5))
        item5.place(relx=0.15,rely=0.7,relwidth=0.2,relheight=0.1)

        item6=tk.Button(frame,text="Item6",font="Roboto 20",bg="white",fg="black",command=lambda:item(6))
        item6.place(relx=0.65,rely=0.7,relwidth=0.2,relheight=0.1)



class itempg():
    def __init__(self,itemno):

        try:               #deletes previous frames if any previous frames exist
            frame.destroy()		 
        except:			
            pass
        
                       
        frame=tk.Frame(root,bg=mainbg)
        frame.place(relx=0,rely=0,relwidth=1,relheight=1)   

        
        global pid

        pid=prodlist[itemno-1] #gets the name of item

        proddesc=desclist[itemno-1]  #gets the name of description

        label=tk.Label(frame,text=f"{pid}",font="Roboto 40",bg="green")                    
        label.place(relx=0,rely=0,relwidth=1,relheight=0.2)


        desclabel=tk.Label(frame,text=f"{proddesc}",font="Roboto 15",bg=mainbg)                    
        desclabel.place(relx=0.45,rely=0.2,relwidth=0.5,relheight=0.7)

        buybutt=tk.Button(frame,text="buy",font="Roboto 20",bg="#ffff28",fg="black",command=lambda:buy(itemno))
        buybutt.place(relx=0.65,rely=0.85,relwidth=0.2,relheight=0.1)

        backbutt=tk.Button(frame,text="<- back to store",font="Roboto 10",bg="white",fg="black",command=lambda:storefunc())
        backbutt.place(relx=0.01,rely=0.21,relwidth=0.15,relheight=0.05) 

class buypg():
    def __init__(self,itemno):

        def order(add,ph):
            if add.strip()=="" or ph.strip()=="":
                messagebox.showinfo("Alert","address/phone number is blank!")


            else:
                
                print(f"name:{uname},product:{pid},address:{add},phone:{ph}") #replace with db entry

                messagebox.showinfo("Alert","Successful!")
                storefunc()
        
        if messagebox.askyesno("Alert",f"Do you want to purchase {pid}"):    #spawns messagebox asking if willing to quit
            
            try:               #deletes previous frames if any previous frames exist
                frame.destroy()      
            except:         
                pass
        

            frame=tk.Frame(root,bg=mainbg)
            frame.place(relx=0,rely=0,relwidth=1,relheight=1)   

            label=tk.Label(frame,text=f"Enter your details {uname}",font="Roboto 40",bg="green")                    
            label.place(relx=0,rely=0,relwidth=1,relheight=0.2)

            alabel=tk.Label(frame,text=f"Enter your address",font="Roboto 10",bg=mainbg)                    
            alabel.place(relx=0,rely=0.3,relwidth=1,relheight=0.05)

            adentry=tk.Entry(frame,bg="white",fg="black",font="Roboto 15") #address entry
            adentry.place(relx=0.25,rely=0.4,relwidth=0.5,relheight=0.075)

            plabel=tk.Label(frame,text=f"Enter your phone number",font="Roboto 10",bg=mainbg)                    
            plabel.place(relx=0,rely=0.5,relwidth=1,relheight=0.05)

            pentry=tk.Entry(frame,bg="white",fg="black",font="Roboto 15") #phone num entry
            pentry.place(relx=0.25,rely=0.6,relwidth=0.5,relheight=0.075)

            finalbutt=tk.Button(frame,text="buy",bg="white",fg="black",command=lambda:order(adentry.get(),pentry.get()))
            finalbutt.place(relx=0.45,rely=0.7,relwidth=0.1,relheight=0.1)

            cancelbutt=tk.Button(frame,text="cancel",font="Roboto 10",bg="white",fg="black",command=lambda:item(itemno))
            cancelbutt.place(relx=0.01,rely=0.21,relwidth=0.15,relheight=0.05) 

        else:
            item(itemno)
                
        
            




root=tk.Tk()   #makes a root window 
root.title("Name of our company") #changes the title of the window (PICK NAME PLEASE)
#root.iconbitmap("logo.ico")      #sets window icon (please make ideas for icon)

canvas=tk.Canvas(root, height=HEIGHT,width=WIDTH) #creates a canvas
canvas.pack()#adds the canvas to the root window



page=homepg() #creates page object


root.protocol("WM_DELETE_WINDOW", on_closing)  #checks if close button is pressed or not
root.mainloop() #runs app
