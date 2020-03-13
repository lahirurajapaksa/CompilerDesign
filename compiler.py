import sys
import string
import re
from anytree import Node, RenderTree
from anytree.exporter import DotExporter
########################################## Read the input ########################################
f = open("Errors.log","w")
#store the file in a list, with each new line as a new element
lines = list(open("example.txt"))
validsets = ["variables:","constants:","predicates:","equality:","connectives:","quantifiers:"]
productiondict={}
i=0
while i<(len(lines)):

	formulaFound=False

	currentline = lines[i]
	#print(currentline)
	#strip the line of whitespace and trailing newline char
	currentline.strip()
	currentline = currentline.strip('\n')
	currentline = currentline.strip('\t')

	currentline=' '.join(currentline.split())
	#print("AFTer",currentline)


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
		f.write("ERROR in input file: invalid tag used, can only be variables, constants, predicates, equality, connectives, quantifiers or formula\n")
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
	f.write("ERROR in input file: equality is blank, must be cardinality of 1\n")
	sys.exit()

connectives = connectives.strip()
connectives = connectives.split(' ')
print("connectives =", connectives)


quantifiers = quantifiers.strip()
quantifiers = quantifiers.split(' ')
print("quantifiers =", quantifiers)

#print("String here")
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
	
	else:
		#print("MAP THIS!",formula[i])
		# formula[i] = list(map(str,formula[i]))
		#print("formula i is ",formula[i])
		s=formula[i]
		s=[s.strip() for s in  re.split(r'([\(\),])', s.strip()) if s]
		#print("S is ",s)
		newformula.extend(s)
print("new formula is",newformula)

print("Set of terminals: ",end =" ")



print("Set of non-terminals: start, variable, constant, equality, connectives, quantifiers, term, predicate, formula\n")
#iterate through formula and split the 

#check whether constants, predicates and variables all have different names
check = any(item in variables for item in constants)

if check == True:
	f.write("ERROR in input file: Variables and constants cant be the same\n")
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
			f.write("ERROR in input file: incorrect variable name, must only contain alphanumeric characters and underscore\n")
			sys.exit()
	if i==0:
		print(currentvariable, end=" ")
		continue

	print("|",currentvariable, end=" ")

print('\n')

#store it in the dict 
productiondict['variables']=variables


#define the production for constants
print("constant ->", end = " ")
for i in range(len(constants)):
	currentconstant = constants[i]

	for j in range(len(currentconstant)):
		if (currentconstant[j].isalpha()==True) or (currentconstant[j] in validname):
			continue
		else:
			print("\n")
			f.write("ERROR in input file: incorrect constant name, must only contain alphanumeric characters and underscore\n")
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
	f.write("ERROR in input file: Equality set is not equal to size 1\n")
	sys.exit()
for i in range(len(equality)):
	currentequality = equality[i]

	for j in range(len(currentequality)):
		if (currentequality[j].isalpha()==True) or (currentequality[j] in validname) or (currentequality[j]=="=") or (currentequality[j]=="\\"):
			continue
			
		else:
			f.write("ERROR in input file: incorrect equality used, must be alphanumeric, = or \\ \n")
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
	f.write("ERROR in input file: connectives set is not of size 5\n")
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
			f.write("ERROR in input file: incorrect connective name used, must contain alphanumeric characters, underscore or \\ \n")
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
			f.write("ERROR in input file: incorrect quantifier name used, must be alphanumeric, underscore or \\ \n")
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
		f.write("ERROR in input file: predicate does not satisfy minimum length of 4\n")
		sys.exit()

	#check if the last element is a closing bracket
	if currentpredicate[-1]!="]":
		f.write("ERROR in input file: the predicate format is incorrect, last character should be a closing bracket\n")
		sys.exit()
	#check if there is an opening bracket
	elif "[" not in currentpredicate:
		f.write("ERROR in input file: the predicate format is incorrect, should have a opening bracket\n")
		sys.exit()

	#check whether the open and closed bracket occur only once
	opencount = currentpredicate.count('[')
	closedcount = currentpredicate.count(']')

	if ((opencount!=1) or (closedcount!=1)):
		f.write("ERROR in input file: predicate has too many brackets\n")
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
			f.write("ERROR in input file: predicate name character is not alphanumeric or an underscore\n")
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
			f.write("ERROR in input file: arity is not numeric\n")
			sys.exit()
	predicatearity.append(arity)

	#check whether the predicate names are the same as any of the variable names
	if predicatename in variables:
		f.write("ERROR in input file: predicate name cannot be the same as a variable name\n")
		sys.exit()
	elif predicatename in constants:
		f.write("ERROR in input file: predicate name cannot be the same as a constant name\n")
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
print('| quantifier variable formula',end=" ")
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
global parentpointer

