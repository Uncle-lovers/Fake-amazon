import mysql.connector as mydb

db = mydb.connect(host="localhost",
	user="root",
	passwd="root",
	database="fakeamazon")


mycursor = db.cursor()

'notes'

#check if tables exist before (login table and sales table)
#if table does not exist create table
#login table requires name,password
#sales table requires name,productname,price,phonenumber,address

'''both tables should be able to have values inserted and values retrieved 

i dont remember python + mysql so correct whatever is wrong, but you get it right?

def usersignup(uname,passcode):
	mycursor.execute(f"INSERT INTO TABLE logins VALUES({uname},{passcode})")

def loginpull():
	mycursor.execute("select * from logins ..........") #rest i forgot python+msql but it should be available as a list/tuple

def order(uname,pname,price,pnum,address):
	mycursor.execute(f"INSERT INTO TABLE logins VALUES({uname},{passcode})")

def searchdat(option):
	displaying things, ill type later
'''
