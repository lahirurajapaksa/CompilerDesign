import sys

########################################## Read the input ########################################

#store the file in a list, with each new line as a new element
lines = list(open("example.txt"))
validsets = ["variables:","constants:","predicates:","equality:","connectives:","quantifiers:"]
productiondict={}
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
print('\n')

#check whether constants, predicates and variables all have different names
check = any(item in variables for item in constants)

if check == True:
	print("Variables and constants cant be the same")
	sys.exit()


################################## Produce the grammar + more error checking ###################################

#the set of non terminals are the same for every input file
nonterminals = ["variables","constants","predicates","equality","connectives","quantifiers","formula"]	
validname="0123456789_"

#define the production rules

#define the start symbol
print("start -> formula")
print('\n')



#define the production for 'variables'
print("variable ->", end = " ")
for i in range(len(variables)):
	#check whether the variable name consists of only alphanumeric characters and underscore
	currentvariable = variables[i]
	for j in range(len(currentvariable)):
		if (currentvariable[j].isalpha()==True) or (currentvariable[j] in validname):
			continue
		else:
			print("\n")
			print("incorrect variable name, must only contain alphanumeric characters and underscore")
			sys.exit()
	if i==0:
		print(currentvariable, end=" ")
		continue

	print("|",currentvariable, end=" ")

print('\n')

#store it in the dict
productiondict['variables']=variables


#define the production for constants
print("constants ->", end = " ")
for i in range(len(constants)):
	currentconstant = constants[i]

	for j in range(len(currentconstant)):
		if (currentconstant[j].isalpha()==True) or (currentconstant[j] in validname):
			continue
		else:
			print("\n")
			print("incorrect constant name, must only contain alphanumeric characters and underscore")
			sys.exit()

	if i==0:
		print(constants[i], end=" ")
		continue


	print("|",constants[i], end=" ")
print('\n')

#store it in the dict
productiondict['constants']=constants




#define the production for equality
print("equality ->", end = " ")
if len(equality)!=1:
	print("Equality set is not equal to size 1")
	sys.exit()
for i in range(len(equality)):
	currentequality = equality[i]
	#check whether the length of the equality symbol is equal to one
	if len(currentequality)!=1:
		print("equality set is not equal to size one")
		sys.exit()

	for j in range(len(currentequality)):
		if (currentequality[j]=="="):
			continue
		else:
			print("\n")
			print("incorrect equality used, must be =")
			sys.exit()

	if i==0:
		print(equality[i], end=" ")
		continue


	print("|",equality[i], end=" ")
print('\n')

#store it in the dict
productiondict['equality']=equality


#define the production for connectives
print("connectives ->", end = " ")
#check that the connectives are a set of 5
if len(connectives)!=5:
	print("connectives set is not of size 5")
	sys.exit()

#remove the last negation element from the connectives set and store it in a variable
#this will be used in a production rule later for //neg formula, instead of formula //neg formula which is wrong

#store the last element
negationelement = connectives[-1]
#delete the last element now
connectives = connectives[:-1]

for i in range(len(connectives)):

	currentconnective = connectives[i]


	# for j in range(len(currentconnective)):
	# 	if (currentconnective[j]=="="):
	# 		continue
	# 	else:
	# 		print("\n")
	# 		print("incorrect equality used, must be =")
	# 		sys.exit()

	if i==0:
		print(currentconnective, end=" ")
		continue


	print("|",currentconnective, end=" ")
print('\n')

#store it in the dict
productiondict['connectives']=connectives


#define the production for quantifiers
print("quantifiers ->", end = " ")
if len(quantifiers)!=2:
	print("quantifiers set is not of size 2")
	sys.exit()
for i in range(len(quantifiers)):
	currentquantifier = quantifiers[i]

	# for j in range(len(currentquantifier)):
		# if (currentquantifier[j]=="="):
		# 	continue
		# else:
		# 	print("\n")
		# 	print("incorrect equality used, must be =")
		# 	sys.exit()

	if i==0:
		print(currentquantifier, end=" ")
		continue


	print("|",currentquantifier, end=" ")
