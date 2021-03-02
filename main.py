import mysql.connector as mydb

db = mydb.connect(host="localhost",
	user="root",
	passwd="root",
	database="fakeamazon")


mycursor = db.cursor()
#c_id, c_name, c_number,product_id,product_name,product_price
mycursor.execute()
