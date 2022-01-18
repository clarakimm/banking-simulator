print ("Welcome to ND Banking.")
password= input("Please enter the password to enter the account: ")
if (password=="FightingIrish"):
	c=100.00 #CAD
	a=75 #USD
	action3="NO"
	while (action3=="NO" or action3=="no"):
		print ("Canadian Account: $%.2f" %c,"CAD")
		print ("American Account: $%.2f" %a,"USD")
		print ("1. Canadian Account")
		print ("2. American Account")
		print ("3. Transfer Betweeen Accounts")
		print ("4. Exit")
		action= int(input("What service would you like to access?: "))
		if (action==1):
			print ("Canadian Account")
			print ("1. Deposit")
			print ("2. Withdraw")
			action2=int(input("What action would you like to take? "))
			if (action2==1):
				print ("Amount in account: $%.2f" %c,"CAD" )
				deposit = float(input("How much would you like to deposit?: "))
				c=c+deposit
				
				print ("Total amount in account: $%.2f" %c,"CAD")
				action3=(input("Would you like to make another action in your Canadian Account?"))
				while (action3=="YES" or action3=="yes"):
					print ("Canadian Account")
					print ("1. Deposit")
					print ("2. Withdraw")
					action2=int(input("What action would you like to take? "))
					if (action2==1):
						print ("Amount in account: $%.2f" %c,"CAD")
						deposit = float(input("How much would you like to deposit?: "))
						deposit = round(deposit,2)
						c=c+deposit 
						print ("Total amount in account: $%.2f" %c,"CAD")
						action3=input("Would you like to make another action in your Canadian Account?")
					elif (action2==2):
						print ("Amount in account: $%.2f" %c,"CAD")
						withdraw = float (input("How much would you like to withdraw?: "))
						if(withdraw<=c): 
							c=c-withdraw
							print ("Total amount in account: $%.2f" %c,"CAD")
							action3= input("Would you like to make another action in your Canadian Account?")
						elif(withdraw>c):
							print("You do not have enough money in your account to withdraw from.")
							action3= input("Would you like to make another action in your Canadian Account?")
						
			elif (action2==2):
				print ("Amount in account: $%.2f" %c,"CAD")
				withdraw = float(input("How much would you like to withdraw?: "))
				if(withdraw<=c): 
					c=c-withdraw
					print ("Total amount in account: $%.2f" %c,"CAD")
					action3= input("Would you like to make another action in your Canadian Account?")
				elif(withdraw>c):
					print("You do not have enough money in your account to withdraw from.")
					action3= input("Would you like to make another action in your Canadian Account?")
				while (action3=="YES" or action3=="yes"):
					print ("Canadian Account")
					print ("1. Deposit")
					print ("2. Withdraw")
					action2=int(input("What action would you like to take? "))
					if (action2==1):
						print ("Amount in account: $%.2f" %c,"CAD")
						deposit = float(input("How much would you like to deposit?: "))
						deposit = round(deposit,2)
						c=c+deposit 
						print ("Total amount in account: $%.2f" %c,"CAD")
						action3=(input("Would you like to make another action in your Canadian Account?"))
					elif (action2==2):
						print ("Amount in account: $%.2f" %c )
						withdraw = float(input("How much would you like to withdraw?: "))
						if(withdraw<=c): 
							c=c-withdraw
							print ("Total amount in account: $%.2f" %c,"CAD")
							action3= input("Would you like to make another action in your Canadian Account?")
						elif(withdraw>c):
							print("You do not have enough money in your account to withdraw from.")
							action3= input("Would you like to make another action in your Canadian Account?")

		elif (action==2):
			print ("American Account")
			print ("1. Deposit")
			print ("2. Withdraw")
			action2=int(input("What action would you like to take? "))
			if (action2==1):
				print ("Amount in account: $%.2f" %a,"USD" )
				deposit = float(input("How much would you like to deposit?: "))
				deposit = round(deposit,2)
				a=a+deposit 
				print ("Total amount in account:$%.2f" %a,"USD")
				action3=(input("Would you like to make another action in your American Account?"))
				while (action3=="YES" or action3=="yes"):
					print ("American Account")
					print ("1. Deposit")
					print ("2. Withdraw")
					action2=int(input("What action would you like to take? "))
					if (action2==1):
						print ("Amount in account:$%.2f" %a,"USD")
						deposit = float(input("How much would you like to deposit?: "))
						deposit = round(deposit,2)
						a=a+deposit 
						print ("Total amount in account:$%.2f" %a,"USD")
						action3=input("Would you like to make another action in your American Account?")
					elif (action2==2):
						print ("Amount in account:$%.2f" %a,"USD")
						withdraw = float (input("How much would you like to withdraw?: "))
						if(withdraw<=a): 
							a=a-withdraw
							print ("Total amount in account: $%.2f" %a,"USD")
							action3= input("Would you like to make another action in your American Account?")
						elif(withdraw>a):
							print("You do not have enough money in your account to withdraw from.")
							action3= input("Would you like to make another action in your American Account?")
						
			elif (action2==2):
				print ("Amount in account: $%.2f" %a,"USD")
				withdraw = float(input("How much would you like to withdraw?: "))
				if(withdraw<=a): 
					a=a-withdraw
					print ("Total amount in account: $%.2f" %a,"USD")
					action3= input("Would you like to make another action in your American Account?")
				elif(withdraw>a):
					print("You do not have enough money in your account to withdraw from.")
					action3= input("Would you like to make another action in your American Account?")
				while (action3=="YES" or action3=="yes"):
					print ("American Account")
					print ("1. Deposit")
					print ("2. Withdraw")
					action2=int(input("What action would you like to take? "))
					if (action2==1):
						print ("Amount in account: $%.2f" %a,"USD")
						deposit = float(input("How much would you like to deposit?: "))
						deposit = round(deposit,2)
						a=a+deposit 
						print ("Total amount in account: $%.2f" %a,"USD")
						action3=(input("Would you like to make another action in your American Account?"))
					elif(action2==2):
						print ("Amount in account: $%.2f" %a,"USD")
						withdraw = float(input("How much would you like to withdraw?: "))
						if(withdraw<=a): 
							a=a-withdraw
							print ("Total amount in account: $%.2f" %a,"USD")
							action3= input("Would you like to make another action in your American Account?")
						elif(withdraw>a):
							print("You do not have enough money in your account to withdraw from.")
							action3= input("Would you like to make another action in your American Account?")

		elif (action==3):
			print ("TRANSFERING OPTIONS:")
			print ("1. Candian Account to American Account")
			print ("2. American Account to Canadian Account")
			t1=int(input("How would you like to perform your transaction? :"))
			if (t1==1):
				print ("Amount in Canadian Account: $%.2f" %c,"CAD")
				print ("Amount in American Account: $%.2f" %a,"USD")
				howmuch=float(input("How much would you like to transfer?: "))
				if (howmuch<=c):
					c=c-howmuch
					howmuch=howmuch*0.75
					howmuch=round(howmuch,2)
					a=a+howmuch 
					print ("Amount in Canadian Account: $%.2f" %c,"CAD")
					print ("Amount in American Account: $%.2f" %a,"USD")
					back= input("Press any key to return to the Main Menu.")
					if (back=="M"):
						action3="no"
					else:
						action3="no"
				elif(howmuch>c):
					print("You do not have enough money in this account to transfer from.")
					action3="no"
			
			elif (t1==2):
				print ("Amount in Canadian Account: $%.2f" %c,"CAD")
				print ("Amount in American Account: $%.2f" %a,"USD")
				howmuch=float(input("How much would you like to transfer?: "))
				if (howmuch<=a):
					howmuch=round(howmuch,2)
					a=a-howmuch
					howmuch=howmuch*1.34
					howmuch=round(howmuch,2)
					c=c+howmuch
					print ("Amount in Canadian Account: $%.2f" %c,"CAD")
					print ("Amount in American Account: $%.2f" %a,"USD")
					back= input("Press any key to return to the Main Menu.")
					if (back=="M"):
						action3="no"
					else:
						action3="no"
				elif(howmuch>a):
					print("You do not have enough money in this account to transfer from.")
					action3="no"

		elif(action==4): 
			print ("Thank you for using ND Banking. Press any key to Exit.")
			break
			
