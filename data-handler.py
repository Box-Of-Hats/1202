import pickle
import os
"""
This is how the student class will have to be defined in another file to work
with the DataHandler.

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
        self.data_table = []
        if os.path.isfile('data.dat'):
            self.retrieve()

    def add_data(self, student):
        row = [student.student_id,
               student.year_of_study,
               student.course,
               student.vark_answers,
               student.hm_answers]

        self.data_table.append(row)
        self.store()

    def print_data(self):
        for row in self.data_table:
            print("Student ID:", row[0])
            print("Year of study:", row[1])
            print("Course:", row[2])
            print("VARK answers:", row[3])
            print("Honey & Mumford answers:", row[4])

    def store(self):
        dataFile = open('data.dat', 'wb')
        pickle.dump(self.data_table, dataFile)
        dataFile.close()

    def retrieve(self):
        dataFile = open('data.dat', 'rb')
        self.data_table = pickle.load(dataFile)
        dataFile.close()


def main():
    pass

if __name__ == '__main__':
    main()
