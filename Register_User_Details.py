"""[- Register user details
	{input:
		-student number(int)
		-course(string)
		-year of study(int)
		
	output:
		-save to a temporary list(string)
		}
"""

def Register_User_Details(studentNumber,course,yearOfStudy):
	currentUser = (str(studentNumber) + "//" + str(course) + "//" + str(yearOfStudy))
	return(currentUser)

n = Register_User_Details(1422431,"Computer Science",1)

print(n)





