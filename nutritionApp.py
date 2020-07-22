import random
from tkinter import *
from tkinter import ttk


root = Tk()

protienSource = ['b#N:eggs#C:0.6#F:5#P:6#K:78','b#N:greekYoghurt#C:7.2#F:9#P:15#K:170','b#N:skimmedMilk#C:9#F:1#P:6#K:65','o#N:tilapia#C:2#F:1.7#P:26#K:128','o#N:chickenB#C:0#F:3.6#P:30#K:165','o#N:chickenT#C:0#F:11#P:26#K:209' , 'o#N:tunaCan#C:1#F:2#P:25#K:123','o#N:CottageCheese#C:3.4#F:4.3#P:11#K:99', 'o#N:Greeyo#C:2#F:0.3#P:9#K:45']
fatSource = ['b#N:cashew#C:30#F:44#P:18#K:5', 'b#N:peanutButter#C:6#F:16#P:8#K:190', 'b#N:pistachio#C:28#F:45#P:20#K:6' , 'b#N:almond#C:22#F:49#P:21#K:6']
carbSource = ['b#N:oats#C:65.7#F:8#P:13#K:392' , 'o#N:whiteRice#C:79#F:0.6#P:7#K:360' , 'o#N:brownRice#C:76#F:2.7#P:8#K:362' , 'o#N:basmatiRice#C:80#F:1#P:7#K:90' , 'b#N:honey#C:17#F:0#P:0#K:64']
vegetables = ['o#N:cucumber#C:0#F:0#P:0#K:16', 'o#N:tomato#C:0#F:0#P:0#K:24', 'o#N:cannedMushroom#C:0#F:0#P:0#K:38' , 'o#N:onion#C:0#F:0#P:0#K:44']
fruits = ['o#N:apple#C:25#F:0.3#P:0.5#K:95' , 'o#N:guava#C:24#F:1.6#P:4.2#K:110' ,'o#N:peach#C:15#F:0#P:1.4#K:70' , 'o#N:oranges#C:15#F:0.2#P:1.2#K:62' , 'o#N:orangeJuice#C:28#F:0#P:1#K:110' , 'b#N:avocado#C:4#F:15#P:2#K:168']



root.title('Nutrition App')
root.geometry("750x500")
root.configure(background='#228B22')
weightLabel = Label(root , text="weight")
weightLabel.config(foreground = '#FFFAF1' , background = '#228B22' , font =  ('times', 20, 'bold'))
weightLabel.pack()
weightEntry = Entry(root, width = 35 )
weightEntry.configure(background = '#FFFAF1' , foreground = '#228B22')
weightEntry.pack()

heightLabel = Label(root , text="height")
heightLabel.config(foreground = '#FFFAF1' , background = '#228B22' , font =  ('times', 20, 'bold'))
heightLabel.pack()
heightEntry = Entry(root, width = 35)
heightEntry.configure(background = '#FFFAF1' , foreground = '#228B22')
heightEntry.pack()

ageLabel = Label(root , text="age")
ageLabel.config(foreground = '#FFFAF1' , background = '#228B22' , font =  ('times', 20, 'bold'))
ageLabel.pack()
ageEntry = Entry(root, width = 35)
ageEntry.configure(background = '#FFFAF1' , foreground = '#228B22')
ageEntry.pack()

genderLabel = Label(root , text="gender")
genderLabel.config(foreground = '#FFFAF1' , background = '#228B22' , font =  ('times', 20, 'bold'))
genderLabel.pack()

genderVariable = StringVar(root)
genderVariable.set("gender") # default value

genderEntry = OptionMenu(root, genderVariable, "male", "female")
genderEntry.config(background = '#FFFAF1' , foreground = '#228B22' , width = 30)
genderEntry.pack()

activityRateLabel = Label(root , text="activity rate")
activityRateLabel.config(foreground = '#FFFAF1' , background = '#228B22' , font =  ('times', 20, 'bold'))
activityRateLabel.pack()

activityRateVariable = StringVar(root)
activityRateVariable.set("activityRate")

activityRateEntry = OptionMenu(root, activityRateVariable, "1 - having desk job and engage in very little exercise or chores", "2 - doing chores and go on long walks/engage in exercise at least 1 to 3 days a week", "3 - moving alot during the day and workout (moderate effort) at least 3 to 5 days in a week" , "4 - playing sports or engaging in vigorous exercise on most days" , "5 - doing intense workouts 6 to 7 days a week with work that demands physical activity")
activityRateEntry.config(background = '#FFFAF1' , foreground = '#228B22' , width = 30)
activityRateEntry.pack()

targetLabel = Label(root , text="target")
targetLabel.config(foreground = '#FFFAF1' , background = '#228B22' , font =  ('times', 20, 'bold'))
targetLabel.pack()

targetVariable = StringVar(root)
targetVariable.set("target")

targetEntry = OptionMenu(root, targetVariable, "gain weight", "lose weight", "stay the same weight")
targetEntry.config(background = '#FFFAF1' , foreground = '#228B22' , width = 30)
targetEntry.pack()

menteLabel = Label(root , text=" ")
menteLabel.config(foreground = '#FFFAF1' , background = '#228B22' , font =  ('times', 20, 'bold'))
menteLabel.pack()

avoidInDiet = []

def getName(x):
	i = 0
	flag = False
	out = ''
	while i < len(x):
		if(x[i] == 'N' and x[i+1] == ':'):
			flag = True
			i = i+2
		else:
			i = i+1	
		if(flag == True):
			if(x[i] != '#'):
				out = out + x[i]
			else:
				break
	return out

def isInDatabase(x):
	i = 0
	while i < len(protienSource):
		if(x == getName(protienSource[i])):
			return True
		i = i+1	
	i = 0
	while i < len(fatSource):
		if(x == getName(fatSource[i])):
			return True
		i = i+1	
	i = 0
	while i < len(carbSource):
		if(x == getName(carbSource[i])):
			return True
		i = i+1	
	i = 0
	while i < len(protienSource):
		if(x == getName(protienSource[i])):
			return True
		i = i+1	
	i = 0
	while i < len(vegetables):
		if(x == getName(vegetables[i])):
			return True
		i = i+1	
	i = 0	
	while i < len(fruits):
		if(x == getName(fruits[i])):
			return True
		i = i+1
	return False


								




def getCarbAsInt(x):
	i = 0
	flag = False
	out = ''
	while i < len(x):
		if(x[i] == 'C' and x[i+1] == ':'):
			flag = True
			i = i+2
		else:
			i = i+1	
		if(flag == True):
			if(x[i] != '#'):
				out = out + x[i]
			else:
				break
	return float(out) 		 			 

def getFatAsInt(x):
	i = 0
	flag = False
	out = ''
	while i < len(x):
		if(x[i] == 'F' and x[i+1] == ':'):
			flag = True
			i = i+2
		else:
			i = i+1	
		if(flag == True):
			if(x[i] != '#'):
				out = out + x[i]
			else:
				break
	return float(out) 	
