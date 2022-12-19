def register(cursor, sql):
	try:
		username = input('Enter full name: ')
		password = input('Enter password: ')

		query = 'SELECT * FROM `users` WHERE username = %s'
		data = (username,)

		cursor.execute(query, data)
		response = cursor.fetchone()

		if response:
			print('\nUser already exists.')
			input('\n--> Press ENTER to try again: ')
			register(cursor, sql)
		else:
			query = "INSERT into users(username, password) VALUES (%s, %s)"
			data = (username, password)

			cursor.execute(query, data)
			sql.commit()

			print('Account created successfully.')
			input('\n--> Press ENTER to go back: ')
			pass
	
	except KeyboardInterrupt:
		print("\n\n\tExiting...")
		exit()