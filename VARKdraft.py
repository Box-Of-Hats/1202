def main():
	print("\n")
	questions = [("You have a bug in your code but don't know how to fix it - what do you do?",
		"A. Ask your lecturer to explain the bug to you",
		"B. You watch a video of somebody showing how the bug works and how it can be fixed",
		"C. Keep changing your code until the bug disappears",
		"D. Read about bugs in a programming book"),

	("What is your most effective revision method?",
		"A. Listening to audio/lectures",
	 	"B. Watching visual footage online",
	 	"C. Taking/reading notes",
	 	"D. Practicing work by going over examples",
		),

	 ("You want to build your own computer but don't know where to start. What do you do?",
	 	"A. Read about different computer components online",
	 	"B. Take apart a different computer to try and understand how the components fit together",
	 	"C. Listen to a podcast about computer building",
	 	"D. Watch a video of somebody building a computer",
	 	),
	 ("Question 4",
	 	"A. ",
	 	"B. ",
	 	"C. ",
	 	"D. ",
	 	),
	 ("Question 5",
	 	"A. ",
	 	"B. ",
	 	"C. ",
	 	"D. ",
	 )]


	answers = []

	for quest in questions:
		print(quest[0] + "\n")
		print(quest[1] + "\n" + quest[2] + "\n" + quest[3] + "\n" + quest[4])
		a = raw_input("Answer: ")
		print("Your answer is = " + a.upper() + "\n")
		answers.append(a)
		
	print(answers)

if __name__ == '__main__':
	main()