def getProtienAsInt(x):
	i = 0
	flag = False
	out = ''
	while i < len(x):
		if(x[i] == 'P' and x[i+1] == ':'):
			flag = True
			i = i+2
		else:
			i = i+1	
		if(flag == True):
			if(x[i] != '#'):
				out = out + x[i]
			else:
				break
	return float(out) 	
def getCaloriesAsInt(x):
	i = 0
	flag = False
	out = ''
	while i < len(x)-1:
		if(x[i] == 'K' and x[i+1] == ':'):
			flag = True
			i = i+2
		else:
			i = i+1	
		if(flag == True):
				out = out + x[i]
	return float(out)

def getOneSourceName(x):
	i = 0 
	out = ''
	while i<len(x):
		if(x[i] == '#'):
			break
		else:
			out = out + x[i]
		i = i+1	
	return out


def getSpace(x):
	i = 0 
	outList = []
	while i < len(x):

		j = 0
		temp = ''
		while j < len(x[i]):

			if(x[i][j].isupper()):
				temp = temp + ' ' + x[i][j].lower()
			else:
				temp = temp + x[i][j]
			j = j + 1	
		outList.insert(len(outList) , temp)
		i = i+1
	return outList				


	
def firstTime(x , y):
	if(y == 0):
		return True
	z = y
	y = y -1
	while(y>=0):
		if(x[y] == x[z]):
			return False
		y = y-1
	return True

# to which source does x belong	
def toXBelong(x):
	i = 0
	while i < len(protienSource):
		if(x == getName(protienSource[i])):
			return 'P'
		i = i+1	
	i = 0
	while i < len(fatSource):
		if(x == getName(fatSource[i])):
			return 'F'
		i = i+1	
	i = 0
	while i < len(carbSource):
		if(x == getName(carbSource[i])):
			return 'C'
		i = i+1	
	i = 0
	while i < len(protienSource):
		if(x == getName(protienSource[i])):
			return 'P'
		i = i+1	
	i = 0
	while i < len(vegetables):
		if(x == getName(vegetables[i])):
			return 'V'
		i = i+1	
	i = 0	
	while i < len(fruits):
		if(x == getName(fruits[i])):
			return 'Fr'
		i = i+1
	return 'X'


def fromUserToCode(x):
	out = ''
	i = 0 
	while i < len(x):
		if(x[i] == ' ' and i < (len(x)-1)):
			out = out + x[i+1].upper()
			i = i+2
		else:
			out = out + x[i]
			i = i+1		
	return out			 


def translateTheFoodCode(x):
	i = 0
	out = ''
	allInAList = []
	while i < len(x):
		if(x[i] == '#'):
			allInAList.insert(0 , out)
			out = ''
		else:
			out = out + str(x[i])
		i = i+1	
	allInAList =  getSpace(allInAList)	
	i = 0
	n = 1
	out = ''
	while i < len(allInAList):

		if(firstTime(allInAList , i)):
			j = i+1
			n = 1
			if(j == len(allInAList)):
				out = out +  str(n) + 'x ' + allInAList[i]
			else:
				while j < len(allInAList):
					if(allInAList[j] == allInAList[i]):
						n = n + 1		
					j = j+1	
				out = out + str(n) + 'x ' + allInAList[i] + '\n'	
		i = i+1	
	return out		



				
def makeBreakfast(protienCalories , carbCalories , fatCalories , specialProtien , specialCarb , specialFat):
	print(specialCarb)
	out = 'Meal 1 \n'
	protienOut = ''
	carbOut = ''
	fatOut = ''
	specialBreakfastProtien = []
	specialBreakfastCarb = []
	specialBreakfastFat = []
	specialProtien = fromUserToCode(specialProtien)
	specialCarb = fromUserToCode(specialCarb)
	specialFat = fromUserToCode(specialFat)
	specialBreakfastProtien.insert(0 , specialProtien)
	specialBreakfastCarb.insert(0 , specialCarb)
	specialBreakfastFat.insert(0 , specialFat)
	if(not isInDatabase(specialBreakfastProtien[0])):
		specialBreakfastProtien = []
	if(not isInDatabase(specialBreakfastCarb[0])):
		specialBreakfastCarb = []
	if(not isInDatabase(specialBreakfastFat[0])):
		specialBreakfastFat = []	
			

	# adding protiens to the breakfast
	while protienCalories > 10:
		i = 0
		while i < len(protienSource):
			if(protienSource[i][0] == 'b' and not (getName(protienSource[i]) in avoidInDiet) and len(protienOut) == 0 and len(specialBreakfastProtien) == 0):
				if(protienCalories - getCaloriesAsInt(protienSource[i]) != 0):
					protienOut = protienOut + getName(protienSource[i]) + '#'
					protienCalories = protienCalories - getCaloriesAsInt(protienSource[i])
					#print('protienCalories', protienCalories)
					print(getName(protienSource[i]))
					break
			elif(len(specialBreakfastProtien) > 0 and protienSource[i][0] == 'b' and specialBreakfastProtien[0] == getName(protienSource[i]) and protienCalories - getCaloriesAsInt(protienSource[i]) != 0):
					protienOut = protienOut + getName(protienSource[i]) + '#'
					protienCalories = protienCalories - getCaloriesAsInt(protienSource[i])
					specialBreakfastProtien = []
					break

						
			elif(protienSource[i][0] == 'b'):
				oneSource = getOneSourceName(protienOut)
				if(( oneSource == getName(protienSource[i])) and protienCalories - getCaloriesAsInt(protienSource[i]) != 0):
					protienOut = protienOut + getName(protienSource[i]) + '#'
					protienCalories = protienCalories - getCaloriesAsInt(protienSource[i])
					break
			if(len(protienOut) == 0 and len(specialBreakfastProtien) != 0 and i > 40):
				specialBreakfastProtien = ''			


			i = i+1
# adding carb to the breakfast
	while carbCalories > 10:
		i = 0
		while i < len(carbSource):
			if(carbSource[i][0] == 'b' and not (getName(carbSource[i]) in avoidInDiet) and len(carbOut) == 0 and len(specialBreakfastCarb) == 0):
				if(carbCalories - getCaloriesAsInt(carbSource[i]) != 0):
					carbOut = carbOut + getName(carbSource[i]) + '#'
					carbCalories = carbCalories - getCaloriesAsInt(carbSource[i])
					break
			elif(len(specialBreakfastCarb) > 0 and carbSource[i][0] == 'b' and specialBreakfastCarb[0] == getName(carbSource[i]) and carbCalories - getCaloriesAsInt(carbSource[i]) != 0):
				carbOut = carbOut + getName(carbSource[i]) + '#'
				carbCalories = carbCalories - getCaloriesAsInt(carbSource[i])
				specialBreakfastCarb= []
				break		
			elif(carbSource[i][0] == 'b'):
				oneSource = getOneSourceName(carbOut)
				if(oneSource == getName(carbSource[i]) and carbCalories - getCaloriesAsInt(carbSource[i]) != 0):
					carbOut = carbOut + getName(carbSource[i]) + '#'
					carbCalories = carbCalories - getCaloriesAsInt(carbSource[i])
					break
			if(len(carbOut) == 0 and len(specialBreakfastCarb) != 0 and i>40):
				specialBreakfastCarb = ''			


			i = i+1	
