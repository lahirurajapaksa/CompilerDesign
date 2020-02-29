def readinput():
	#fh = open("example.txt","r")

	#read the file line by line
	# with open("example.txt") as filein:
	# 	lines=[]
	# 	for line in filein:
	# 		#examine the line individually
	# 		#print(line)
	# 		#strip the line of whitespace and trailing newline char
	# 		line.strip()
	# 		line = line.strip('\n')

	# 		# #split the line based on the colon
	# 		# colonSplit = line.split(":")

	# 		# print("colonSplit is ", colonSplit)
			

	# 		# if colonSplit[0]=="variables":
	# 		# 	variables = colonSplit[1]
	# 		# elif colonSplit[0]=="constants":
	# 		# 	constants = colonSplit[1]
	# 		# elif colonSplit[0]=="predicates":
	# 		# 	predicates = colonSplit[1]
	# 		# elif colonSplit[0]=="equality":
	# 		# 	equality = colonSplit[1]
	# 		# elif colonSplit[0]=="connectives":
	# 		# 	connectives = colonSplit[1]
	# 		# elif colonSplit[0]=="quantifiers":
	# 		# 	quantifiers = colonSplit[1]

	# 		# #there can be tabs, line breaks and spaces between symbols in the formula
	# 		# elif colonSplit[0]=="formula":
	# 		# 	formula = colonSplit[1]
	# 		# else:
	# 		# 	print("wrong input")



	# 		lines.append(line)

	#store the file in a list, with each new line as a new element
	lines = list(open("example.txt"))
	validsets = ["variables","constants","predicates","equality","connectives","quantifiers"]
	i=0
	while i<(len(lines)):
		formulaFound = False
		try:

			currentline = lines[i]
			print(currentline)
			#strip the line of whitespace and trailing newline char
			currentline.strip()
			currentline = currentline.strip('\n')
			currentline = currentline.strip('\t')


			 #split the line based on the colon
			colonSplit = currentline.split(":")

			print("colonSplit is ", colonSplit)

			#check whether we are dealing with 'formuala', if so we need to check the next lines as well
			#use a while loop
			if colonSplit[0]=='formula':
				formulaFound=True
				#add the current line's data to the formula
				formula = colonSplit[1]

			if formulaFound==True:
				stop = False
				originali = i 
				while stop==False:
					i=i+1
					nextline = lines[i]
					nextline = nextline.strip('\n')
					nextline = nextline.strip('\t')

					#split the line in to several elements

					nextlinesplit = nextline.split()

					if nextlinesplit[0] in validsets:
						#the next line is not part of the formula
						i=i-1
						stop = True
					else:
						#add it to the formula
						formula = formula + str(nextline)
						i=i+1


		except:
			print("invalid format")



	#separate the contents in to individual elements in a list structure
	# variables = variables.strip()
	# variables = variables.split(' ')
	# print("variables =", variables)

	# constants = constants.strip()
	# constants = constants.split(' ')
	# print("constants =", constants)

	# predicates = predicates.strip()
	# predicates = predicates.split(' ')
	# print("predicates =", predicates)

	# equality = equality.strip()
	# equality = equality.split(' ')
	# print("equality =", equality)

	# connectives = connectives.strip()
	# connectives = connectives.split(' ')
	# print("connectives =", connectives)

	# quantifiers = quantifiers.strip()
	# quantifiers = quantifiers.split(' ')
	# print("quantifiers =", quantifiers)

	# print("formula =", formula)




	#print(lines)

readinput()