uniqueids = 0

def match():
	global lookahead
	lookahead+=1

#define procedure for every non -terminal
def start():
	global Start
	Start = Node("start")

	global Formulanode
	Formulanode = Node("formula", parent = Start)



	x = formulaproc()
	print("formula proc result is ", x)


def variableproc():
	global parentpointer

	global lookahead
	#access the variable dict
	variablerules = productiondict['variables']

	if formula[lookahead] in variablerules:
		#print("variable match")
		global uniqueids
		currentnode = [Node(formula[lookahead] + "\r"*uniqueids)]
		
		uniqueids +=1
		return 1,currentnode
	else:
		# f.write('ERROR in validation: '+formula[lookahead]+' did not match a variable\n')
		# sys.exit()
		#print(formula[lookahead],"is not a variable")
		return 0,"nothing"

def constantproc():
	global parentpointer

	global lookahead
	#access the constant dict
	constantrules = productiondict['constants']

	if formula[lookahead] in constantrules:
		#print('constant match')
		global uniqueids
		currentnode = [Node(formula[lookahead]+ "\r"*uniqueids)]
		
		uniqueids +=1
		return 1,currentnode
	else:
		# f.write('ERROR in validation: '+formula[lookahead]+' did not match a constant\n')
		# sys.exit()
		#print("Error in constant function: Constant did not match")
		#print(formula[lookahead],"is not a constant")
		return 0,"nothing"




def termproc():
	global lookahead
	#access the term rules
	termrules = productiondict['terms']

	varresult, vardata = variableproc()
	constresult, constdata = constantproc()

	if (varresult==1 or constresult==1):
		#print('term match')
		global uniqueids
		currentnode = [Node(formula[lookahead]+ "\r"*uniqueids)] 
		
		uniqueids +=1
		return 1,currentnode
	else:
		# f.write('ERROR in validation: '+formula[lookahead]+' did not match a term\n')
		# sys.exit()
		#print('term did not match',formula[lookahead])
		notthere = "nothing"
		return 0,notthere



def equalityproc():
	global lookahead
	#access the equality rule
	equalityrule = productiondict['equality']

	if formula[lookahead] == equalityrule[0]:
		#print("equality rule match")
		global uniqueids
		currentnode = [Node(formula[lookahead]+ "\r"*uniqueids)]
		
		uniqueids +=1
		#match()
		return 1,currentnode


	else:
		# f.write('ERROR in validation: '+formula[lookahead]+' did not match the equality symbol\n')
		# sys.exit()
		#print("ERROR in equality function: equality does not match")
		#print(formula[lookahead],"is not an equality")
		notthere = "nothing"
		return 0,notthere


def connectiveproc():
	global lookahead
	global parentpointer
	#access the connectives rule
	connectivesrule = productiondict['connectives']
	#print("Connectives",connectivesrule)
	if formula[lookahead] in connectivesrule:
		#print('Connectives match')
		global uniqueids
		currentnode = [Node(formula[lookahead]+ "\r"*uniqueids)]
		
		uniqueids +=1
		return 1,currentnode
	else:
		# f.write('ERROR in validation: '+formula[lookahead]+' did not match a connective\n')
		# sys.exit()
		#print("ERROR in connectives function")
		#print(formula[lookahead]," is not a connective")
		return 0,"nothing"



def quantifierproc():
	global lookahead
	global parentpointer
	#access the quantifier rule
	quantifiersrule = productiondict['quantifiers']

	if formula[lookahead] in quantifiersrule:
		#print('Quantifiers match')
		global uniqueids
		currentnode = [Node(formula[lookahead]+ "\r"*uniqueids)]
		
		uniqueids +=1
		return 1, currentnode
	else:
		# f.write('ERROR in validation: '+formula[lookahead]+' did not match a quantifier\n')
		# sys.exit()
		#print("ERROR in quantifiers function")
		#print(formula[lookahead]," is not a quantifier")
		return 0,"nothing"