# adding fat to the breakfast 
	while fatCalories > 10:
		i = 0
		while i < len(fatSource):
			randomNumber = random.randint(0 , len(fatSource) - 1)
			if(fatSource[randomNumber][0] == 'b' and not (getName(fatSource[randomNumber]) in avoidInDiet) and len(fatOut) == 0 and len(specialBreakfastFat) == 0):
				if(fatCalories - getCaloriesAsInt(fatSource[randomNumber]) != 0):
					fatOut = fatOut + getName(fatSource[randomNumber]) + '#'
					fatCalories = fatCalories - getCaloriesAsInt(fatSource[randomNumber])
					break
			elif(len(specialBreakfastFat) > 0 and fatSource[randomNumber][0] == 'b' and specialBreakfastFat[0] == getName(fatSource[randomNumber]) and fatCalories - getCaloriesAsInt(fatSource[randomNumber]) != 0):
				fatOut = fatOut + getName(fatSource[randomNumber]) + '#'
				fatCalories = fatCalories - getCaloriesAsInt(fatSource[randomNumber])
				specialBreakfastFat= []
				break			

			elif(fatSource[i][0] == 'b'):
				oneSource = getOneSourceName(fatOut)
				if(fatCalories - getCaloriesAsInt(fatSource[randomNumber]) != 0):
					fatOut = fatOut + getName(fatSource[randomNumber]) + '#'
					fatCalories = fatCalories - getCaloriesAsInt(fatSource[randomNumber])
					break
		if(len(fatOut) == 0 and len(specialBreakfastFat) != 0 and i>40):
			specialBreakfastFat = ''

			i = i+1

	#print(protienOut  , carbOut , fatOut)
	return protienOut + carbOut + fatOut


def makeMeal(protienCalories , carbCalories , fatCalories , numberOfThisMeal , specialProtien , specialCarb , specialFat):
	i = 0
	j = 0
	protienOut = ''
	carbOut = ''
	fatOut = ''
	vegetablesOut = ''
	fruitsOut = ''
	
	specialNormalProtien  = fromUserToCode(specialProtien)
	specialNormalCarb = fromUserToCode(specialCarb)
	specialNormalFat = fromUserToCode(specialFat)
	if(not isInDatabase(specialNormalProtien)):
		specialNormalProtien = ''
	if(not isInDatabase(specialNormalCarb)):
		specialNormalCarb = ''	
	if(not isInDatabase(specialNormalFat)):
		specialNormalFat = ''		


	if(numberOfThisMeal == 2):
		vegetablesCalories = 0.1*protienCalories + 0.1*carbCalories + 0.1*fatCalories
		fruitsCalories = 0.2*protienCalories + 0.1* carbCalories + 0.1*fatCalories
		protienCalories = protienCalories - (0.2*protienCalories)
		carbCalories = carbCalories - (0.1*carbCalories)
		fatCalories = fatCalories - (0.1* - fatCalories)
#adding vegetable to the meal
		while vegetablesCalories > 10:
			i = 0
			while i < len(vegetables):
				randomNumber = random.randint(0 , len(vegetables) - 1)
				if(vegetables[randomNumber][0] == 'o' and not (getName(vegetables[randomNumber]) in avoidInDiet) and len(vegetablesOut) == 0):
					if(vegetablesCalories - getCaloriesAsInt(vegetables[randomNumber]) != 0):
						vegetablesOut = vegetablesOut + getName(vegetables[randomNumber]) + '#'
						vegetablesCalories = vegetablesCalories - getCaloriesAsInt(vegetables[randomNumber])
						break		
				elif(vegetables[i][0] == 'o'):
					oneSource = getOneSourceName(vegetablesOut)
					if(oneSource != getName(vegetables[randomNumber]) and vegetablesCalories - getCaloriesAsInt(vegetables[randomNumber]) != 0):
						vegetablesOut = vegetablesOut + getName(vegetables[i]) + '#'
						vegetablesCalories = vegetablesCalories - getCaloriesAsInt(vegetables[randomNumber])
						break
			i = i+1
#addinf fruits to the meal
		while fruitsCalories > 10:
			i = 0
			while i < len(fruits):
				randomNumber = random.randint(0 , len(fruits) - 1)
				if(fruits[randomNumber][0] == 'o' and not (getName(fruits[randomNumber]) in avoidInDiet) and len(fruitsOut) == 0):
					if(fruitsCalories - getCaloriesAsInt(fruits[randomNumber]) != 0):
						fruitsOut = fruitsOut + getName(fruits[randomNumber]) + '#'
						fruitsCalories = fruitsCalories - getCaloriesAsInt(fruits[randomNumber])
						break		
				elif(fruits[i][0] == 'o'):
					oneSource = getOneSourceName(fruitsOut)
					if(oneSource != getName(fruits[randomNumber]) and fruitsCalories - getCaloriesAsInt(fruits[randomNumber]) != 0):
						fruitsOut = fruitsOut + getName(fruits[i]) + '#'
						fruitsCalories = fruitsCalories - getCaloriesAsInt(fruits[randomNumber])
						break
			i = i+1

	if(numberOfThisMeal == 3):
		vegetablesCalories = 0.1*protienCalories + 0.1*carbCalories + 0.1*fatCalories
		protienCalories = protienCalories - (0.1*protienCalories)
		carbCalories = carbCalories - (0.05*carbCalories)
		fatCalories = fatCalories - (0.05* - fatCalories)
		while vegetablesCalories > 10:
			i = 0
			while i < len(vegetables):
				randomNumber = random.randint(0 , len(vegetables) - 1)
				if(vegetables[randomNumber][0] == 'o' and not (getName(vegetables[randomNumber]) in avoidInDiet) and len(vegetablesOut) == 0):
					if(vegetablesCalories - getCaloriesAsInt(vegetables[randomNumber]) != 0):
						vegetablesOut = vegetablesOut + getName(vegetables[randomNumber]) + '#'
						vegetablesCalories = vegetablesCalories - getCaloriesAsInt(vegetables[randomNumber])
						break		
				elif(vegetables[i][0] == 'o'):
					oneSource = getOneSourceName(vegetablesOut)
					if(oneSource != getName(vegetables[randomNumber]) and vegetablesCalories - getCaloriesAsInt(vegetables[randomNumber]) != 0):
						vegetablesOut = vegetablesOut + getName(vegetables[i]) + '#'
						vegetablesCalories = vegetablesCalories - getCaloriesAsInt(vegetables[randomNumber])
						break
				i = i+1

	print('vor protien')
