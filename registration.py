#
# Carrie Rice & Sarah White
# 4.16.23
# Registration module for CSC121 group project
#

# IMPORTS THE BILLING AND STUDENT MODULES FOR USE WITHIN THIS PROGRAM (registration.py)
import billing
import student


# FUNCTION THAT IS CALLED AFTER THE USER IS PROMPTED TO INPUT THEIR ID IN THE MAIN FUNCTION.
# THIS FUNCTION PROMPTS THE USER TO PUT IN THE MATCHING PIN.
# THE FUNCTION USES AN "IF" STATEMENT TO VALIDATE THE ID AND PIN (CHECKS TO SEE IF IT IS IN students_list)
# "True" OR "False" IS RETURNED TO THE MAIN FUNCTION.
def login(id, student_list):
    pin = input("Enter PIN: ")
    if (id, pin) in student_list:
        print("ID and PIN verified.")
        print()
        return True
    else:
        print("ID or PIN incorrect.")
        print()
        return False

# START OF THE MAIN FUNCTION
def main():
    student_list = [('1001', '111'), ('1002', '222'),
                    ('1003', '333'), ('1004', '444')]
    student_in_state = {'1001': True,
                        '1002': False,
                        '1003': True,
                        '1004': False}

    course_hours = {'CSC101': 3, 'CSC102': 4, 'CSC103': 5, 'CSC104': 3}
    course_roster = {'CSC101': ['1004', '1003'],
                     'CSC102': ['1001'],
                     'CSC103': ['1002'],
                     'CSC104': []}
    course_max_size = {'CSC101': 3, 'CSC102': 2, 'CSC103': 1, 'CSC104': 3}

    # THE PROGRAM STARTS HERE AND FUNCTIONS AS THE MAIN (INFINITE) LOOP THAT WILL NOT BREAK UNTIL THE USER CHOOSES.
    # AN INPUT OF '0' BREAKS THE LOOP AND ENDS THE PROGRAM.
    # IT PROMPTS THE USER TO ENTER THEIR ID.
    # AFTER THE ID IS INPUTTED, IT CALLS TO THE LOGIN FUNCTION IN THIS FILE.
    # THE RETURNED VALUES OF "TRUE" OR "FALSE" FROM THE "login" FUNCTION ARE TREATED AS WRITTEN.
    while True:
        id = input("Enter ID to log in or 0 to quit: ")
        if id == '0':
            quit()
        if login(id, student_list):
            # THIS IS A NESTED LOOP THAT ONLY STARTS IF THE ID AND PIN COMBO IS CORRECT.
            # AFTER VALIDATION, IT PROMPTS THE USER TO CHOOSE BETWEEN "ADD A COURSE", "DROP A COURSE", "LIST COURSES", "SHOW BILL" OR "EXIT."
            # THIS LOOP ONLY BREAKS WHEN THE USER SPECIFIES TO DO SO.
            # AN INPUT OF '0' BREAKS THE LOOP AND SENDS THE USER BACK TO THE MAIN (INFINITE) LOOP.
            while True:
                choice = int(input("Enter 1 to add course, 2 to drop course, 3 to list courses, 4 to show bill, 0 to exit: "))
                # CALLS TO add_course FUNCTION IN student.py
                if choice == 1:
                    student.add_course(id, course_roster, course_max_size)
                # CALLS TO drop_course FUNCTION IN student.py
                elif choice == 2:
                    student.drop_course(id, course_roster)
                # CALLS TO THE list_courses FUNCTION IN student.py
                elif choice == 3:
                    student.list_courses(id, course_roster)
                # THE 4TH CHOICE WAS THE MOST DIFFICULT FOR ME TO FIGURE OUT.
                # IT CALLS TO BOTH FUNCTIONS IN billing.py.
                elif choice == 4:
                    hours, cost = billing.calculate_hours_and_bill(id, student_in_state, course_roster, course_hours)
                    billing.display_hours_and_bill(hours, cost)
                # THIS CHOICE BREAKS THE LOOP AND SENDS THE USER BACK TO THE MAIN (INFINITE) LOOP.
                elif choice == 0:
                    print("Session ended.")
                    print()
                    break


main()
