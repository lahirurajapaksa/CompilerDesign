def readinput():

	#store the file in a list, with each new line as a new element
	lines = list(open("example.txt"))
	validsets = ["variables:","constants:","predicates:","equality:","connectives:","quantifiers:"]
	i=0
	while i<(len(lines)):
	
		formulaFound=False

		currentline = lines[i]
		print(currentline)
		#strip the line of whitespace and trailing newline char
		currentline.strip()
		currentline = currentline.strip('\n')
		currentline = currentline.strip('\t')

		print("currentline is ",currentline)
		 #split the line based on the colon
		colonSplit = currentline.split(":")


		print("colonSplit is ", colonSplit)

		if colonSplit[0]=="variables":
			variables = colonSplit[1]
			i=i+1
		elif colonSplit[0]=="constants":
		 	constants = colonSplit[1]
		 	i=i+1
		elif colonSplit[0]=="predicates":
		 	predicates = colonSplit[1]
		 	i=i+1
		elif colonSplit[0]=="equality":
		 	equality = colonSplit[1]
		 	i=i+1
		elif colonSplit[0]=="connectives":
		 	connectives = colonSplit[1]
		 	i=i+1
		elif colonSplit[0]=="quantifiers":
		 	quantifiers = colonSplit[1]
		 	i=i+1
		elif colonSplit[0]=="formula":
		#check whether we are dealing with 'formuala', if so we need to check the next lines as well
			formulaFound=True
		#add the current line's data
			formula=colonSplit[1]
		else:
			print("invalid maate")
			print("this is it ", colonSplit)

		#use a while loop

		if formulaFound==True:
			stop = False
			i=i+1
			print("i+1 is ",i,"before entering while loop")
			while stop==False and i<len(lines):
				nextline = lines[i]
				nextline = nextline.strip('\n')
				nextline = nextline.strip('\t')

				#split the line in to several elements

				nextlinesplit = nextline.split()
				print("first element of next line is ",nextlinesplit[0])
				if nextlinesplit[0] in validsets:
					#the next line is not part of the formula
					#i=i-1
					print("next line is not part of formula so i is ",i)
					stop = True
				elif nextlinesplit[0] not in validsets:
					#add it to the formula
					formula = formula + str(nextline)
					i=i+1
					print("adding to formula so i is",i)




	#separate the contents in to individual elements in a list structure
	variables = variables.strip()
	variables = variables.split(' ')
	print("variables =", variables)

	constants = constants.strip()
	constants = constants.split(' ')
	print("constants =", constants)

	predicates = predicates.strip()
	predicates = predicates.split(' ')
	print("predicates =", predicates)

	equality = equality.strip()
	equality = equality.split(' ')
	print("equality =", equality)

	connectives = connectives.strip()
	connectives = connectives.split(' ')
	print("connectives =", connectives)

	quantifiers = quantifiers.strip()
	quantifiers = quantifiers.split(' ')
	print("quantifiers =", quantifiers)

	formula = formula.strip()
	formula = formula.split(' ')
	print("formula =", formula)




	#print(lines)

readinput()