#adding protien to the meal

	while protienCalories > 10:
		i = 0
		while i < len(protienSource):
			if(protienSource[i][0] == 'o' and not (getName(protienSource[i]) in avoidInDiet) and len(protienOut) == 0 and len(specialNormalProtien) == 0):
				if(protienCalories - getCaloriesAsInt(protienSource[i]) != 0):
					protienOut = protienOut + getName(protienSource[i]) + '#'
					protienCalories = protienCalories - getCaloriesAsInt(protienSource[i])
					#print('protienCalories', protienCalories)
					print(getName(protienSource[i]))
					break
			elif(len(specialNormalProtien) > 0 and protienSource[i][0] == 'o' and specialNormalProtien == getName(protienSource[i]) and protienCalories - getCaloriesAsInt(protienSource[i]) != 0):
					protienOut = protienOut + getName(protienSource[i]) + '#'
					protienCalories = protienCalories - getCaloriesAsInt(protienSource[i])
					specialNormalProtien = ''
					break

						
			elif(protienSource[i][0] == 'o'):
				oneSource = getOneSourceName(protienOut)
				if(( oneSource == getName(protienSource[i])) and protienCalories - getCaloriesAsInt(protienSource[i]) != 0):
					protienOut = protienOut + getName(protienSource[i]) + '#'
					protienCalories = protienCalories - getCaloriesAsInt(protienSource[i])
					break
			if(len(protienOut) == 0 and i>40):
				specialNormalProtien = ''		


			i = i+1
	print('nach protien')		
# adding carb to the meal
	while carbCalories > 10:
		print('here 1')
		i = 0
		while i < len(carbSource):
			if(carbSource[i][0] == 'o' and not (getName(carbSource[i]) in avoidInDiet) and len(carbOut) == 0 and len(specialNormalCarb) == 0):
				if(carbCalories - getCaloriesAsInt(carbSource[i]) != 0):
					carbOut = carbOut + getName(carbSource[i]) + '#'
					carbCalories = carbCalories - getCaloriesAsInt(carbSource[i])
					break
			elif(len(specialNormalCarb) > 0 and carbSource[i][0] == 'o' and specialNormalCarb[0] == getName(carbSource[i]) and carbCalories - getCaloriesAsInt(carbSource[i]) != 0):
				carbOut = carbOut + getName(carbSource[i]) + '#'
				carbCalories = carbCalories - getCaloriesAsInt(carbSource[i])
				specialNormalCarb= ''
				break		
			elif(carbSource[i][0] == 'o'):
				oneSource = getOneSourceName(carbOut)
				if(oneSource == getName(carbSource[i]) and carbCalories - getCaloriesAsInt(carbSource[i]) != 0):
					carbOut = carbOut + getName(carbSource[i]) + '#'
					carbCalories = carbCalories - getCaloriesAsInt(carbSource[i])
					break
			if(len(carbOut) == 0 and len(specialNormalCarb) != 0 and i>40):
				specialNormalCarb = ''

			i = i+1	
# adding fat to the meal 
	"""k = 0
	while fatCalories > 10:
		print('here 3')
		i = 0
		while i < len(fatSource):
			if(fatSource[i][0] == 'o' and not (getName(fatSource[i]) in avoidInDiet) and len(fatOut) == 0 and len(specialNormalFat) == 0):
				if(fatCalories - getCaloriesAsInt(fatSource[i]) != 0):
					print('fat if 1')
					fatOut = fatOut + getName(fatSource[i]) + '#'
					fatCalories = fatCalories - getCaloriesAsInt(fatSource[i])
					break
			elif(len(specialNormalFat) > 0 and fatSource[i][0] == 'b' and specialNormalFat[0] == getName(fatSource[i]) and fatCalories - getCaloriesAsInt(fatSource[i]) != 0):
				fatOut = fatOut + getName(fatSource[i]) + '#'
				fatCalories = fatCalories - getCaloriesAsInt(fatSource[i])
				print('fat elif 1')
				specialNormalFat= ''
				break			

			elif(fatSource[i][0] == 'o'):
				oneSource = getOneSourceName(fatOut)
				if(oneSource == getName(fatSource[i]) and fatCalories - getCaloriesAsInt(fatSource[i]) != 0):
					fatOut = fatOut + getName(fatSource[i]) + '#'
					fatCalories = fatCalories - getCaloriesAsInt(fatSource[i])
					print('fat elif 2')
					break

			k = k+1
			if(k > 0 and len(fatOut) == 0):
				break		
			i = i+"""
		

	return protienOut + carbOut + fatOut + vegetablesOut + fruitsOut
	#print(vegetablesCalories , protienCalories , carbCalories , fatCalories)


