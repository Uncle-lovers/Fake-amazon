"""
Project_Name: ElectroZapzonics
Developers: 
-Joshua
-Pradeesh
-Pranav
-Rishi

Date_Created: 05-Mar-21

"""
import mysql.connector as mydb

db = mydb.connect(host="localhost",
	user="root",
	passwd="root",
	database="electrozapzonics",
	autocommit=True)

mycursor = db.cursor()

#logins

def credentialsE(username, password):#Login
	mycursor.execute(f'SELECT username FROM CREDENTIALS WHERE username="{username}"')
	res = mycursor.fetchall()
	try: #Checking username

		if res[0][0] == username:
			print("Username already exists!")
	except:	  #Sign-up
		mycursor.execute(f'INSERT INTO CREDENTIALS VALUES("{username}","{password}")')
		db.commit()
		
	
def credentialsP(user, passw):
	mycursor.execute(f'SELECT password FROM CREDENTIALS WHERE username="{user}"')
	result = mycursor.fetchall()
	


def placeOrder(username,product,price,address,phono):
	mycursor.execute(f'INSERT INTO PRODUCTS VALUES("{username}","{product}","{price}","{address}","{phono}")')
	db.commit()


def search(option,search):
	if option=="1":
		mycursor.execute(f'SELECT * FROM PRODUCTS WHERE USERNAME="{search}"')

	elif option=="2":
		mycursor.execute(f'SELECT * FROM PRODUCTS WHERE PRODUCT="{search}"')

	elif option=="3":
		mycursor.execute(f'SELECT * FROM PRODUCTS WHERE PRICE="{search}"')

	elif option=="4":
		mycursor.execute(f'SELECT * FROM PRODUCTS WHERE address="{search}"')

	elif option=="5":
		mycursor.execute(f'SELECT * FROM PRODUCTS WHERE PHONO="{search}"')

	return mycursor.fetchall()
