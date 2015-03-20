from datahandler import *
"""
Honey and Mumford:
A = pragmatist,  B = Reflector,  C = Activist,  D = Theorist

VARK:
A = Audio, B = Visual, C = Read/Write D = Kinaesthetic


student_id,year of study, course, VARK, HM

"""
#Used to initialise dataHandler:

dataHandler = DataHandler()


#Used to create student .DAT:
myStudent = Student('0000001', '1', 'Computer Science', ['a', 'a', 'a', 'a'], ['a', 'b', 'c', 'd'])
dataHandler.add_data(myStudent)

myStudent = Student('0000002', '1', 'Business Studies', ['a', 'b', 'b', 'b'], ['a', 'd', 'c', 'd'])
dataHandler.add_data(myStudent)

myStudent = Student('0000003', '2', 'Business Studies', ['a', 'b', 'c', 'd'], ['a', 'b', 'c', 'd'])
dataHandler.add_data(myStudent)
#######################################



#Finds the VARK scores for an idividual student.
#Parameter should be a tuple of students details such as ('ID', 'YEAR', 'COURSE', [VARK,], [HM]):
def analyseVARK(student):
	audio = 0
	visual = 0
	read = 0
	kinaesthetic = 0
	print("Student ID: " + student[0])
	print("VARK scores:")
	answerlist = student[3]
	for answer in answerlist:
		#print(answer)
		if answer == "a":
			audio += 1
		elif answer == "b":
			visual += 1
		elif answer == "c":
			read += 1
		elif answer == "d":
			kinaesthetic += 1
		else:
			print("There was an error loading answers.")
	print("Audio: " + str(audio))
	print("Visual: " + str(visual))
	print("Reading/Writing: " +str(read))
	print("kinaesthetic: " + str(kinaesthetic) + "\n")


#Finds the Honey&Mumford scores for an idividual student. 
#Parameter should be a tuple of students details such as ('ID', 'YEAR', 'COURSE', [VARK,], [HM]):
def analyseHM(student):
	pragmatist = 0
	reflector = 0
	activist = 0
	theorist = 0
	print("Student ID: " + student[0])
	print("Honey and Mumford scores:")
	#Making the answerlist = HM scores:
	answerlist = student[3]
	for answer in answerlist:
		if answer == "a":
			pragmatist += 1
		elif answer == "b":
			reflector += 1
		elif answer == "c":
			activist += 1
		elif answer == "d":
			theorist += 1
		else:
			print("Error with answer: " + str(answer))
	print("Audio: " + str(pragmatist))
	print("Visual: " + str(reflector))
	print("Reading/Writing: " +str(activist))
	print("kinaesthetic: " + str(theorist) + "\n")


def analyseAllHM(DataFileName):
	inFile = pickle.load(open(DataFileName,"rb"))
	#Initialise all totals as 0:
	total_pragmatist = 0
	total_reflector = 0
	total_activist = 0
	total_theorist = 0
	#Iterate through the different students:
	for student in inFile:
		#Set answerlist to equal the list of the students answers for H&M questionnaire:
		answerlist = student[4]
		#Print list for debugging:
		print(answerlist)
		#Iterate through answers in the answerlist:
		for answer in answerlist:
			print(answer)
			if answer == "a":
				total_pragmatist += 1
			elif answer == "b":
				total_reflector += 1
			elif answer == "c":
				total_activist += 1
			elif answer == "d":
				total_theorist += 1
			else:
				print("Error with answer: " + str(answer))
			print("Total pragmatist: " + str(total_pragmatist))
			print("Total reflector: " + str(total_reflector))
			print("Total activist: " + str(total_activist))
			print("Total theorist: " + str(total_activist))
					



#Testing:
"""
#Loads data from .dat file and then analyses all results within:
a = pickle.load(open("data.dat","rb"))
for student in a:
	analyseHM(student)
	analyseVARK(student)
"""
analyseAllHM("data.dat")
#dataHandler.retrieveROW(4)

#-print(dataHandler.print_data())