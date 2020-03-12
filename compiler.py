import sys
import string
import re
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

	currentline=' '.join(currentline.split())
	print("AFTer",currentline)


	 #split the line based on the colon
	colonSplit = currentline.split(":")


#	print("colonSplit is ", colonSplit)

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
		sys.exit()

	#use a while loop

	if formulaFound==True:
		stop = False
		i=i+1
		while stop==False and i<len(lines):
			nextline = lines[i]
			nextline = nextline.strip('\n')
			nextline = nextline.strip('\t')

			#split the line in to several elements

			nextlinesplit = nextline.split()
			if nextlinesplit[0] in validsets:
				#the next line is not part of the formula
				#i=i-1
				stop = True
			elif nextlinesplit[0] not in validsets:
				#add it to the formula
				formula = formula +" "+str(nextline)
				i=i+1




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
#check whether nothing is given
if equality[0]=="":
	print("equality is blank")
	sys.exit()

connectives = connectives.strip()
connectives = connectives.split(' ')
print("connectives =", connectives)


quantifiers = quantifiers.strip()
quantifiers = quantifiers.split(' ')
print("quantifiers =", quantifiers)

print("String here")
print(formula)
formula = formula.strip()
formula = formula.split(' ')
print("formula =", formula)
print('\n')
newformula=[]
for i in range(len(formula)):
	# r = re.compile('|'.join([re.escape(w) for w in connectives]), flags=re.I)
	# check = r.findall(formula[i])

	if (formula[i] in quantifiers) or (formula[i] in connectives) or (formula[i] in variables) or (formula[i] in constants) or (formula[i] in equality):
		#print("just append, DO NOT MAP", formula[i])
		newformula.append(formula[i])
	
	# elif (len(check)>0):
	# 	print("check is ",check)
	# 	if (check[0] in connectives):
	# 		print(" CONNECTIVE !!!just append, DO NOT MAP", formula[i])
	# 		print(r.findall(formula[i]))
	# 		newformula.append(check[0])
	else:
		#print("MAP THIS!",formula[i])
		# formula[i] = list(map(str,formula[i]))
		#print("formula i is ",formula[i])
		s=formula[i]
		s=[s.strip() for s in  re.split(r'([\(\),])', s.strip()) if s]
		#print("S is ",s)
		newformula.extend(s)
print("new formula is",newformula)

#iterate through formula and split the 

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
#print("start -> formula | formula start | NULL ")
print("start -> formula")
#store the start symbol
#startlist = ['formula','start + formula','NULL']
startlist = ['formula']
productiondict['start'] = startlist
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

	for j in range(len(currentequality)):
		if (currentequality[j].isalpha()==True) or (currentequality[j] in validname) or (currentequality[j]=="="):
			continue
			
		else:
			print("\n")
			print("incorrect equality used, must be alphanumeric or =")
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

	for j in range(len(currentconnective)):
		if (currentconnective[j].isalpha()==True) or (currentconnective[j] in validname) or(currentconnective[j]=="\\"):
			continue
		else:
			print("\n")
			print("incorrect connective name used, must contain alphanumeric characters or _")
			sys.exit()

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

	for j in range(len(currentquantifier)):
		if (currentquantifier[j].isalpha()==True) or (currentquantifier[j] in validname) or (currentquantifier[j]=="\\"):
			continue
		else:
			print("\n")
			print("incorrect quantifier name used, must be alphanumeric or _")
			sys.exit()

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
print("term -> variable | constant\n")
termlist=['variable','constant']
productiondict['terms'] = termlist





print("predicate -> ",end=" ")


#define the production for predicates
predicatelist= []
predicatenames = []
predicatearity = []
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

	predicatenames.append(predicatename)

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
	predicatearity.append(arity)

	#check whether the predicate names are the same as any of the variable names
	if predicatename in variables:
		print("predicate name is the same as a variable name")
		sys.exit()
	elif predicatename in constants:
		print("predicate name is the same as a constant name")
		sys.exit()

	predicatestring = predicatename	#supposed to be like P[variables,variables]

	predicatestring = predicatename+"("

	#print the production for predicates
	#we check for i=0 in order to get the proper formatting with | symbol
	if i==0:

		#predicate name and opening bracket
		print(predicatename+"(",end="")
		#'variable' repeated arity times 
		for i in range(int(arity)-1):
			print("variable, ",end="")

			#append to predicatestring
			predicatestring = predicatestring + "variable,"

		predicatestring = predicatestring +"variable)"
		predicatelist.append(predicatestring)
		print("variable)",end=" ")

		continue


	print("|",predicatename+"(",end="")

	#'variable' repeated arity times 
	for i in range(int(arity)-1):
		print("variable, ",end="")

		#append to predicatestring
		predicatestring = predicatestring + "variable"

	predicatestring = predicatestring + "variable)"
	predicatelist.append(predicatestring)
	print("variable)",end=" ")

	productiondict['predicate']=predicatelist
	productiondict['predicatenames'] = predicatenames
	productiondict['predicatearity'] = predicatearity


