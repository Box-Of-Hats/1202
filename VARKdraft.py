
#print the question
print ("What is your preferred revision method?")

#save the options as variables
var1 = '1. Listening to audio/lectures (Audio)'
var2 = '2. Watching visual footage online (Visual)'
var3 = '3.  Taking/reading notes (Read/Write)'
var4 = '4. Practicing work by going over examples (Kinaesthetic)'

#display the options on screen
print var1 +"\n"+ var2 +"\n"+ var3 +"\n"+ var4

#Take user's input as option number and saving it in option1
option1=raw_input("Enter your choice (only one)-1, 2, 3 or 4 : ")


#check which option has user selected and assign answer1 value accordingly
if option1=='1':
    answer1=var1
elif option1=='2':
    answer1=var2
elif option1=='3':
    answer1=var3
elif option1=='4':
    answer1=var4
else :
    answer1="Sorry! The input is incorrect"
    

print "User's preferred revision method is "+answer1
