

def the_number_of_student():
    while True:
        try:
            count = int(input("Enter number of students: "))
            if count > 0:
                   return count
            print("Please enter a positive integer.")
        except ValueError:
            print("Invalid input. Please enter a positive integer.")


students = []   
def the_information_student(count):
     print(f"Enter the information of {count} students:")
     for i in range(count):
            print(f"Student {i + 1}:")
            name = input(f"Enter the name of student: ").strip()
            age = int(input(f"Enter the age of student: "))

            students.append({
                "name": name,
                "age": age, 
            })

the_information_student(the_number_of_student())

  

import numpy as np
def calculate_gpa(count):
     print(f"Calculating GPA for {count} students:")
     for i in range(count):
            student = students[i]
            print(f"Student {i + 1}: {student['name']}")
            grades = input("Enter grades: ")
            credits = input("Enter credits: ")

            grade_array = np.array([float(x) for x in grades.split(",")])
            credit_array = np.array([float(x) for x in credits.split(",")])

            gpa = np.average(grade_array, weights=credit_array)
            print(f"GPA for {student['name']} is: {round(gpa, 2)}\n")

calculate_gpa(the_number_of_student())


