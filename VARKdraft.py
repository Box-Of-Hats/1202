def main():
    print("\n")
    questions = [("What is your preferred revision method?",
        "A. Listening to audio/lectures (Audio)",
        "B. Watching visual footage online (Visual)",
        "C. Taking/reading notes (Read/Write)",
        "D.  Practicing work by going over examples (Kinaesthetic)"),

    ("You have a bug in your code but don’t know how to fix it. What do you do?",
        "A. Ask your lecturer to explain the bug to you (Audio)",
        "B. Watch a video of somebody showing how the bug works and how it can be fixed (Visual)",
        "C. Read about bugs in a programming book (Read/Write)",
        "D. Keep changing your code until the bug disappears (Kinaesthetic)",
        ),

     ("You want to build your own computer but don’t know where to start. What do you do?",
        "A. Listen to a podcast about computer building (Audio)",
        "B. Watch a video of somebody building a computer (Visual)",
        "C. Read about different computer components online (Read/Write)",
        "D. Take apart a different computer to try and understand how the components fit together (Kinaesthetic)",
        ),
     ("You are in class and asked to learn a new program for your course. What do you do?",
        "A. Ask someone experienced with the program to explain it to you. (Audio)",
        "B. Look for video tutorials online to watch and understand. (Visual)",
        "C. Read about it online or in a manual. (Read/Write)",
        "D. Experiment with it and see what results you get. (Kinesthetic)",
        ),
     ("You are about to create a new program for a project. What do you do?",
        "A. Ask someone else to tell you what they would want from your program (Audio)",
        "B. Look at some similar programs that already exist (Visual)",
        "C. Write a plan of what you’re going to do first (Read/Write)",
        "D. Begin coding immediately and experiment (Kinesthetic)",
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
