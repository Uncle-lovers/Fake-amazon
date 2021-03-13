"""
Project_Name: ElectroZapzonics
Developers: 
-Joshua
-Pradeesh
-Pranav
-Rishi

Date_Created: 05-Mar-21

"""
import mysql.connector as mydb         #too lazy to install mysql on my linux, just uncomment it no other change

db = mydb.connect(host="localhost",
        user="root",
 	passwd="vvs",
 	database="zapzonics",)


#import sqlite3

#db = sqlite3.connect('electrozapzonics.db')  #sqlite3, get rid when you use mysql

mycursor = db.cursor()


try:            #checks if CREDENTIALS table exists
	
	mycursor.execute('SELECT * FROM CREDENTIALS')
	garbage=mycursor.fetchall()    #causes error if not fetched, smh mysql bad
except:
	mycursor.execute('CREATE TABLE CREDENTIALS (USERNAME varchar(100),PASSWORD varchar(100))')


try:            #checks if PRODUCTS table exists
	
	mycursor.execute('SELECT * FROM PRODUCTS')
	garbage=mycursor.fetchall()    #causes error if not fetched, smh mysql bad
except:
	mycursor.execute('CREATE TABLE PRODUCTS (USERNAME varchar(100),PRODUCT varchar(100),PRICE varchar(10),ADDRESS varchar(100),PHONO varchar(20))')

#logins

def credentialsE(username, password):#for signing up
	mycursor.execute(f'SELECT username FROM CREDENTIALS WHERE username="{username}"')
	res = mycursor.fetchall()   
	try: #Checking username

		if res[0][0] == username:  #rasies error if no records exist
			 return False

	except:	  #Sign-up
		mycursor.execute(f'INSERT INTO CREDENTIALS VALUES("{username}","{password}")')
		db.commit()      
	
		return True
	
def credentialsP(user, passw):  #login
	mycursor.execute(f'SELECT password FROM CREDENTIALS WHERE username="{user}"')
	result = mycursor.fetchall()   
	
	try:                               #error is raised if table is empty
		return result[0][0]==passw
	except:
		return False


def placeOrder(username,product,price,address,phono):
	mycursor.execute(f'INSERT INTO PRODUCTS VALUES("{username}","{product}","{price}","{address}","{phono}")')
	db.commit()        


def search(option,search):

	try:                   #if admin messes up option 6



		if option==1:
			mycursor.execute(f'SELECT * FROM PRODUCTS WHERE USERNAME="{search}"')
			

		elif option==2:
			mycursor.execute(f'SELECT * FROM PRODUCTS WHERE PRODUCT="{search}"')
			

		elif option==3:
			mycursor.execute(f'SELECT * FROM PRODUCTS WHERE PRICE>"{search}"')
			

		elif option==4:
			mycursor.execute(f'SELECT * FROM PRODUCTS WHERE address="{search}"')
			

		elif option==5:
			mycursor.execute(f'SELECT * FROM PRODUCTS WHERE PHONO="{search}"')
			

		elif option==6:
			mycursor.execute(search)
			

		
		return mycursor.fetchall()   

	except Exception as E:
		
		return [("error",)]

