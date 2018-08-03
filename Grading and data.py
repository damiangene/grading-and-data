import json
students = {}
new_student = 0

def action_choice():
  while True:
    answer = str(input("Would you like to add marks or view the class marks? add/view/exit \n")).lower()
  
    if  answer == "view":
      with open("names_marks.txt") as tmpfile:
        students = json.load(tmpfile)
      
      for name in students: 
        print (name)
        print ("Average %.2f" % (mark_average(name)))
        print(students[name])
               
      exit()

    elif answer == "add": 
      student = str(input("Which student would you like to add to?"))
      return student

    elif answer == "clear":
        students = {}

        with open('names_marks.txt', 'w') as outfile: 
            json.dump(students, outfile, indent = 2)

    elif answer == "exit":
      exit()

    else:
      print ("what you say?")


def append_student():
  name = action_choice()
  mark = input("what mark did %s get?\n" % (name))
  mark = int(mark)
  
  with open("names_marks.txt") as tmpfile:
        students = json.load(tmpfile)

        if students.get(name):
            students[name]["Marks"].append(mark)
        
        else:
            students[name] = {"Marks":[mark]}

        print (students)
        with open('names_marks.txt', 'w') as outfile: 
            json.dump(students, outfile, indent = 2)

def mark_average(name):
    with open("names_marks.txt") as tmpfile:
        students = json.load(tmpfile)

    total = sum(students[name]["Marks"])
    s_average = total / len(students[name]["Marks"])
    return s_average

append_student()
