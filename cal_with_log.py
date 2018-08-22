while True:
	print("Welcome")
	print("Please choose operation from following list to perform calculation.")
	print("addition='a', substraction='s', multiplication='m', division='d', quit='q'")
	opn=input("Enter your choice:")
	if opn=="q":
		print("\nresetting calculator.\n")
		n1=0
		n2=0
		rslt=0
		print("Thank you! \n \nSujitSGawand.\n")
		break
	elif opn=="a":
		n1=float(input("Enter 1st number:"))
		n2=float(input("Enter 2nd number:"))
		rslt=str(n1+n2)
		print("\nresult: "+rslt)
		print("\nresetting calculator.\n")
		n1=0
		n2=0
		rslt=0
	elif opn=="s":
		n1=float(input("Enter 1st number:"))
		n2=float(input("Enter 2nd number:"))
		typsb=input("Enter p for positve result only substraction, n for normal substraction:")
		if typsb=="n":
			rslt=str(n1-n2)
		elif n1>n2:
			rslt=str(n1-n2)
		else:
			rslt=str(n2-n1)
		print("\nresult: "+rslt)
		print("\nresetting calculator.\n")
		n1=0
		n2=0
		rslt=0
	elif opn=="m":
		n1=float(input("Enter 1st number:"))
		n2=float(input("Enter 2nd number:"))
		rslt=str(n1*n2)
		print("\nresult: "+rslt)
		print("\nresetting calculator.\n")
		n1=0
		n2=0
		rslt=0
	elif opn=="d":
		n1=float(input("Enter 1st number:"))
		n2=float(input("Enter 2nd number:"))
		rslt=str(n1/n2)
		print("\nresult: "+rslt)
		print("\nresetting calculator.\n")
		n1=0
		n2=0
		rslt=0







