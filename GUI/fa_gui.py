import tkinter as tk  #Imports tkinter; the gui package
from tkinter import messagebox #imports the messagebox module within tkinter
import sys                     #required for sys.exit()
import time
import login     #custom made sql connectivity module



HEIGHT=1280  #var for height and width  (makes life easier by specifying here)
WIDTH=720


#mainbg='#8AFF33' #pick hexadecimal code for colour later guys)
mainbg='white'

labelcol='#131921'

buttoncol="#a2b4f0"

ltextcol="white"
uname=""        #global variable for username

pid=""          #global variable for product ID

prodlist=[("ALPHA","7,499"),("TAPTIME","10,000"),("JHOSHLET","1"),("PORTCOMP","69"),("EECHO BOX","2,500"),("GLAREELS","999999")] #names of products


f=open("desc.txt",'r')
desclist=f.read()
desclist=desclist.split("|pogline|")        #collects product descriptions

f.close()




def on_closing():          #function activates when window is closed
    if messagebox.askokcancel("Quit", "Do you want to quit?"):    #spawns messagebox asking if willing to quit
        root.destroy()             #destroys root window
        sys.exit()                   #exits






#functions for switching pages

def logout(): #go to home page
    page=homepg()

def becomebezos():   #become the all-powerful jeff bezos
    page=adminpg()

def storefunc():       #goes to store
	page=storepg()
			    

def item(x):				#goes to specified item
    page=itempg(x)

def buy(x):                   #goes to buy page of specified item
    page=buypg(x)



#I do not know much about OOP so please excuse me 

class homepg():   #a class created for the home page

    def __init__(self): # runs when object is created

        def helpinfo():
            messagebox.showinfo("Help","""Welcome to our store (fill this part)
Cash on delivery only
All deliveries take place within two days!!!
Due to the current pandemic and the international silicon shortage,
all orders are limited to one item



Team members
============
Joshua Sheron D
Pradeesh D
Pranav H P
Rishikeswaran V""")

        def verify(username,passcode):           #checks if entered credentials are correct
            global uname

            if username=="admin" and passcode=="root":
                becomebezos()
			
            elif login.credentialsP(username,passcode): #for log in
            	
            	uname=username

            	storefunc()

            else:
                mainlabel['text']="Please enter valid credentials"
		
        
        def signup(username,passcode):
            if username.strip()=="" or passcode.strip()=="":
                messagebox.showinfo("Alert","Blank username/password found")
            
            elif username=='admin':
                mainlabel["text"]=="Invalid username"

            elif login.credentialsE(username,passcode): #gives true if there is no username clash 
                
            
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

            else:
                mainlabel["text"]=="Username already exists!"

        try:               #deletes previous frames if any previous frames exist
            frame.destroy()		 
        except:			
            pass
    
        frame=tk.Frame(root,bg=mainbg)#creates a frame  (
        frame.place(relx=0,rely=0,relwidth=1,relheight=1)  #width and height goes from 0-1 where 1 is filling the entire thing

        global background_image
        
        background_image = tk.PhotoImage(file='bgblue.png')
        background_label = tk.Label(frame, image=background_image)
        background_label.place(relwidth=1, relheight=1)
        
        mainlabel=tk.Label(frame,text="ZapZonics",font="APlayfairDisplay 40",justify="left",bg=labelcol,fg=ltextcol)#creates text area
        mainlabel.place(relx=0,rely=0,relwidth=1,relheight=0.1)#places it in frame

        #sublabel=tk.Label(frame,text="login",font="Roboto 40",bg="grey",fg=ltextcol)#creates text area
        #sublabel.place(relx=0,rely=0.1,relwidth=1,relheight=0.1)

        uentry=tk.Entry(frame,bg=buttoncol,fg="black",font="Roboto 15") #entry field
        uentry.place(relx=0.25,rely=0.4,relwidth=0.5,relheight=0.075)

        pentry=tk.Entry(frame,bg=buttoncol,fg="black",show='*',font="Roboto 15") #entry field
        pentry.place(relx=0.25,rely=0.5,relwidth=0.5,relheight=0.075)

        startbutt=tk.Button(frame,text="Log in",font="Roboto 20",bg=buttoncol,fg="black",command=lambda:verify((uentry.get()).strip(),(pentry.get()).strip()))
        startbutt.place(relx=0.55,rely=0.75,relwidth=0.3,relheight=0.1) #places button in the window

        signbutt=tk.Button(frame,text="sign up",font="Roboto 20",bg=buttoncol,fg="black",command=lambda:signup((uentry.get()).strip(),(pentry.get()).strip()))
        signbutt.place(relx=0.15,rely=0.75,relwidth=0.3,relheight=0.1) #places button in the window

        helpbutt=tk.Button(frame,text="help",font="Roboto 20",bg=buttoncol,fg="black",command=lambda:helpinfo())
        helpbutt.place(relx=0.004,rely=0.11,relwidth=0.15,relheight=0.05) #places button in the window




