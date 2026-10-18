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