def setNumberOfMeals():
	def secondWindow():
		def thirdWindow(): # breakfast
			def fourthWindow():
				def fifthWindow(): # the second meal (1st after breakfast)
					def sixthWindow():
						def seventhWindow(): # the third meal
							def eighthWindow():
								def finalReportAfterThird():  # final report after the third meal
									thirdMealTitelLabel.pack_forget()
									specialProtienForThirdMealLabel.pack_forget()
									specialCarbForThirdMealLabel.pack_forget()
									specialFatForThirdMealLabel.pack_forget()
									specialProtienForThirdMealEntry.pack_forget()
									specialCarbForThirdMealEntry.pack_forget()
									specialFatForThirdMealEntry.pack_forget()
									thirdMealLabel.pack_forget()
									getTheFinalReportAfterThirdMealButton.pack_forget()

									finalReport = "breakfast \n"
									finalReport = finalReport + breakfast + "\n \n"
									finalReport = finalReport + "second meal" + "\n"
									finalReport = finalReport + secondMeal + "\n\n"
									finalReport = finalReport + "third meal" + "\n"
									finalReport = finalReport + thirdMeal + "\n"
									finalReportLabel = Label(root , text = "FINAL REPORT")
									finalReportLabel.config(foreground = '#FFFAF1' , background = '#228B22' , font =  ('times', 20, 'bold'))
									finalReportLabel.pack()
									finalReportText = Text(root , height = 18 , width = 65)
									finalReportText.insert(INSERT , finalReport)
									finalReportText.pack()
								def ninthWindow(): #the fourth meal
									def tenthWindow():

										def finalReportAfterFourth():
											fourthMealTitelLabel.pack_forget()
											specialProtienForFourthMealLabel.pack_forget()
											specialCarbForFourthMealLabel.pack_forget()
											specialFatForFourthMealLabel.pack_forget()
											specialProtienForFourthMealEntry.pack_forget()
											specialCarbForFourthMealEntry.pack_forget()
											specialFatForFourthMealEntry.pack_forget()
											fourthMealLabel.pack_forget()
											getTheFinalReportAfterFourthMealButton.pack_forget()

											finalReport = "breakfast \n"
											finalReport = finalReport + breakfast + "\n \n"
											finalReport = finalReport + "second meal" + "\n"
											finalReport = finalReport + secondMeal + "\n\n"
											finalReport = finalReport + "third meal" + "\n"
											finalReport = finalReport + thirdMeal + "\n\n"
											finalReport = finalReport + "fourth meal" + "\n"
											finalReport = finalReport + fourthMeal + "\n\n"

											finalReportLabel = Label(root , text = "FINAL REPORT")
											finalReportLabel.config(foreground = '#FFFAF1' , background = '#228B22' , font =  ('times', 20, 'bold'))
											finalReportLabel.pack()
											finalReportText = Text(root , height = 22 , width = 65)
											finalReportText.insert(INSERT , finalReport)
											finalReportText.pack()
										def eleventhWindow(): #fifth meal 
											def twelfthWindow():
												def finalReportAfterFifth():
													fifthMealTitelLabel.pack_forget()
													specialProtienForFifthMealLabel.pack_forget()
													specialCarbForFifthMealLabel.pack_forget()
													specialFatForFifthMealLabel.pack_forget()
													specialProtienForFifthMealEntry.pack_forget()
													specialCarbForFifthMealEntry.pack_forget()
													specialFatForFifthMealEntry.pack_forget()
													fifthMealLabel.pack_forget()
													getTheFinalReportAfterFifthMealButton.pack_forget()

													finalReport = "breakfast \n"
													finalReport = finalReport + breakfast + "\n \n"
													finalReport = finalReport + "second meal" + "\n"
													finalReport = finalReport + secondMeal + "\n\n"
													finalReport = finalReport + "third meal" + "\n"
													finalReport = finalReport + thirdMeal + "\n\n"
													finalReport = finalReport + "fourth meal" + "\n"
													finalReport = finalReport + fourthMeal + "\n\n"
													finalReport = finalReport + "fifth meal" + "\n"
													finalReport = finalReport + fifthMeal + "\n\n"

													root.geometry("850x650")
													finalReportLabel = Label(root , text = "FINAL REPORT")
													finalReportLabel.config(foreground = '#FFFAF1' , background = '#228B22' , font =  ('times', 20, 'bold'))
													finalReportLabel.pack()
													finalReportText = Text(root , height = 35 , width = 65)
													finalReportText.insert(INSERT , finalReport)
													finalReportText.pack()


												makeFifthMealButton.pack_forget()
												fifthMeal = translateTheFoodCode(makeMeal(protienCaloriesInNormalMeals , carbCaloriesInNormalMeals , fatCaloriesInNormalMeals , 5 , specialProtienForFifthMealEntry.get() , specialCarbForFifthMealEntry.get() , specialFatForFifthMealEntry.get()))
												fifthMealLabel = Label(root , text = fifthMeal)
												fifthMealLabel.config(foreground = '#FFFAF1' , background = '#228B22' , font =  ('times', 20, 'bold'))
												fifthMealLabel.pack()
												getTheFinalReportAfterFifthMealButton = Button(root , text = "get final report"  ,  background = '#FFFAF1' , foreground='#228B22', width = 20 , command = finalReportAfterFifth)
												getTheFinalReportAfterFifthMealButton.pack()




											fourthMealTitelLabel.pack_forget()
											specialProtienForFourthMealLabel.pack_forget()
											specialCarbForFourthMealLabel.pack_forget()
											specialFatForFourthMealLabel.pack_forget()
											specialProtienForFourthMealEntry.pack_forget()
											specialCarbForFourthMealEntry.pack_forget()
											specialFatForFourthMealEntry.pack_forget()
											fourthMealLabel.pack_forget()
											afterFourthMealButton.pack_forget()

											fifthMealTitelLabel = Label(root , text="Meal 5")
											fifthMealTitelLabel.config(foreground = '#FFFAF1' , background = '#228B22' , font =  ('times', 20, 'bold'))
											fifthMealTitelLabel.pack()	

											specialProtienForFifthMealLabel = Label(root , text="special protien source you want for the fourth meal")
											specialProtienForFifthMealLabel.config(foreground = '#FFFAF1' , background = '#228B22' , font =  ('times', 20, 'bold'))
											specialProtienForFifthMealLabel.pack()	
											specialProtienForFifthMealEntry = Entry(root, width = 35 )
											specialProtienForFifthMealEntry.configure(background = '#FFFAF1' , foreground = '#228B22')
											specialProtienForFifthMealEntry.pack()

											specialCarbForFifthMealLabel = Label(root , text="special carb source you want for the fourth meal")
											specialCarbForFifthMealLabel.config(foreground = '#FFFAF1' , background = '#228B22' , font =  ('times', 20, 'bold'))
											specialCarbForFifthMealLabel.pack()	
											specialCarbForFifthMealEntry = Entry(root, width = 35 )
											specialCarbForFifthMealEntry.configure(background = '#FFFAF1' , foreground = '#228B22')
											specialCarbForFifthMealEntry.pack()

											specialFatForFifthMealLabel = Label(root , text="special fat source you want for the fourth meal")
											specialFatForFifthMealLabel.config(foreground = '#FFFAF1' , background = '#228B22' , font =  ('times', 20, 'bold'))
											specialFatForFifthMealLabel.pack()	
											specialFatForFifthMealEntry = Entry(root, width = 35 )
											specialFatForFifthMealEntry.configure(background = '#FFFAF1' , foreground = '#228B22')
											specialFatForFifthMealEntry.pack()

											makeFifthMealButton = Button(root , text = "submit"  ,  background = '#FFFAF1' , foreground='#228B22', width = 20, command = twelfthWindow)
											makeFifthMealButton.pack()


										makeFourthMealButton.pack_forget()
										fourthMeal = translateTheFoodCode(makeMeal(protienCaloriesInNormalMeals , carbCaloriesInNormalMeals , fatCaloriesInNormalMeals , 4 , specialProtienForFourthMealEntry.get() , specialCarbForFourthMealEntry.get() , specialFatForFourthMealEntry.get()))
										fourthMealLabel = Label(root , text = fourthMeal)
										fourthMealLabel.config(foreground = '#FFFAF1' , background = '#228B22' , font =  ('times', 20, 'bold'))
										fourthMealLabel.pack()
										if numberOfMeals > 4:	
											afterFourthMealButton = Button(root , text = "next"  ,  background = '#FFFAF1' , foreground='#228B22', width = 20  , command = eleventhWindow)
											afterFourthMealButton.pack()
										else:
											getTheFinalReportAfterFourthMealButton = Button(root , text = "get final report"  ,  background = '#FFFAF1' , foreground='#228B22', width = 20 , command = finalReportAfterFourth)
											getTheFinalReportAfterFourthMealButton.pack()

									 

									thirdMealTitelLabel.pack_forget()
									specialProtienForThirdMealLabel.pack_forget()
									specialCarbForThirdMealLabel.pack_forget()
									specialFatForThirdMealLabel.pack_forget()
									specialProtienForThirdMealEntry.pack_forget()
									specialCarbForThirdMealEntry.pack_forget()
									specialFatForThirdMealEntry.pack_forget()
									thirdMealLabel.pack_forget()
									afterThirdMealButton.pack_forget()

									fourthMealTitelLabel = Label(root , text="Meal 4")
									fourthMealTitelLabel.config(foreground = '#FFFAF1' , background = '#228B22' , font =  ('times', 20, 'bold'))
									fourthMealTitelLabel.pack()	

									specialProtienForFourthMealLabel = Label(root , text="special protien source you want for the fourth meal")
									specialProtienForFourthMealLabel.config(foreground = '#FFFAF1' , background = '#228B22' , font =  ('times', 20, 'bold'))
									specialProtienForFourthMealLabel.pack()	
									specialProtienForFourthMealEntry = Entry(root, width = 35 )
									specialProtienForFourthMealEntry.configure(background = '#FFFAF1' , foreground = '#228B22')
									specialProtienForFourthMealEntry.pack()

									specialCarbForFourthMealLabel = Label(root , text="special carb source you want for the fourth meal")
									specialCarbForFourthMealLabel.config(foreground = '#FFFAF1' , background = '#228B22' , font =  ('times', 20, 'bold'))
									specialCarbForFourthMealLabel.pack()	
									specialCarbForFourthMealEntry = Entry(root, width = 35 )
									specialCarbForFourthMealEntry.configure(background = '#FFFAF1' , foreground = '#228B22')
									specialCarbForFourthMealEntry.pack()

									specialFatForFourthMealLabel = Label(root , text="special fat source you want for the fourth meal")
									specialFatForFourthMealLabel.config(foreground = '#FFFAF1' , background = '#228B22' , font =  ('times', 20, 'bold'))
									specialFatForFourthMealLabel.pack()	
									specialFatForFourthMealEntry = Entry(root, width = 35 )
									specialFatForFourthMealEntry.configure(background = '#FFFAF1' , foreground = '#228B22')
									specialFatForFourthMealEntry.pack()

									makeFourthMealButton = Button(root , text = "submit"  ,  background = '#FFFAF1' , foreground='#228B22', width = 20, command = tenthWindow)
									makeFourthMealButton.pack()






								makeThirdMealButton.pack_forget()
								thirdMeal = translateTheFoodCode(makeMeal(protienCaloriesInNormalMeals , carbCaloriesInNormalMeals , fatCaloriesInNormalMeals , 3 , specialProtienForThirdMealEntry.get() , specialCarbForThirdMealEntry.get() , specialFatForThirdMealEntry.get()))
								thirdMealLabel = Label(root , text = thirdMeal)
								thirdMealLabel.config(foreground = '#FFFAF1' , background = '#228B22' , font =  ('times', 20, 'bold'))
								thirdMealLabel.pack()
								if numberOfMeals > 3:	
									afterThirdMealButton = Button(root , text = "next"  ,  background = '#FFFAF1' , foreground='#228B22', width = 20 , command = ninthWindow)
									afterThirdMealButton.pack()
								else:
									getTheFinalReportAfterThirdMealButton = Button(root , text = "get final report"  ,  background = '#FFFAF1' , foreground='#228B22', width = 20 , command = finalReportAfterThird)
									getTheFinalReportAfterThirdMealButton.pack()
										



							secondMealTitelLabel.pack_forget()
							specialProtienForSecondMealLabel.pack_forget()
							specialFatForSecondMealLabel.pack_forget()
							specialCarbForSecondMealLabel.pack_forget()
							specialProtienForSecondMealEntry.pack_forget()
							specialCarbForSecondMealEntry.pack_forget()
							specialFatForSecondMealEntry.pack_forget()
							secondMealLabel.pack_forget()
							afterSecondMealButton.pack_forget()

							thirdMealTitelLabel = Label(root , text="Meal 3")
							thirdMealTitelLabel.config(foreground = '#FFFAF1' , background = '#228B22' , font =  ('times', 20, 'bold'))
							thirdMealTitelLabel.pack()	

							specialProtienForThirdMealLabel = Label(root , text="special protien source you want for the third meal")
							specialProtienForThirdMealLabel.config(foreground = '#FFFAF1' , background = '#228B22' , font =  ('times', 20, 'bold'))
							specialProtienForThirdMealLabel.pack()	
							specialProtienForThirdMealEntry = Entry(root, width = 35 )
							specialProtienForThirdMealEntry.configure(background = '#FFFAF1' , foreground = '#228B22')
							specialProtienForThirdMealEntry.pack()

							specialCarbForThirdMealLabel = Label(root , text="special carb source you want for the third meal")
							specialCarbForThirdMealLabel.config(foreground = '#FFFAF1' , background = '#228B22' , font =  ('times', 20, 'bold'))
							specialCarbForThirdMealLabel.pack()	
							specialCarbForThirdMealEntry = Entry(root, width = 35 )
							specialCarbForThirdMealEntry.configure(background = '#FFFAF1' , foreground = '#228B22')
							specialCarbForThirdMealEntry.pack()

							specialFatForThirdMealLabel = Label(root , text="special fat source you want for the third meal")
							specialFatForThirdMealLabel.config(foreground = '#FFFAF1' , background = '#228B22' , font =  ('times', 20, 'bold'))
							specialFatForThirdMealLabel.pack()	
							specialFatForThirdMealEntry = Entry(root, width = 35 )
							specialFatForThirdMealEntry.configure(background = '#FFFAF1' , foreground = '#228B22')
							specialFatForThirdMealEntry.pack()

							makeThirdMealButton = Button(root , text = "submit"  ,  background = '#FFFAF1' , foreground='#228B22', width = 20, command = eighthWindow)
							makeThirdMealButton.pack()






						makeSecondMealButton.pack_forget()
						secondMeal = translateTheFoodCode(makeMeal(protienCaloriesInNormalMeals , carbCaloriesInNormalMeals , fatCaloriesInNormalMeals , 2 , specialProtienForSecondMealEntry.get() , specialCarbForSecondMealEntry.get() , specialFatForSecondMealEntry.get()))
						secondMealLabel = Label(root , text = secondMeal)
						secondMealLabel.config(foreground = '#FFFAF1' , background = '#228B22' , font =  ('times', 20, 'bold'))
						secondMealLabel.pack()	
						afterSecondMealButton = Button(root , text = "next"  ,  background = '#FFFAF1' , foreground='#228B22', width = 20 , command = seventhWindow)
						afterSecondMealButton.pack()


					specialProtienForBreakfastLabel.pack_forget()
					specialCarbForBreakfastLabel.pack_forget()
					specialFatForBreakfastLabel.pack_forget()
					specialProtienForBreakfastEntry.pack_forget()
					specialCarbForBreakfastEntry.pack_forget()
					specialFatForBreakfastEntry.pack_forget()
					breakfastLabel.pack_forget()
					afterBreakfastNextButton.pack_forget()

					secondMealTitelLabel = Label(root , text="Meal 2")
					secondMealTitelLabel.config(foreground = '#FFFAF1' , background = '#228B22' , font =  ('times', 20, 'bold'))
					secondMealTitelLabel.pack()	

					specialProtienForSecondMealLabel = Label(root , text="special protien source you want for the second meal")
					specialProtienForSecondMealLabel.config(foreground = '#FFFAF1' , background = '#228B22' , font =  ('times', 20, 'bold'))
					specialProtienForSecondMealLabel.pack()	
					specialProtienForSecondMealEntry = Entry(root, width = 35 )
					specialProtienForSecondMealEntry.configure(background = '#FFFAF1' , foreground = '#228B22')
					specialProtienForSecondMealEntry.pack()

					specialCarbForSecondMealLabel = Label(root , text="special carb source you want for the second meal")
					specialCarbForSecondMealLabel.config(foreground = '#FFFAF1' , background = '#228B22' , font =  ('times', 20, 'bold'))
					specialCarbForSecondMealLabel.pack()	
					specialCarbForSecondMealEntry = Entry(root, width = 35 )
					specialCarbForSecondMealEntry.configure(background = '#FFFAF1' , foreground = '#228B22')
					specialCarbForSecondMealEntry.pack()

					specialFatForSecondMealLabel = Label(root , text="special fat source you want for the second meal")
					specialFatForSecondMealLabel.config(foreground = '#FFFAF1' , background = '#228B22' , font =  ('times', 20, 'bold'))
					specialFatForSecondMealLabel.pack()	
					specialFatForSecondMealEntry = Entry(root, width = 35 )
					specialFatForSecondMealEntry.configure(background = '#FFFAF1' , foreground = '#228B22')
					specialFatForSecondMealEntry.pack()

					makeSecondMealButton = Button(root , text = "submit"  ,  background = '#FFFAF1' , foreground='#228B22', width = 20, command = sixthWindow)
					makeSecondMealButton.pack()








				specialBreaksfastProtien = specialProtienForBreakfastEntry.get()
				specialBreaksfastCarb = specialCarbForBreakfastEntry.get()
				specialBreaksfastFat = specialFatForBreakfastEntry.get()
				breakfast = translateTheFoodCode(makeBreakfast(protienCaloriesInBreakfast , carbCaloriesInBreakfast , fatCaloriesInBreakfast ,specialBreaksfastProtien , specialBreaksfastCarb , specialBreaksfastFat ))
				
				makeBreakfastButton.pack_forget()

				breakfastLabel = Label(root , text= breakfast)
				breakfastLabel.config(foreground = '#FFFAF1' , background = '#228B22' , font =  ('times', 20, 'bold'))
				breakfastLabel.pack()

				afterBreakfastNextButton = Button(root , text = "next"  ,  background = '#FFFAF1' , foreground='#228B22', width = 20 , command = fifthWindow)
				afterBreakfastNextButton.pack()




			x = avoidFoodEntry.get()
			i = 0
			out = ''
			while i < len(x):
				if(x[i] == ','):
					avoidInDiet.insert(0 , out)
					out = ''
				elif(i == len(x) -1):
					out = out+x[i]
					avoidInDiet.insert(0 , out)
				else:
					out = out+x[i]		

				i = i+1
			print(avoidInDiet)
			avoidFoodLabel.pack_forget()
			avoidFoodEntry.pack_forget()
			avoidFoodErklaerungLabel.pack_forget()
			avoidFoodErklaerungLabel1.pack_forget()
			ayMenteLabel.pack_forget()
			submitAvoidFoodButton.pack_forget()
			
			specialProtienForBreakfastLabel = Label(root , text="special protien source you want for the breakfast")
			specialProtienForBreakfastLabel.config(foreground = '#FFFAF1' , background = '#228B22' , font =  ('times', 20, 'bold'))
			specialProtienForBreakfastLabel.pack()	
			specialProtienForBreakfastEntry = Entry(root, width = 35 )
			specialProtienForBreakfastEntry.configure(background = '#FFFAF1' , foreground = '#228B22')
			specialProtienForBreakfastEntry.pack()

			specialCarbForBreakfastLabel = Label(root , text="special carb source you want for the breakfast")
			specialCarbForBreakfastLabel.config(foreground = '#FFFAF1' , background = '#228B22' , font =  ('times', 20, 'bold'))
			specialCarbForBreakfastLabel.pack()	
			specialCarbForBreakfastEntry = Entry(root, width = 35 )
			specialCarbForBreakfastEntry.configure(background = '#FFFAF1' , foreground = '#228B22')
			specialCarbForBreakfastEntry.pack()

			specialFatForBreakfastLabel = Label(root , text="special fat source you want for the breakfast")
			specialFatForBreakfastLabel.config(foreground = '#FFFAF1' , background = '#228B22' , font =  ('times', 20, 'bold'))
			specialFatForBreakfastLabel.pack()	
			specialFatForBreakfastEntry = Entry(root, width = 35 )
			specialFatForBreakfastEntry.configure(background = '#FFFAF1' , foreground = '#228B22')
			specialFatForBreakfastEntry.pack()

			makeBreakfastButton = Button(root , text = "submit"  ,  background = '#FFFAF1' , foreground='#228B22', width = 20, command = fourthWindow)
			makeBreakfastButton.pack()








	
		weightLabel.pack_forget()
		weightEntry.pack_forget()
		heightLabel.pack_forget()
		heightEntry.pack_forget()
		ageLabel.pack_forget()
		ageEntry.pack_forget()
		genderEntry.pack_forget()
		genderLabel.pack_forget()
		activityRateLabel.pack_forget()
		activityRateEntry.pack_forget()
		targetEntry.pack_forget()
		targetLabel.pack_forget()
		fristNextButton.pack_forget()
		numberOfMealsAndSnackLabel.pack_forget()
		

		print('please enter the food that you do not want to have it in your plan')
		print('when you are finished enter exit')
		print('also if all food is okay for you enter exit')
		avoidFoodLabel = Label(root , text="enter here the food you want to avoid in the whole plan")
		avoidFoodLabel.config(foreground = '#FFFAF1' , background = '#228B22' , font =  ('times', 20, 'bold'))
		avoidFoodLabel.pack()
		avoidFoodErklaerungLabel = Label(root , text= "enter them seperated by commas and press submit")
		avoidFoodErklaerungLabel.config(foreground = '#FFFAF1' , background = '#228B22' , font =  ('times', 20, 'bold'))
		avoidFoodErklaerungLabel.pack()
		avoidFoodErklaerungLabel1 = Label(root , text= "e.g. eggs,avocado,cashew")
		avoidFoodErklaerungLabel1.config(foreground = '#FFFAF1' , background = '#228B22' , font =  ('times', 20, 'bold'))
		avoidFoodErklaerungLabel1.pack()
		avoidFoodEntry =Entry(root, width = 45)
		avoidFoodEntry.configure(background = '#FFFAF1' , foreground = '#228B22')
		avoidFoodEntry.pack()
		ayMenteLabel = Label(root , text="")
		ayMenteLabel.config(foreground = '#FFFAF1' , background = '#228B22' , font =  ('times', 20, 'bold'))
		ayMenteLabel.pack()
		submitAvoidFoodButton = Button(root , text = "submit"  ,  background = '#FFFAF1' , foreground='#228B22', width = 20, command = thirdWindow)
		submitAvoidFoodButton.pack()



		




	

	"""heightLabel = Label(root , text="height")
	heightLabel.config(foreground = '#FFFAF1' , background = '#228B22' , font =  ('times', 20, 'bold'))
	heightLabel.pack()
	heightEntry = Entry(root, width = 35)
	heightEntry.configure(background = '#FFFAF1' , foreground = '#228B22')
	heightEntry.pack()"""
	weight = ''
	height = ''
	age = ''
	gender = ''
	activityLevel = ''
	target = ''
	data = submitFirstInfo()


	i = 0
	j = 0
	try:
		while i< len(data):
			if(data[i] == '#'):
				j = j+1
			else:	
				if(j == 0):
					weight = weight + data[i]
				elif(j == 1):
					height = height + data[i]
				elif(j == 2):
					age = age + data[i]
				elif(j == 3):
					gender = gender + data[i]
				elif(j == 4):
					activityLevel = activityLevel + data[i]
				elif(j == 5):
					target = target + data[i]
			i = i+1

		weight = int(weight)
		height = int(height)
		age = int(age)

	except:
		window2 = Toplevel(root)
		window2.geometry("700x100")
		window2.configure(background='#228B22')
		errorLabel = Label(window2 , text = "there is something wrong with the entered data")
		errorLabel.config(foreground = '#FFFAF1' , background = '#228B22' , font =  ('times', 20, 'bold'))
		errorLabel.pack()	
								

	print('gender' , gender)
	if(gender[0] == 'm' or gender[0] == 'M'):
		BMR = (10*weight) + (6.25 * height) - (5*age) + 5
	else:
		BMR = (10*weight) + (6.25 * height) - (5*age) - 161
		

	if(activityLevel == 'sedentary'):
		caloriesPerDay = BMR*1.2
	elif(activityLevel == 'lightly active'):
		caloriesPerDay = BMR*1.375
	elif(activityLevel == 'moderately active'):
		caloriesPerDay = BMR*1.55
	
	elif(activityLevel == 'very active'):
		caloriesPerDay = BMR*1.725
	elif(activityLevel == 'extra active'):
		caloriesPerDay = BMR*1.9

	if(target == 'gain weight'):
		caloriesPerDay = caloriesPerDay + 500
	elif(target == 'lose weight'):
		caloriesPerDay = caloriesPerDay - 500				
	else:
		caloriesPerDay = caloriesPerDay

	if(caloriesPerDay <= 1400):
		numberOfMeals = 3
		numberOfSnacks = 1
	elif(caloriesPerDay <= 1700):
		numberOfMeals = 3
		numberOfSnacks = 2
	elif(caloriesPerDay <= 2000):
		numberOfMeals = 4		
		numberOfSnacks = 1
	elif(caloriesPerDay <= 2500):
		numberOfMeals = 5
		numberOfSnacks = 0
	else:
		numberOfMeals = 5		
		numberOfSnacks = 1
	breakfastProtienRatio = 1.5/3.5  
	breakfastCarbRatio = 1/3.5
	breakfastFatRatio = 1/3.5
	normalProtienRatio = 2/3.5
	normalCarbRatio = 1/3.5
	normalFatRatio = 0.5/3.5

	protienCaloriesInBreakfast = caloriesPerDay/numberOfMeals * breakfastProtienRatio
	carbCaloriesInBreakfast = caloriesPerDay/numberOfMeals  * breakfastCarbRatio
	fatCaloriesInBreakfast = caloriesPerDay/numberOfMeals  * breakfastFatRatio
	protienCaloriesInNormalMeals = caloriesPerDay/numberOfMeals  * normalProtienRatio
	carbCaloriesInNormalMeals = caloriesPerDay/numberOfMeals  * normalCarbRatio
	fatCaloriesInNormalMeals = caloriesPerDay/numberOfMeals  * normalFatRatio
	

	textToBeAddedToTheWindow = 'you need ' + str(numberOfMeals) + ' meals and ' + str(numberOfSnacks) + ' snack(s)' 	
	numberOfMealsAndSnackLabel = Label(root , text = textToBeAddedToTheWindow)
	numberOfMealsAndSnackLabel.config(foreground = '#FFFAF1' , background = '#228B22' , font =  ('times', 20, 'bold'))
	numberOfMealsAndSnackLabel.pack()
	fristNextButton = Button(root , text = "next"  ,  background = '#FFFAF1' , foreground='#228B22', width = 30 , command = secondWindow)
	fristNextButton.pack()
	firstInfoButton.pack_forget()