print('\n')

#store it in the dict
productiondict['quantifiers']=quantifiers




formulaproductions =[]
#make the four rules + others in the spec for formulas

#define the term production rule
print("term -> variable | constant")
termlist=['variable','constant']
productiondict['terms'] = termlist
print('\n')

#use the term rule to define the primitive formula rule

#define rule 2 (C = D), (C = x), (x = C) and (x = y) are valid

print("formula -> term equality term |",end=" ")
#get the equality set
equals = productiondict['equality']
rule2 = ['(','term',equality,'term',')']
formulaproductions.append(rule2)


#define rule 3 formula ^ formula , and so on
#use the connectives set to define this
# c = productiondict['connectives']
# rule3list = []
# print('formula -> ', end=" ")

# for i in range(len(c)):
# 	currentstring = ""
# 	currentcon = c[i]
# 	if i==0:
# 		print("formula",currentcon,"formula", end=" ")
# 		currentstring = "formula " + currentcon + " formula"
# 		rule3list.append(currentstring)
# 		continue

# 	currentstring = "formula " + currentcon + " formula"
# 	rule3list.append(currentstring)

# 	print("|","formula",currentcon,"formula", end=" ")

# productiondict['formula'] = rule3list
#productiondict['formula'] = productiondict['formula'].extend(rule3list)



#define formula connective formula
print('formula connective formula',end=" ")

connectiveset = productiondict['connectives']
rule3 = ['(','formula',connectiveset,'formula',')']
formulaproductions.append(rule3)





#define rule 4 - there exists x formula, for all x formula as long as x is a variable


# q = productiondict['quantifiers']
# rule4list = []
# #use the quantifiers set to check for stuff in front of 
# for i in range(len(q)):
# 	currentstring=""
# 	currentq = q[i]

# 	if i == 0:
# 		print(currentq," variable"," formula",end=" ")
# 		currentstring = currentq + " variable " + "formula"
# 		rule4list.append(currentstring)
# 		continue

# 	currentstring = currentq + " variable " + "formula"
# 	rule4list.append(currentstring)
# 	print("|",currentq,"variable ","formula",end=" ")

#productiondict['formula4'] = rule4list

# productiondict['formula'] = productiondict['formula']+rule4list



#define quantifier variable formula
print('| quantifier variable formula|',end=" ")
quantifierset = productiondict['quantifiers']
varset = productiondict['variables']

rule4 = [quantifierset,varset,'formula']
formulaproductions.append(rule4)




#define the production for predicates
predicatelist= []
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
		sys.exit()

	predicatestring = predicatename	#supposed to be like P[variables,variables]

	predicatestring = predicatename+"["

	#print the production for predicates
	#we check for i=0 in order to get the proper formatting with | symbol
	if i==0:

		#predicate name and opening bracket
		print(predicatename+"[",end="")
		#'variable' repeated arity times 
		for i in range(int(arity)-1):
			print("variable, ",end="")

			#append to predicatestring
			predicatestring = predicatestring + "variable,"

		predicatestring = predicatestring +"variable]"
		predicatelist.append(predicatestring)
		print("variable]",end=" ")

		continue


	print("|",predicatename+"[",end="")

	#'variable' repeated arity times 
	for i in range(int(arity)-1):
		print("variable, ",end="")

		#append to predicatestring
		predicatestring = predicatestring + "variable"

	predicatestring = predicatestring + "variable]"
	predicatelist.append(predicatestring)
	print("variable]",end=" ")


#append to formulaproductions
formulaproductions.append(predicatelist)


#add the negation formula element
print("| ",negationelement," formula")
negationlist = [negationelement,'formula']
formulaproductions.append(negationlist)
print("\n")

#add formulaproductions to the dict
productiondict['formula']=formulaproductions
print("dict is ", productiondict)




#we test whether the formula is valid by trying to recreate the string with the production rules



