while True:
	c_ount=0
	while True:
		def n_umber(n1,n2):
			n1=float(input("\nEnter 1st number:"))
			n2=float(input("Enter 2nd number:"))
			return(n1,n2)
		def p_ositive_sub(n1,n2):
			if n2>n1:
				return(n2,n1)
			else:
				return(n1,n2)
		def r_eset(n1,n2,rslt):
			print("\nresetting calculator.\n")
			n1,n2,rslt=0,0,0
			return(n1,n2,rslt)
		def s_num(n_m):
			n_m=float(input("Enter number:"))
			return(n_m)
		def l_og(opn,n1,n2,rslt):
			myfile = open(r"C:\logs\Python\cal_logs_py.txt","a+")
			if opn=="r"or opn=="\\":
				l_og_dir=str({"Operation":"Square root","num":n1,"Result":rslt})
			elif opn=="c"or opn=="0":
				l_og_dir=str("{'Operation': 'Continuous addition', 'n1': "+str(n1))
			else:
				l_og_dir=str({"Operation":opn,"n1":n1,"n2":n2,"Result":rslt})
			myfile.write("\n"+l_og_dir)
			myfile.close()
		print("Welcome!\n")
		print("Please choose operation from following list to perform calculation.")
		print("1)addition='a or +'\n2)substraction='s or -'\n3)multiplication='m or *'\n4)division='d or /'\n5)square root='r or \\'\n7)continuous addition='c or 0'\n6)quit='q' or '.'")
		opn=str(input("\nEnter your choice:"))
		if c_ount==0:
			c_ount=1
			n1,n2,rslt=0,0,0
		if opn=="q" or opn==".":
			print("\nClearing memory!")
			del n1,n2,rslt,c_ount,l_og,s_num,r_eset,p_ositive_sub
			print("\nThank you! \n")
			break
		elif opn=="a" or opn=="+":
			n1,n2=n_umber(n1,n2)
			rslt=str(n1+n2)
			print("\nresult: "+rslt)
			l_og(opn,n1,n2,rslt)
			n1,n2,rslt=r_eset(n1,n2,rslt)
			continue
		elif opn=="s" or opn=="-":
			n1,n2=n_umber(n1,n2)
			typsb=input("Press p for positve result only substraction, anything for normal substraction:")
			if typsb=="p" or typsb=="+":
				n1,n2=p_ositive_sub(n1,n2)
				rslt=str(n1-n2)
			else:
				rslt=str(n1-n2)
			print("\nresult: "+rslt)
			l_og(opn,n1,n2,rslt)
			n1,n2,rslt=r_eset(n1,n2,rslt)
			continue
		elif opn=="m" or opn=="*":
			n1,n2=n_umber(n1,n2)
			rslt=str(n1*n2)
			print("\nresult: "+rslt)
			l_og(opn,n1,n2,rslt)
			n1,n2,rslt=r_eset(n1,n2,rslt)
			continue
		elif opn=="d" or opn=="/":
			n1,n2=n_umber(n1,n2)
			rslt=str(round((n1/n2),3))
			print("\nresult: "+rslt)
			l_og(opn,n1,n2,rslt)
			n1,n2,rslt=r_eset(n1,n2,rslt)
			continue
		elif opn=="r"or opn=="\\":
			print("")
			from math import sqrt as r
			n1=s_num(n1)
			rslt=str(round(r(n1),2))
			print("\nSquare root of "+str(n1)+" is: "+rslt)
			l_og(opn,n1,n2,rslt)
			n1,n2,rslt=r_eset(n1,n2,rslt)
			continue
		elif opn=="c"or opn=="0":
			print("\nPress valid nonzero values only, for final result press '0'.\n")
			n1=s_num(n1)
			l_og(opn,n1,n2,rslt)
			rslt=rslt+n1
			if n1!=0:
				c2=2
				while True:
					n2=s_num(n2)
					if n2==0:
						break
					else:
						rslt=rslt+n2
						print(rslt)
						myfile_2= open(r"C:\logs\Python\cal_logs_py.txt","a+")
						myfile_2.write(", 'n"+str(c2)+"':"+str(n2))
						myfile_2.close()
						c2+=1
			print("\nresult: "+str(rslt))
			myfile_2= open(r"C:\logs\Python\cal_logs_py.txt","a+")
			myfile_2.write(", 'Result': "+str(rslt)+"}")
			myfile_2.close()
			n1,n2,rslt=r_eset(n1,n2,rslt)
			continue
	print("SujitSGawand.©\n")
	break
    #test