print('\n')







#use the term rule to define the primitive formula rule

#define rule 2 (C = D), (C = x), (x = C) and (x = y) are valid

print("formula -> (term equality term) |",end=" ")
#get the equality set
equals = productiondict['equality']
rule2 = ['(','term','equality','term',')']
formulaproductions.append(rule2)




#define formula connective formula
print('(formula connective formula)',end=" ")

connectiveset = productiondict['connectives']
rule3 = ['(','formula','connectives','formula',')']
formulaproductions.append(rule3)

 
#define rule 4 - there exists x formula, for all x formula as long as x is a variable



#define quantifier variable formula
print('| quantifier variable formula|',end=" ")
quantifierset = productiondict['quantifiers']
varset = productiondict['variables']

rule4 = ['quantifiers','variable','formula']
formulaproductions.append(rule4)




#add the negation formula element
print("| ",negationelement,"formula",end=" ")
negationlist = ['(',negationelement,'formula']
formulaproductions.append(negationlist)



#add predicate to formulaproductions
print("| predicate")
print('\n')
formulaproductions.append(['predicate'])
print("\n")
#add formulaproductions to the dict
productiondict['formula']=formulaproductions
print("dict is ", productiondict)


#recursive descent parser

#list of non-terminals 
nonterminals = ['start','variable','constants','equality','connectives','quantifiers','term','formula']

formula = newformula

# #define input pointer and descent pointers
#lookahead = 0
# #define match procedure (this will be executed if the current token is a terminal)
# #can build the tree here in the same go

def match():
	global lookahead
	lookahead+=1

#define procedure for every non -terminal
def start():
	x = formulaproc()
	print("formula proc result is ", x)


def variableproc():
	global lookahead
	#access the variable dict
	variablerules = productiondict['variables']

	if formula[lookahead] in variablerules:
		print("variable match")
		return 1
	else:
		print('Error in variable function: Variable did not match')
		print(formula[lookahead],"is not a variable")
		return 0



def constantproc():
	global lookahead
	#access the constant dict
	constantrules = productiondict['constants']

	if formula[lookahead] in constantrules:
		print('constant match')
		return 1
	else:
		print("Error in constant function: Constant did not match")
		print(formula[lookahead],"is not a constant")
		return 0




def termproc():
	#access the term rules
	termrules = productiondict['terms']

	if (variableproc()==1 or constantproc()==1):
		print('term match')
		return 1
	else:
		print('term did not match')
		return 0



def equalityproc():
	#access the equality rule
	equalityrule = productiondict['equality']

	if formula[lookahead] == equalityrule[0]:
		print("equality rule match")
		#match()
		return 1
	else:
		print("ERROR in equality function: equality does not match")
		print(formula[lookahead],"is not an equality")
		return 0


def connectiveproc():
	#access the connectives rule
	connectivesrule = productiondict['connectives']
	print("Connectives",connectivesrule)
	if formula[lookahead] in connectivesrule:
		print('Connectives match')
		return 1
	else:
		print("ERROR in connectives function")
		print(formula[lookahead]," is not a connective")
		return 0



def quantifierproc():
	#access the quantifier rule
	quantifiersrule = productiondict['quantifiers']

	if formula[lookahead] in quantifiersrule:
		print('Quantifiers match')
		return 1
	else:
		print("ERROR in quantifiers function")
		print(formula[lookahead]," is not a quantifier")
		return 0


