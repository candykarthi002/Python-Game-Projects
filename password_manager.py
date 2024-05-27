from password_dbase import add_password, delete_password, search_password, display_all_passwords

# def startup():
# 	print()
# 	print("Password Manager")
# 	print()
# 	print("1. Add Password")
# 	print("2. Delete Password")
# 	print("3. Search Password")
# 	print("4. Display all")
# 	print()

def add(details):
	# username = input("Enter the user name: ")
	# account = input("Enter the account: ")
	# password = input("Enter the password: ")
	# platform = input("Enter the platform of the account((e.g) => 'facebook', 'github'): ")
	status = add_password(details["username"], details["account"], details["password"], details["platform"])
	print(status)
	return status
	# if status == "Success":
	# 	print("Process done successfully!!")
	# else:
	# 	print("Process Failed!!")

def delete(name):
	# username = input("Enter the user name: ")
	# account = input("Enter the account: ")
	process = delete_password(name)
	print(process)
	if process == "Success":
		return "Process was done successfully!!"
	else:
		return "Process Failed!!"

def search(info):
	# username = input("Enter the user name: ")
	# account = input("Enter the account: ")
	result = search_password(info["username"], info["account"])
	return result

def display():
	result = display_all_passwords()
	return result


# startup()
# choice = int(input("Enter your choice: "))

# while choice in [1, 2, 3, 4]:
# 	if choice == 1:
# 		add()
# 	elif choice == 2:
# 		delete()
# 	elif choice == 3:
# 		search()
# 	else:
# 		display()
# 	startup()
# 	choice = int(input("Enter your choice: "))

# else:
# 	print("Invalid input!!")
# display()