class adminpg(): #become bezos
    def __init__(self):



        def searchdb(stype,value):


            
            if stype ==0:
                results['text']="Please select an option"
            elif value.strip()=="":
                results['text']="Please enter a search term"

            else:
                res=login.search(stype,value)

                gap=" "*20
                searchres="username"+gap+"product"+gap+"price"+gap+"address"+gap+"phonenum\n"# string for containing values
                

                for i in res:
                    searchres+="\n"
                    for j in i:
                        searchres+=j+gap
                    

                if searchres.strip()=="":
                	results['text']="no results"
                else:
                	results['text']=searchres




        try:               #deletes previous frames if any previous frames exist
            frame.destroy()      
        except:         
            pass

        frame=tk.Frame(root,bg=mainbg)
        frame.place(relx=0,rely=0,relwidth=1,relheight=1)  

        
        label=tk.Label(frame,text="Admin mode",font="Roboto 40",bg=labelcol,fg=ltextcol)
        label.place(relx=0,rely=0,relwidth=1,relheight=0.2)

        options=['Name','Phone no','Address','Product']

        sop=tk.IntVar() #a special variable that holds the options in tkinter

        sop1=tk.Radiobutton(frame,text="Search By Name",variable=sop,value=1,bg=mainbg)
        sop1.place(relx=0.1,rely=0.21)

        sop2=tk.Radiobutton(frame,text="Search By Product",variable=sop,value=2,bg=mainbg)
        sop2.place(relx=0.3,rely=0.21)

        sop3=tk.Radiobutton(frame,text="Search By Price(greater than)",variable=sop,value=3,bg=mainbg)
        sop3.place(relx=0.5,rely=0.21)

        sop4=tk.Radiobutton(frame,text="Search By Address",variable=sop,value=4,bg=mainbg)
        sop4.place(relx=0.7,rely=0.21)

        sop5=tk.Radiobutton(frame,text="Search By Phone No",variable=sop,value=5,bg=mainbg)
        sop5.place(relx=0.1,rely=0.25)

        sop6=tk.Radiobutton(frame,text="Raw sql query",variable=sop,value=6,bg=mainbg)
        sop6.place(relx=0.3,rely=0.25)

        searchbar=tk.Entry(frame,bg=buttoncol,fg="black",font="Roboto 20") #entry field
        searchbar.place(relx=0.1,rely=0.3,relwidth=0.5,relheight=0.075)

        loutbutt=tk.Button(frame,text="log out",font="Roboto 20",bg=buttoncol,fg="black",command=lambda:logout()) #for logging out
        loutbutt.place(relx=0,rely=0,relwidth=0.15,relheight=0.05) #places button in the window

        searchbutt=tk.Button(frame,text="search",font="Roboto 15",bg=buttoncol,fg="black",command=lambda:searchdb(sop.get(),searchbar.get()))
        searchbutt.place(relx=0.61,rely=0.315,relwidth=0.15,relheight=0.05) #places button in the window

        results=tk.Label(frame,text="Admin mode",justify='left',font="Roboto 15",bg=buttoncol)
        results.place(relx=0.05,rely=0.4,relwidth=0.9,relheight=0.5)

class storepg():   #a class created for the store

    def __init__(self): 

        try:               #deletes previous frames if any previous frames exist
            frame.destroy()		 
        except:			
            pass
    
    
        frame=tk.Frame(root,bg=mainbg)
        frame.place(relx=0,rely=0,relwidth=1,relheight=1)  

        
        label=tk.Label(frame,text="Store",font="Roboto 40",bg=labelcol,fg=ltextcol)
        label.place(relx=0,rely=0,relwidth=1,relheight=0.2)


        item1=tk.Button(frame,text=f"{prodlist[0][0]}",font="Roboto 20",bg=buttoncol,fg="black",command=lambda:item(1))
        item1.place(relx=0.15,rely=0.3,relwidth=0.2,relheight=0.1)

        item2=tk.Button(frame,text=f"{prodlist[1][0]}",font="Roboto 20",bg=buttoncol,fg="black",command=lambda:item(2))
        item2.place(relx=0.65,rely=0.3,relwidth=0.2,relheight=0.1)

        item3=tk.Button(frame,text=f"{prodlist[2][0]}",font="Roboto 20",bg=buttoncol,fg="black",command=lambda:item(3))
        item3.place(relx=0.15,rely=0.5,relwidth=0.2,relheight=0.1)

        item4=tk.Button(frame,text=f"{prodlist[3][0]}",font="Roboto 20",bg=buttoncol,fg="black",command=lambda:item(4))
        item4.place(relx=0.65,rely=0.5,relwidth=0.2,relheight=0.1)

        item5=tk.Button(frame,text=f"{prodlist[4][0]}",font="Roboto 20",bg=buttoncol,fg="black",command=lambda:item(5))
        item5.place(relx=0.15,rely=0.7,relwidth=0.2,relheight=0.1)

        item6=tk.Button(frame,text=f"{prodlist[5][0]}",font="Roboto 20",bg=buttoncol,fg="black",command=lambda:item(6))
        item6.place(relx=0.65,rely=0.7,relwidth=0.2,relheight=0.1)

        loutbutt=tk.Button(frame,text="log out",font="Roboto 20",bg=buttoncol,fg="black",command=lambda:logout()) #for logging out
        loutbutt.place(relx=0.01,rely=0.21,relwidth=0.15,relheight=0.05) #places button in the window





