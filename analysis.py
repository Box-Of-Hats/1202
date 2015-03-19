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


"""
#Used to create student .DAT:
myStudent = Student('0000001', '1', 'Computer Science', ['a', 'b', 'c', 'd'], ['d', 'd', 'c', 'c'])
dataHandler.add_data(myStudent)

myStudent = Student('0000002', '1', 'Business Studies', ['d', 'b', 'd', 'd'], ['a', 'b', 'a', 'b'])
dataHandler.add_data(myStudent)

myStudent = Student('0000003', '2', 'Business Studies', ['d', 'c', 'a', 'a'], ['d', 'd', 'd', 'd'])
dataHandler.add_data(myStudent)
#######################################

"""


def analyseVARK():
	audio = 0
	visual = 0
	read = 0
	kinaesthetic = 0
	for answer in dataHandler.retrieveROW(3):
		print(answer)
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
	print("kinaesthetic: " + str(kinaesthetic))
		
def analyseHM():
	pragmatist = 0
	reflector = 0
	activist = 0
	theorist = 0
	for answer in dataHandler.retrieveROW(4):
		print(answer)
		if answer == "a":
			pragmatist += 1
		elif answer == "b":
			reflector += 1
		elif answer == "c":
			activist += 1
		elif answer == "d":
			theorist += 1
		else:
			print("There was an error loading answers.")
	print("Audio: " + str(pragmatist))
	print("Visual: " + str(reflector))
	print("Reading/Writing: " +str(activist))
	print("kinaesthetic: " + str(theorist))

#Testing:

analyseVARK()
analyseHM()

#dataHandler.print_data()