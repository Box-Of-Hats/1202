import pickle
import os

"""
HOW TO USE THIS CLASS:
When a DataHandler is created it checks if a data.dat file exists, and
if it does it loads the student data currently stored in it.

Use the add_student function to add a new student to the file.
The 'students' array holds all of the student data, so to access student
data you would simply type something like print(students[0])

Below is a template for the student class used for testing.

class Student:
    def __init__(self,
                 student_id,
                 year_of_study,
                 course,
                 vark_answers,
                 hm_answers):
        self.student_id = student_id
        self.year_of_study = year_of_study
        self.course = course
        self.vark_answers = vark_answers
        self.hm_answers = hm_answers
"""


class DataHandler:
    def __init__(self):
        self.students = []
        if os.path.isfile('data.dat'):
            self.retrieve()

    def add_student(self, student):
        self.students.append(student)
        self.store()

    def print_students(self):
        for student in self.students:
            print("Student ID:", student.student_id)
            print("Year of study:", student.year_of_study)
            print("Course:", student.course)
            print("VARK answers:", student.vark_answers)
            print("Honey & Mumford answers:", student.hm_answers)

    def store(self):
        dataFile = open('data.dat', 'wb')
        pickle.dump(self.students, dataFile)
        dataFile.close()

    def retrieve(self):
        dataFile = open('data.dat', 'rb')
        self.students = pickle.load(dataFile)
        dataFile.close()


def main():
    pass

if __name__ == '__main__':
    main()