class itempg():
    def __init__(self,itemno):

        try:               #deletes previous frames if any previous frames exist
            frame.destroy()		 
        except:			
            pass
        
                       
        frame=tk.Frame(root,bg=mainbg)
        frame.place(relx=0,rely=0,relwidth=1,relheight=1)   

        
        global pid
        global price
        pid=prodlist[itemno-1][0] #gets the name of item
        price=prodlist[itemno-1][1] #gets the price of the item

        proddesc=desclist[itemno-1]  #gets the name of description

        label=tk.Label(frame,text=f"{pid}",font="Roboto 40",bg=labelcol,fg=ltextcol)                    
        label.place(relx=0,rely=0,relwidth=1,relheight=0.2)


        desclabel=tk.Label(frame,text=f"{proddesc}",justify='left',font="Roboto 15",bg=mainbg)                    
        desclabel.place(relx=0.45,rely=0.2,relwidth=0.5,relheight=0.7)

        global pimage   #prevents image from being garbage collected

        pimage = tk.PhotoImage(file=f"item{itemno}.png")    #creates image object
        imglabel=tk.Label(frame,image=pimage)                                            #creates label containing image
        imglabel.place(relx=0.01,rely=0.31,relwidth=0.45,relheight=0.45)#adds img label to the frame
        

        buybutt=tk.Button(frame,text="buy",font="Roboto 20",bg="#ffff28",fg="black",command=lambda:buy(itemno))
        buybutt.place(relx=0.65,rely=0.85,relwidth=0.2,relheight=0.1)

        backbutt=tk.Button(frame,text="<- back to store",font="Roboto 10",bg=buttoncol,fg="black",command=lambda:storefunc())
        backbutt.place(relx=0.01,rely=0.21,relwidth=0.15,relheight=0.05) 

class buypg():
    def __init__(self,itemno):

        def order(add,ph):

            
            
            try:  #checks if the phone number is a number, raises error if it is not.
                    int(ph)
                    if add.strip()=="" or ph.strip()=="":
                        messagebox.showinfo("Alert","address/phone number is blank!")

            
                    else:
                
                        login.placeOrder(uname,pid,price,add,ph) #enters into db
                

                        messagebox.showinfo("Alert",f"Successful!\nYour order will arrive in 2 days\n{price} Rs must be paid on delivery")
                        storefunc()
            except:
                    messagebox.showinfo("Alert","Phone number contains non numeric values")
            
            
        
        if messagebox.askyesno("Alert",f"Do you want to purchase {pid} \nprice:{price}"):    #spawns messagebox asking if willing to quit
            
            try:               #deletes previous frames if any previous frames exist
                frame.destroy()      
            except:         
                pass
        

            frame=tk.Frame(root,bg=mainbg)
            frame.place(relx=0,rely=0,relwidth=1,relheight=1)   

            label=tk.Label(frame,text=f"Enter your details {uname}",font="Roboto 40",bg=labelcol,fg=ltextcol)                    
            label.place(relx=0,rely=0,relwidth=1,relheight=0.2)

            alabel=tk.Label(frame,text=f"Enter your address",font="Roboto 10",bg=mainbg)                    
            alabel.place(relx=0,rely=0.3,relwidth=1,relheight=0.05)

            adentry=tk.Entry(frame,bg=buttoncol,fg="black",font="Roboto 15") #address entry
            adentry.place(relx=0.25,rely=0.4,relwidth=0.5,relheight=0.075)

            plabel=tk.Label(frame,text=f"Enter your phone number",font="Roboto 10",bg=mainbg)                    
            plabel.place(relx=0,rely=0.5,relwidth=1,relheight=0.05)

            pentry=tk.Entry(frame,bg=buttoncol,fg="black",font="Roboto 15") #phone num entry
            pentry.place(relx=0.25,rely=0.6,relwidth=0.5,relheight=0.075)

            finalbutt=tk.Button(frame,text="buy",bg=buttoncol,fg="black",command=lambda:order(adentry.get(),pentry.get()))
            finalbutt.place(relx=0.45,rely=0.7,relwidth=0.1,relheight=0.1)

            cancelbutt=tk.Button(frame,text="cancel",font="Roboto 10",bg=buttoncol,fg="black",command=lambda:item(itemno))
            cancelbutt.place(relx=0.01,rely=0.21,relwidth=0.15,relheight=0.05) 

        else:
            item(itemno)
                
        
            




root=tk.Tk()   #makes a root window 
root.title("ZapZonics store") #changes the title of the window (PICK NAME PLEASE)
#root.iconbitmap("logo.ico")      #sets window icon (please make ideas for icon)
root.geometry('1920x1080')

canvas=tk.Canvas(root, height=HEIGHT,width=WIDTH) #creates a canvas
canvas.pack()#adds the canvas to the root window



page=homepg() #creates page object


root.protocol("WM_DELETE_WINDOW", on_closing)  #checks if close button is pressed or not
root.mainloop() #runs app