def predicateproc():
	global parentpointer
	currentnode =[]
	global lookahead
	global uniqueids
	#access the predicate rules
	predicaterules = productiondict['predicate']
	names = productiondict['predicatenames']
	aritylist = productiondict['predicatearity']

	found = False
	for i in range(len(predicaterules)):

		#print("formula lookahead is ",formula[lookahead])
		if formula[lookahead] in names:
			#print(formula[lookahead]," in names list, so match")
			prednode = [Node(formula[lookahead]+'\r'*uniqueids)]
			currentnode.extend(prednode)

			match()
			

			if formula[lookahead] == "(":
				match()
				#print(formula[lookahead], "is (, so match")

				currentarity = aritylist[i]

				#print("Current arity is ",currentarity)

				for j in range(int(currentarity)):
					#iterate through the arity
					varresult, vardata = variableproc()
					if varresult == 1:
						
						#add this to the node list
						varthisnode = [Node(formula[lookahead]+ '\r'*uniqueids)]
						#varthisnode = [Node(formula[lookahead])]
						#print("var node",varthisnode)
						currentnode.extend(varthisnode)
						match()

					if formula[lookahead] == ",":
						
						match()

				
				#print("predicate current node 1",currentnode)
				#now make everything the child of the predicate name - which will be the parent in this case
				for k in range(1,len(currentnode)):
					currentnode[k].parent = currentnode[0]

				#print("predicate current node",currentnode)

				if formula[lookahead] == ")":
					#match()
					#currentnode = [Node(formula[lookahead])]
					found = True
					print("Predicate match")
					return 1,currentnode
				# else:
				# 	f.write('ERROR in validation: '+formula[lookahead]+' did not match the closing bracket of predicate\n')
				# 	sys.exit()

			else:
				# f.write('ERROR in validation: '+formula[lookahead]+' did not match the opening bracket of predicate\n')
				# sys.exit()
				#print(formula[lookahead],"is not (")
				break
		
		else:
			# f.write('ERROR in validation: '+formula[lookahead]+' is not a given predicate name\n')
			# sys.exit()
			#print(formula[lookahead]," is not a valid predicate name")
			break


	if found == False:
		return 0,"nothing"

def termequalityterm():

	global parentpointer

	global lookahead
	treedata= []
	global uniqueids

	if formula[lookahead]=="(":
				match()

				term1check, dataterm1 = termproc() 
				if term1check ==1:
					match()

					equalitycheck, equalitydata = equalityproc()
					if equalitycheck==1:
						match()

						term2check, dataterm2 = termproc()
						if term2check==1:
							match()

							if formula[lookahead]==")":


								treedata.extend(equalitydata)
							
								treedata.extend(dataterm1)
								treedata.extend(dataterm2)
				
								#make the terms children of equality
								treedata[1].parent = treedata[0]
								treedata[2].parent = treedata[0]

								#print("term equality term nodes")
								#print(treedata)
								#match() #was commented out earlier
								return 1,treedata
							else:
								#lookahead = 0
								return 0,"nothing"
						else:
							#lookahead = 0
							return 0,"nothing"
					else:
						#lookahead = 0
						return 0,"nothing"
				else:
					#lookahead = 0
					return 0,"nothing"
	else:
		#lookahead = 0
		return 0,"nothing"


def fcf():
	global parentpointer

	global lookahead
	currentdata =[]

	if formula[lookahead]=="(":
		#print("fcf: ( match",formula[lookahead])
		match()

		formula1check, formula1data = formulaproc()
		#print("formula1data ",formula1data)
		if formula1check==1:
			#print("fcf: formula match",formula[lookahead])
			match()

			connectivecheck, connectivedata = connectiveproc()
			if connectivecheck==1:
				#print("fcf: connective match",formula[lookahead])
				match()

				formula2check, formula2data = formulaproc()
				#print("formula2data",formula2data)
				if formula2check==1:
					#print("fcf: formula match",formula[lookahead])
					match()

					if formula[lookahead]==")":
						#print("fcf: ) match",formula[lookahead])
						#match()\
						currentdata.extend(connectivedata)
						#add the opening bracket

						formula1data[0].parent = currentdata[0]
						currentdata.extend(formula1data) 

						#make the first element of formula2data the child of connective 

						formula2data[0].parent = currentdata[0]
						currentdata.extend(formula2data)


						#print("current data is ",currentdata)

						#make the first element of formula1data the child of connective
						#currentdata[1].parent = currentdata[0]


						# print("fcf")
						# print(currentdata)
						# print(currentdata[0])
						# print(currentdata[1])
						# print(currentdata[2])


						return 1, currentdata
					else:
						#print("fcf: NO ) match",formula[lookahead])
						#lookahead =0 
						return 0,"nothing"

				else:
					#print("fcf: NO second formula match",formula[lookahead])
					#lookahead = 0
					return 0,"nothing"

			else:
				#print("fcf: NO connective match",formula[lookahead])
				#lookahead = 0
				return 0,"nothing"

		else:
			#print("fcf: NO first formula match",formula[lookahead])
			#lookahead = 0
			return 0,"nothing"
	else:
		#print("fcf: NO ( match",formula[lookahead])
		#lookahead = 0
		return 0,"nothing"

