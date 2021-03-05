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
	


#sales