def submitFirstInfo():
	weight = weightEntry.get()
	height = heightEntry.get()
	age = ageEntry.get()
	gender = genderVariable.get()
	globgender = gender
	print(weight , gender)
	activityLevel = activityRateVariable.get()
	if(activityLevel[0] == '1'):
		activityLevel = 'sedentary'
	elif(activityLevel[0] == '2'):
		activityLevel = 'lightly active'
	elif(activityLevel[0] == '3'):
		activityLevel = 'moderately active'
	elif(activityLevel[0] == '4'):
		activityLevel = 'very active'
	elif(activityLevel[0] == '5'):
		activityLevel = 'extra active'
	target = targetVariable.get()
	return weight + '#' + height + '#' + age + '#' + gender + '#' + activityLevel + '#' + target  					


firstInfoButton = Button(root , text = 'submit' ,  background = '#FFFAF1' , foreground='#228B22', width = 30 , command = setNumberOfMeals)
firstInfoButton.pack()

avoidInDiet = []

print('please enter the food that you do not want to have it in your plan')
print('when you are finished enter exit')
print('also if all food is okay for you enter exit')

while True:
	food = input()
	if(food == 'exit'):
		break
	else:
		if(isInDatabase(fromUserToCode(food))):
			avoidInDiet.insert(0 , food)
		else:
			print('the food you entered is not in the database')
			print('please check if there is a spelling mistake')
			print('when not then try to use the plural form')	





