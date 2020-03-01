import sys

########################################## Read the input ########################################

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

	#replace any tabs
	currentline = currentline.replace('\t','')
	#currentline = currentline.replace('\n','')


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
		print("for quantifiers colonsplit[1] is ",colonSplit[1])
		quantifiers = colonSplit[1]
		print("quantifiers is ",quantifiers)
		i=i+1
	elif colonSplit[0]=="formula":
	#check whether we are dealing with 'formuala', if so we need to check the next lines as well
		formulaFound=True
	#add the current line's data
		formula=colonSplit[1]
	else:
		print("invalid maate")
		sys.exit()
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
#the data that involves elements with a \, will automatically be stored with a \\
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

#check whether constants, predicates and variables all have different names
check = any(item in variables for item in constants)

if check == True:
	print("Variables and constants cant be the same")
	sys.exit()
#double for loop to check iterate through every predicate to compare against the variables
# for i in range(len(predicates)):
# 	for j in range(len(predicates[i])):
# 		if predicates[i][j] in variables:
# 			print(predicates[i][j])
# 			print("predicates and variables cannot be the same")
# 			sys.exit()


################################## Produce the grammar ###################################

#the set of non terminals are the same for every input file
nonterminals = ["variables","constants","predicates","equality","connectives","quantifiers","formula"]	
validname="0123456789_"
#define the production rules

#define the production for 'variables'
print("variable ->", end = " ")
for i in range(len(variables)):
	print("|",variables[i], end=" ")
print('\n')

#define the production for constants
print("constants ->", end = " ")
for i in range(len(constants)):
	print("|",constants[i], end=" ")
print('\n')


varstring = "variable"
#define the production for predicates
print("predicates ->", end = " ")
for i in range(len(predicates)):
	currentpredicate = predicates[i]

	#check to see whether the predicate satisfies the minimum length: 4
	if len(currentpredicate)<4:
		print("predicate does not satisfy minimum length of 4")
		sys.exit()

	#check if the last element is a closing bracket
	if currentpredicate[-1]!="]":
		print("the predicate format is incorrect, last character should be a closing bracket")
		sys.exit()
	#check if there is an opening bracket
	elif "[" not in currentpredicate:
		print("the predicate format is incorrect, should have a opening bracket")
		sys.exit()

	#check whether the open and closed bracket occur only once
	opencount = currentpredicate.count('[')
	closedcount = currentpredicate.count(']')

	if ((opencount!=1) or (closedcount!=1)):
		print("too many brackets")
		sys.exit()

	predicatename=""
	#make sure the first part of the predicate is only alphabetical/numeric/underscore
	for j in range(len(currentpredicate)):
		if (currentpredicate[j] in validname) or (currentpredicate[j].isalpha()==True):
			predicatename=predicatename+currentpredicate[j]
			continue
		elif (currentpredicate[j]=="["):
			openingbrackindex = j
			break
		else:
			print("character is not alphanumeric or an underscore")
			sys.exit()

	arity=""
	#use the index of the opening bracket in order to extract the number inside
	#ensure that everything between the opening bracket and the closing bracket is an integer
	for k in range(openingbrackindex+1,len(currentpredicate)-1):
		if currentpredicate[k].isdigit()==True:
			arity=arity+currentpredicate[k]
			continue
		else:
			print("arity is not numeric")
			sys.exit()

	#check whether the predicate names are the same as any of the variable names
	if predicatename in variables:
		print("predicate name is the same as a variable name")
		sys.exit()
	elif predicatename in constants:
		print("predicate name is the same as a constant name")

	#print the production for predicates
	
print('\n')





