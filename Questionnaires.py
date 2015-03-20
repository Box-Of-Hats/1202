from tkinter import *

class Application(Frame):
	def menu_page(self):
		Questionnaires = Button(root, text = "Start Questionnaires", command = lambda: self.frame_clearer("start", Questionnaires, ViewResults))
		ViewResults = Button(root, text = "View All Results", command= lambda: self.frame_clearer("results", Questionnaires, ViewResults))
		Questionnaires.pack({"side" : "top"})
		ViewResults.pack({"side": "top"})
		
	def start_page(self):
		yearOfStudy = 0
		courseType = ""
		label1 = Label(root, text = "Student Number")
		label1.pack()
		studentNumber = Entry(root)
		studentNumber.pack()
		label2 = Label(root, text = "Year of study?")
		label2.pack()
		radiobutton1 = Radiobutton(root, text="One", variable=yearOfStudy, value=1)
		radiobutton1.pack()
		radiobutton2 = Radiobutton(root, text="Two", variable=yearOfStudy, value=2)
		radiobutton2.pack()
		radiobutton3 = Radiobutton(root, text="Three", variable=yearOfStudy, value=3)
		radiobutton3.pack()
		label3 = Label(root, text = "Course type?")
		label3.pack()
		radiobutton4 = Radiobutton(root, text="CS", variable=courseType, value="CS", indicatoron = 0)
		radiobutton4.pack()
		radiobutton5 = Radiobutton(root, text="BIS", variable=courseType, value="BIS", indicatoron = 0)
		radiobutton5.pack()
		radiobutton6 = Radiobutton(root, text="SE", variable=courseType, value="SE", indicatoron = 0)
		radiobutton6.pack()
		submitButton = Button(root, text = "Start Questionnaires", command = lambda: self.frame_clearer("questions", label1, label2, label3, submitButton, studentNumber, radiobutton1, radiobutton2, radiobutton3, radiobutton4, radiobutton5, radiobutton6))
		submitButton.pack()
		
	def results_page(self):
		print("results")

	def questions_page(self):
		answer = ""
		label1 = Label(root, text = "......")
		label1.pack()
		radiobutton1 = Radiobutton(root, text="...", variable=answer, value="a")
		radiobutton1.pack()
		radiobutton2 = Radiobutton(root, text="...", variable=answer, value="b")
		radiobutton2.pack()
		radiobutton3 = Radiobutton(root, text="...", variable=answer, value="c")
		radiobutton3.pack()
		radiobutton4 = Radiobutton(root, text="...", variable=answer, value="d")
		radiobutton4.pack()
		submitButton = Button(root, text = "Submit Answer", command = lambda: self.frame_clearer("questions", label1, submitButton, radiobutton1, radiobutton2, radiobutton3, radiobutton4))
		submitButton.pack()


	def personal_page(self):
		print("personal")

	def frame_clearer(self, nextPage, *remover):
		for x in remover:
			x.pack_forget()
		if nextPage == "start":
			self.start_page()
		elif nextPage == "results":
			self.results_page()
		elif nextPage == "questions":
			self.questions_page()
		elif nextPage == "personal":
			self.personal_page()
		elif nextPage == "menu":
			self.menu_page()

	def __init__(self, master=None):
		Frame.__init__(self, master)
		self.pack()
		self.menu_page()

root = Tk()
app = Application(master=root)
app.mainloop()



