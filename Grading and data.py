students = {}
new_student = 0

def action_choice():
  while True:
    answer = str(input("Would you like to add marks or view the class marks? add/view/exit \n")).lower()
  
    if  answer == "view":
      print (students) 
      exit()

    elif answer == "add": 
      student = str(input("Which student would you like to add to?"))
      return student

    elif answer == "exit":
      exit()

    else:
      print ("what you say?")


def append_student():
  student = action_choice()
  mark = input("what mark did %s get?\n" % (student))
  students.update({student:mark})

append_student()
print (students)