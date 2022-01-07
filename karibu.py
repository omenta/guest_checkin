import time
guests = []
archived_guests = []

def check_in():  # TODO: Make sure no fields are left blank
	guest_id = 0
	print ('Name: ')
	name = input()
	print ('Company: ')
	company = input()
	print ('Host: ')
	host = input()
	print ('Department: ')
	department = input()
	print ('Purpose: ')
	purpose = input()
	
	guests.append(name)
	f = open("wageni.txt", "a")
	f.write("\n"+name+" from "+company+" to "+purpose+" with "+host+" in "+department+".")
	f.close()
	
	print ("Welcome!")
	print ("You've been successfully signed in.")
	
	guest_id +=1 # Increases the guest ID number by 1
	
	
def check_out():
	guest = input("Name: ")
	if guest in guests:
		archived_guests.append(guest) # move guest name to archives 
		guests.remove(guest) # remove guest from list of guests 
	else:
		print ("Name not found!")
			
	print ("Thank you!")
	print ("Check out successful!")
	

def intro():
	option = int(input("1. Check In \n2. Check Out \n : "))
	if option == 1:
		check_in()
	elif option == 2:
		check_out()
	else:
		#while (option != 1 && option != 2):
			print ("Invalid input! Try again. ")
			print ("Enter 1 for Check In and 2 for Check Out")
			

def main ():
	print(time.asctime())
	print(time.time())
	print("Check In Terminal")
	intro()
	
	
if __name__ == "__main__":
	main()
	#app.run(host='localhost', port=9874)
	#app.run()