def predicateproc():
	global lookahead
	#access the predicate rules
	predicaterules = productiondict['predicate']
	names = productiondict['predicatenames']
	aritylist = productiondict['predicatearity']

	found = False
	for i in range(len(predicaterules)):
		#currentpredicate = predicate[i]
		print("formula lookahead is ",formula[lookahead])
		if formula[lookahead] in names:
			print(formula[lookahead]," in names list, so match")
			match()
			if formula[lookahead] == "(":
				match()
				print(formula[lookahead], "is (, so match")

				currentarity = aritylist[i]

				print("Current arity is ",currentarity)

				for j in range(int(currentarity)):
					#iterate through the arity
					if variableproc() == 1:
						match()
					if formula[lookahead] == ",":
						match()

				if formula[lookahead] == ")":
					#match()
					found = True
					print("Predicate match")
					return 1

			else:
				print(formula[lookahead],"is not (")
				break
		
		else:
			print(formula[lookahead]," is not a valid predicate name")
			break


	if found == False:
		return 0

def termequalityterm():
	global lookahead

	if formula[lookahead]=="(":
				match()

				if termproc() ==1:
					match()

					if equalityproc()==1:
						match()

						if termproc()==1:
							match()

							if formula[lookahead]==")":
								#match() #was commented out earlier
								return 1
							else:
								#lookahead = 0
								return 0
						else:
							#lookahead = 0
							return 0
					else:
						#lookahead = 0
						return 0
				else:
					#lookahead = 0
					return 0
	else:
		#lookahead = 0
		return 0


def fcf():
	global lookahead

	if formula[lookahead]=="(":
		print("fcf: ( match",formula[lookahead])
		match()

		if formulaproc()==1:
			print("fcf: formula match",formula[lookahead])
			match()

			if connectiveproc()==1:
				print("fcf: connective match",formula[lookahead])
				match()

				if formulaproc()==1:
					print("fcf: formula match",formula[lookahead])
					match()

					if formula[lookahead]==")":
						print("fcf: ) match",formula[lookahead])
						#match()
						return 1
					else:
						print("fcf: NO ) match",formula[lookahead])
						#lookahead =0 
						return 0

				else:
					print("fcf: NO second formula match",formula[lookahead])
					#lookahead = 0
					return 0

			else:
				print("fcf: NO connective match",formula[lookahead])
				#lookahead = 0
				return 0

		else:
			print("fcf: NO first formula match",formula[lookahead])
			#lookahead = 0
			return 0
	else:
		print("fcf: NO ( match",formula[lookahead])
		#lookahead = 0
		return 0

def qvf():
	global lookahead

	if quantifierproc()==1:
		print("qvf: quantifier match",formula[lookahead])
		match()

		if variableproc()==1:
			print("qvf: variable match",formula[lookahead])
			match()

			if formulaproc()==1:
				#print("qvf: formula match",formula[lookahead])
				#match() #this was commented out earlier - match()
				return 1

			else:
				print("qvf: formula NO match",formula[lookahead])
				#lookahead =0
				return 0

		else:
			print("qvf: variable NO match",formula[lookahead])
			#lookahead =0
			return 0

	else:
		print("qvf: quantifier NO match",formula[lookahead])
		#lookahead =0
		return 0


def negformula():
	global lookahead
	#negation element should be used here
	if formula[lookahead] ==negationelement:
		print("Negformula: \\neg match",formula[lookahead])
		match()

		if formulaproc()==1:
			#print("Negformula: formula match",formula[lookahead])
			#match() #was commented out earlier
			return 1

		else:
			#print("Negformula: formula NO match",formula[lookahead])
			#lookahead = 0
			return 0

	else:
		print("Negformula: \\neg NO match",formula[lookahead])
		#lookahead = 0 
		return 0





def formulaproc():

	global lookahead

	#call fcf 
	initlook = lookahead

	print("Calling formula connective formula")

	fcfresult = fcf()
	if fcfresult == 0:
		print(" formula connective formula result is 0 ")

		lookahead = initlook


		#call qvf
		print("Calling quantifier variable formula")
		qvfresult = qvf()
		if qvfresult == 0:
			print("Quantifer variable formula result is 0")

			lookahead = initlook

			print("Calling neg formula")
			negresult = negformula()
			if negresult == 0:
				print("Neg formula result is 0")

				lookahead = initlook

				print("callinf predicate formula")
				predresult = predicateproc()

				if predresult == 0:
					print("predicate result is 0")
					lookahead = initlook

					print("calling term equality term function")
					tetresult = termequalityterm()

					if tetresult == 0:
						print("term equality term result is 0")
						print("not a valid formula")
						return 0

					else:
						print("formula is term equality term")
						return 1

				else:
					print("formula is predicate")
					return 1
			else:
				print("formula is neg formula")
				return 1
		else:
			print("formula is quantifier variable formula")
			return 1
	else:
		print("formula is fcf")
		return 1


lookahead = 0
start()