def qvf():
	global parentpointer

	global lookahead

	currentdata=[]

	checkquantifier, quantifierdata = quantifierproc()

	if checkquantifier==1:
		#print("qvf: quantifier match",formula[lookahead])
		match()

		checkvariable, variabledata = variableproc()
		if checkvariable==1:
			#print("qvf: variable match",formula[lookahead])
			match()

			formulacheck, formuladata = formulaproc()
			if formulacheck==1:
				#print("qvf: formula match",formula[lookahead])
				#match() #this was commented out earlier - match()
				currentdata.extend(quantifierdata)
				currentdata.extend(variabledata)
				
				currentdata.extend(formuladata)

				currentdata[1].parent = currentdata[0]
				currentdata[2].parent = currentdata[0]


				return 1,currentdata

			else:
				#print("qvf: formula NO match",formula[lookahead])
				#lookahead =0
				return 0,"nothing"

		else:
			#print("qvf: variable NO match",formula[lookahead])
			#lookahead =0
			return 0,"nothing"

	else:
		#print("qvf: quantifier NO match",formula[lookahead])
		#lookahead =0
		return 0,"nothing"


def negformula():
	global lookahead

	global parentpointer
	currentdata= []
	#negation element should be used here
	if formula[lookahead] ==negationelement:
		#print("Negformula: \\neg match",formula[lookahead])
		negationNode = [Node(formula[lookahead]+'\r'*uniqueids)]
		match()

		formulacheck, formuladata = formulaproc()
		if formulacheck==1:

			currentdata.extend(negationNode)
			formuladata[0].parent = currentdata[0]
			currentdata.extend(formuladata)
			return 1, currentdata


		else:
			return 0,"nothing"

	else:
		#print("Negformula: \\neg NO match",formula[lookahead])
		#lookahead = 0 
		return 0,"nothing"



def formulaproc():
	global parentpointer

	global lookahead
	
	currentdata=[]

	#call fcf 
	initlook = lookahead

	#print("Calling formula connective formula")

	fcfresult, fcfdata = fcf()
	if fcfresult == 0:

		print(" formula connective formula result is 0 ")

		lookahead = initlook

		#call qvf
		print("Calling quantifier variable formula")
		qvfresult, qvfdata = qvf()
		if qvfresult == 0:
			print("Quantifer variable formula result is 0")

			lookahead = initlook

			print("Calling neg formula")
			negresult, negdata = negformula()
			if negresult == 0:
				print("Neg formula result is 0")

				lookahead = initlook

				print("callinf predicate formula")
				predresult, preddata = predicateproc()

				if predresult == 0:
					print("predicate result is 0")
					lookahead = initlook

					print("calling term equality term function")
					tetresult, tetdata = termequalityterm()

					if tetresult == 0:
						print("term equality term result is 0")
						print("not a valid formula")
						f.write("ERROR in validation: Input formula cannot be produced with (term equality term), (formula connective formula), quantifier variable formula, negation formula or predicate \n")
						f.write("Therefore, this is an invalid input formula\n")
						sys.exit()
						return 0,"invalid"

					else:
						#check that the lookahead = len(formula), this will account for weird inputs with extra brackets and all
						currentdata.extend(tetdata)

						print("formula is term equality term")
						f.write("Passed validation: The formula is valid\n")
						return 1, currentdata

				else:
					currentdata.extend(preddata)
					print("formula is predicate")
					f.write("Passed validation: The formula is valid\n")
					return 1, currentdata
			else:
				# print('hello')
				# print(negdata)
				currentdata.extend(negdata)
				print("formula is neg formula")
				f.write("Passed validation: The formula is valid\n")
				return 1, currentdata
		else:
			currentdata.extend(qvfdata)
			print("formula is quantifier variable formula")
			f.write("Passed validation: The formula is valid\n")
			return 1, currentdata
	else:
		currentdata.extend(fcfdata)
		print("formula is fcf")
		f.write("Passed validation: The formula is valid\n")
		return 1, currentdata


lookahead = 0
#start()

#make the graph

#result,data = termequalityterm()


#DotExporter(Start).dot_dotfile("graph.dot")
#DotExporter(data[0]).to_picture("test2.png")

result, data = formulaproc()
DotExporter(data[0]).to_picture("test4.png")

# DotExporter(data[0]).to_dotfile("graph.dot")
# check_call(['dot','-Tpng','graph.dot','-o','test3.png'])
