#
# Sarah White (drop_course & add_course), Gwenole Somadjagbi (list_courses)
# 4.23.23
# Student module for CSC121 group project
#


# THIS FUNCTION PROMPTS USER TO INPUT THE COURSE THEY WANT TO ADD, AND RESPONDS ACCORDINGLY.
# IF THE COURSE DOES NOT EXIST IN course_roster, IT WILL PRINT AN ERROR MESSAGE TELLING THE USER THAT.
# IF THE STUDENT ID IS FOUND IN course_roster[course], IT WILL PRINT AN ERROR MESSAGE TELLING THE USER THAT.
# IF THE COURSE IS AT MAX CAPACITY, IT WILL PRINT AN ERROR MESSAGE TELLING THE USER THAT.
# IF THE COURSE EXISTS, THE STUDENT IS NOT ALREADY ENROLLED IN THE COURSE AND THE COURSE IS NOT AT MAX CAPACITY, THE FUNCTION WILL APPEND course_roster[course] AND ADD THE STUDENT ID.
def add_course(id, course_roster, course_max_size):
    # ADD DESCRIPTION HERE
    course = input("Enter the course you want to add: ")

    if course not in course_roster:
        print("Course not found.")
        print()
        return

    if id in course_roster[course]:
        print("You are already enrolled in that course.")
        print()
        return

    if len(course_roster[course]) == course_max_size[course]:
        print("Course already full.")
        print()
        return

    course_roster[course].append(id)
    print("Course added.")
    print()


# THIS FUNCTION PROMPTS USER TO INPUT THE COURSE THEY WANT TO DROP, AND RESPONDS ACCORDINGLY.
# IF THE COURSE IS NOT FOUND IN course_roster, IT WILL PRINT AN ERROR MESSAGE.
# IF THE SPECIFIED STUDENT ID IS NOT FOUND IN course_roster[course], IT WILL PRINT AN ERROR MESSAGE.
# IF THE SPECIFIED STUDENT ID IS FOUND IN course_roster[course], IT WILL REMOVE THE STUDENT FROM THE COURSE AND PRINT THAT THE DROP WAS SUCCESSFUL.
def drop_course(id, course_roster):
    course = input("Enter course you want to drop: ")
    if course not in course_roster:
        print("Course not found.")
        print()
        return
    elif id not in course_roster[course]:
        print("You are not enrolled in that course.")
        print()
        return
    else:
        course_roster[course].remove(id)
        print("Course dropped.")
        print()


# THIS FUNCTION WILL LIST ALL COURSES THE SPECIFIED STUDENT IS ENROLLED IN AND SHOW THE TOTAL NUMBER OF COURSES.
# FIRST IT INITIALIZES THE TOTAL NUMBER OF COURSES TO '0' FOR A COUNTER.
# THE FUNCTION WILL THEN LOOP THROUGH EACH COURSE, CHECK IF THE SPECIFIED STUDENT IS ENROLLED.
# IF THEY ARE ENROLLED, THE NAME OF THE COURSE IS PRINTED AND '1' IS ADDED TO THE COUNTER.
# AFTER THE LOOP IS FINISHED, THE TOTAL NUMBER OF COURSES THAT THE STUDENT IS CURRENTLY ENROLLED IN IS PRINTED.
def list_courses(id, course_roster):
    num_courses = 0
    print("Courses registered: ")
    for course, roster in course_roster.items():
        if id in roster:
            print(f"{course}")
            num_courses += 1
    print(f"Total number: {num_courses}")
    print()