else:
	print ("Try Again.")
	password=input("Password: ")
	if (password=="FightingIrish"):
		c=100.00 #CAD
		a=75 #USD
		action3="NO"
		while (action3=="NO" or action3=="no"):
			print ("Canadian Account: $%.2f" %c,"CAD")
			print ("American Account: $%.2f" %a,"USD")
			print ("1. Canadian Account")
			print ("2. American Account")
			print ("3. Transfer Betweeen Accounts")
			print ("4. Exit")
			action= int(input("What service would you like to access?: "))
			if (action==1):
				print ("Canadian Account")
				print ("1. Deposit")
				print ("2. Withdraw")
				action2=int(input("What action would you like to take? "))
				if (action2==1):
					print ("Amount in account: $%.2f" %c,"CAD" )
					deposit = float(input("How much would you like to deposit?: "))
					c=c+deposit
					
					 
					print ("Total amount in account: $%.2f" %c,"CAD")
					action3=(input("Would you like to make another action in your Canadian Account?"))
					while (action3=="YES" or action3=="yes"):
						print ("Canadian Account")
						print ("1. Deposit")
						print ("2. Withdraw")
						action2=int(input("What action would you like to take? "))
						if (action2==1):
							print ("Amount in account: $%.2f" %c,"CAD")
							deposit = float(input("How much would you like to deposit?: "))
							deposit = round(deposit,2)
							c=c+deposit 
							print ("Total amount in account: $%.2f" %c,"CAD")
							action3=input("Would you like to make another action in your Canadian Account?")
						elif (action2==2):
							print ("Amount in account: $%.2f" %c,"CAD")
							withdraw = float (input("How much would you like to withdraw?: "))
							if(withdraw<=c): 
								c=c-withdraw
								print ("Total amount in account: $%.2f" %c,"CAD")
								action3= input("Would you like to make another action in your Canadian Account?")
							elif(withdraw>c):
								print("You do not have enough money in your account to withdraw from.")
								action3= input("Would you like to make another action in your Canadian Account?")
							
				elif (action2==2):
					print ("Amount in account: $%.2f" %c,"CAD")
					withdraw = float(input("How much would you like to withdraw?: "))
					if(withdraw<=c): 
						c=c-withdraw
						print ("Total amount in account: $%.2f" %c,"CAD")
						action3= input("Would you like to make another action in your Canadian Account?")
					elif(withdraw>c):
						print("You do not have enough money in your account to withdraw from.")
						action3= input("Would you like to make another action in your Canadian Account?")
					while (action3=="YES" or action3=="yes"):
						print ("Canadian Account")
						print ("1. Deposit")
						print ("2. Withdraw")
						action2=int(input("What action would you like to take? "))
						if (action2==1):
							print ("Amount in account: $%.2f" %c,"CAD")
							deposit = float(input("How much would you like to deposit?: "))
							deposit = round(deposit,2)
							c=c+deposit 
							print ("Total amount in account: $%.2f" %c,"CAD")
							action3=(input("Would you like to make another action in your Canadian Account?"))
						elif (action2==2):
							print ("Amount in account: $%.2f" %c )
							withdraw = float(input("How much would you like to withdraw?: "))
							if(withdraw<=c): 
								c=c-withdraw
								print ("Total amount in account: $%.2f" %c,"CAD")
								action3= input("Would you like to make another action in your Canadian Account?")
							elif(withdraw>c):
								print("You do not have enough money in your account to withdraw from.")
								action3= input("Would you like to make another action in your Canadian Account?")

			elif (action==2):
				print ("American Account")
				print ("1. Deposit")
				print ("2. Withdraw")
				action2=int(input("What action would you like to take? "))
				if (action2==1):
					print ("Amount in account: $%.2f" %a,"USD" )
					deposit = float(input("How much would you like to deposit?: "))
					deposit = round(deposit,2)
					a=a+deposit 
					print ("Total amount in account:$%.2f" %a,"USD")
					action3=(input("Would you like to make another action in your American Account?"))
					while (action3=="YES" or action3=="yes"):
						print ("American Account")
						print ("1. Deposit")
						print ("2. Withdraw")
						action2=int(input("What action would you like to take? "))
						if (action2==1):
							print ("Amount in account:$%.2f" %a,"USD")
							deposit = float(input("How much would you like to deposit?: "))
							deposit = round(deposit,2)
							a=a+deposit 
							print ("Total amount in account:$%.2f" %a,"USD")
							action3=input("Would you like to make another action in your American Account?")
						elif (action2==2):
							print ("Amount in account:$%.2f" %a,"USD")
							withdraw = float (input("How much would you like to withdraw?: "))
							if(withdraw<=a): 
								a=a-withdraw
								print ("Total amount in account: $%.2f" %a,"USD")
								action3= input("Would you like to make another action in your American Account?")
							elif(withdraw>a):
								print("You do not have enough money in your account to withdraw from.")
								action3= input("Would you like to make another action in your American Account?")
							
				elif (action2==2):
					print ("Amount in account: $%.2f" %a,"USD")
					withdraw = float(input("How much would you like to withdraw?: "))
					if(withdraw<=a): 
						a=a-withdraw
						print ("Total amount in account: $%.2f" %a,"USD")
						action3= input("Would you like to make another action in your American Account?")
					elif(withdraw>a):
						print("You do not have enough money in your account to withdraw from.")
						action3= input("Would you like to make another action in your American Account?")
					while (action3=="YES" or action3=="yes"):
						print ("American Account")
						print ("1. Deposit")
						print ("2. Withdraw")
						action2=int(input("What action would you like to take? "))
						if (action2==1):
							print ("Amount in account: $%.2f" %a,"USD")
							deposit = float(input("How much would you like to deposit?: "))
							deposit = round(deposit,2)
							a=a+deposit 
							print ("Total amount in account: $%.2f" %a,"USD")
							action3=(input("Would you like to make another action in your American Account?"))
						elif(action2==2):
							print ("Amount in account: $%.2f" %a,"USD")
							withdraw = float(input("How much would you like to withdraw?: "))
							if(withdraw<=a): 
								a=a-withdraw
								print ("Total amount in account: $%.2f" %a,"USD")
								action3= input("Would you like to make another action in your American Account?")
							elif(withdraw>a):
								print("You do not have enough money in your account to withdraw from.")
								action3= input("Would you like to make another action in your American Account?")

			elif (action==3):
				print ("TRANSFERING OPTIONS:")
				print ("1. Candian Account to American Account")
				print ("2. American Account to Canadian Account")
				t1=int(input("How would you like to perform your transaction? :"))
				if (t1==1):
					print ("Amount in Canadian Account: $%.2f" %c,"CAD")
					print ("Amount in American Account: $%.2f" %a,"USD")
					howmuch=float(input("How much would you like to transfer?: "))
					if (howmuch<=c):
						c=c-howmuch
						howmuch=howmuch*0.75
						howmuch=round(howmuch,2)
						a=a+howmuch 
						print ("Amount in Canadian Account: $%.2f" %c,"CAD")
						print ("Amount in American Account: $%.2f" %a,"USD")
						back= input("Press any key to return to the Main Menu.")
						if (back=="M"):
							action3="no"
						else:
							action3="no"
					elif(howmuch>c):
						print("You do not have enough money in this account to transfer from.")
						action3="no"
				
				elif (t1==2):
					print ("Amount in Canadian Account: $%.2f" %c,"CAD")
					print ("Amount in American Account: $%.2f" %a,"USD")
					howmuch=float(input("How much would you like to transfer?: "))
					if (howmuch<=a):
						howmuch=round(howmuch,2)
						a=a-howmuch
						howmuch=howmuch*1.34
						howmuch=round(howmuch,2)
						c=c+howmuch
						print ("Amount in Canadian Account: $%.2f" %c,"CAD")
						print ("Amount in American Account: $%.2f" %a,"USD")
						back= input("Press any key to return to the Main Menu.")
						if (back=="M"):
							action3="no"
						else:
							action3="no"
					elif(howmuch>a):
						print("You do not have enough money in this account to transfer from.")
						action3="no"

			elif(action==4): 
				print ("Thank you for using ND Banking. Press any key to Exit.")
				break
