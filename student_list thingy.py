student_list = []
grades_dict = {}

while True:
    user_input = input("Welcome to SAx student:grades arranger\nEnter 1 to register\nEnter 2 to enter grades\nEnter 3 to display list\nEnter 4 to exit\nKindly enter your selection: ")

    if user_input == "1":
        quantity = int(input("How many students are there? "))
        for i in range(quantity):
            student_name = input("What is the student's name? ")
            student_list.append(student_name)
        print("Students registered successfully!")

    elif user_input == "2":
        if not student_list:
            print("No students registered yet. Please register students first.")
        else:
            assignment_name = input("What is the name of the assignment? ")
            total_score = int(input("What is the maximum possible score? "))
            for student in student_list:
                student_grade = int(input(f"What is {student}'s grade for {assignment_name}? "))
                if student in grades_dict:
                    grades_dict[student].append((assignment_name, student_grade))
                else:
                    grades_dict[student] = [(assignment_name, student_grade)]
            print("Grades entered successfully!")

    elif user_input == "3":
        if not grades_dict:
            print("No grades entered yet.")
        else:
            for student, grades in grades_dict.items():
                print(f"Student: {student}")
                for assignment, grade in grades:
                    print(f"Assignment: {assignment}, Grade: {grade}")
                print()

    elif user_input == "4":
        print("Exiting the program. Goodbye!")
        break

    else:
        print("Invalid selection. Please try again.")