def getSpecials():
	specialNormalProtien = []
	specialNormalCarb = []
	specialNormalFat = []



	
	print('is there a special protien source you want for the meals other than breakfast')
	print('when no the enter exit')

	while True:
		food = input()
		food = fromUserToCode(food)
		if(food == 'exit'):
			specialNormalProtien.insert(0 , '')
			break
		elif(isInDatabase(fromUserToCode(food)) and toXBelong(fromUserToCode(food)) =='P'):
			specialNormalProtien.insert(0 , fromUserToCode(food))
			break
		else:		
			print('the food you entered is not in the database or is not a protien source')
			print('please check if there is a spelling mistake')
			print('when not then try to use the plural form')

	print('is there a special carb source you want for the meals other than breakfast')
	print('when no the enter exit')

	while True:
		food = input()
		food = fromUserToCode(food)
		if(food == 'exit'):
			specialNormalCarb.insert(0 , '')
			break
		elif(isInDatabase(fromUserToCode(food)) and toXBelong(fromUserToCode(food)) =='C'):
			specialNormalCarb.insert(0 , fromUserToCode(food))
			break
		else:		
			print('the food you entered is not in the database or is not a Carb source')
			print('please check if there is a spelling mistake')
			print('when not then try to use the plural form')	

	print('is there a special fat source you want for the meals other than breakfast')
	print('when no the enter exit')

	while True:
		food = input()
		food = fromUserToCode(food)
		if(food == 'exit'):
			specialNormalFat.insert(0 , '')
			break
		elif(isInDatabase(fromUserToCode(food)) and toXBelong(fromUserToCode(food)) =='F'):
			specialNormalFat.insert(0 , fromUserToCode(food))
			break
		else:		
			print('the food you entered is not in the database or is not a fat source')
			print('please check if there is a spelling mistake')
			print('when not then try to use the plural form')			
	return specialNormalProtien[0] + '#' + specialNormalCarb[0] + '#' + specialNormalFat[0]				
	







root.mainloop()