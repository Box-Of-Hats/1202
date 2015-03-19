def main():
	print("\n")
	questions = [("When learning about a new programming concept, I: ",
		"A. Like to see how it could be applied to a real life project.",
		"B. Think about previous programming work I have done and how the new concept would be used to improve it. ",
		"C. Experiment with it by using it in my own projects to help me learn about how it works and why it could be useful.",
		"D. Theorist answer..."),
	("If I was to build my own computer, I would: ",
		"A. Want to know how people decide which components to use in the real world.",
		"B. Observe somebody else building a computer beforehand.",
		"C. Take apart a computer to analyse how each of the components work together.",
		"D. Want to know the purpose of each component and how they work.",
		),
	("If my code is not functioning as intended, I would: ",
		"A. See how people debug their code in the real world.",
		"B. Think about issues that my code has had before and check them against my new code.",
		"C. Experiment my code and try to fix the issue with trial and error.",
		"D. Look at my code and think about how each individual part works to solve the problem.",
	),
	("When overclocking computer components I: ",
		"A. Run benchmarks beforehand and then calculate the amount of overclocking room that is available before applying the overclock.",
		"B. Try to get as many opinions as possible and only overclock once I am fully satisfied.",
		"C. Overclock the components and then see how the system runs.",
		"D. Do my research by reading and then apply the overclock.",
	),
	("If I am trying to build my own portal, I supposed to: ",
		"A. You can create either a blank page or a page prepopulated with portlets from a page template.",
		"B. Allows you to keep the existing look and feel while giving your site a different flavor.",
		"C. Read alot about different databases and choose the best.",
		"D. Knowning what does the databases making differences.",
	)]

	answers = []

	for quest in questions:
		print(quest[0] + "\n")
		print(quest[1] + "\n" + quest[2] + "\n" + quest[3] + "\n" + quest[4])

		counter=False
		while not counter:
			a = input("Answer: ")
			if a.lower() in ('a','b','c','d'):
				print("Your answer is = " + a.upper() + "\n")
				answers.append(a)
				counter=True
			else:
				a='na'
				print("The option does not exist.Please Try Again")

	print(answers)

if __name__ == '__main__':
	main()
