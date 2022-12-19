def login(cursor):
	try:
		username = input('Enter full name: ')
		password = input('Enter password: ')

		query = ('SELECT * FROM `users` WHERE username = %s AND password = %s')
		data = (username, password)

		cursor.execute(query, data)
		response = cursor.fetchone()

		if len(response)>0:
			print('Logged in successfully.')
			input('\n--> Press ENTER to continue: ')
			return username
		else:
			login(cursor)
	
	except KeyboardInterrupt:
		print("\n\n\tExiting...")
		exit()