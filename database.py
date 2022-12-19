def database(cursor):
	## Create DB
	cursor.execute("CREATE DATABASE IF NOT EXISTS hotel")
	cursor.execute("USE hotel")

	## Create User Table
	userTable = '''
		CREATE TABLE IF NOT EXISTS users(
			username varchar(20) primary key,
			password varchar(40)
		)'''
	cursor.execute(userTable)