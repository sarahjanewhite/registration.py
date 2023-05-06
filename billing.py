#
# Sarah White
# 4.16.23
# Billing module for CSC121 group project
#

# FUNCTION THAT CALCULATES THE TOTAL HOURS AND TOTAL BILL FOR SPECIFIED STUDENT.
# FIRST IT SETS THE BASELINE FOR THE HOURS AND COST TO ZERO.
# THE FUNCTION THEN GOES THROUGH EACH COURSE TO DETERMINE IF THE SPECIFIED STUDENT IS ENROLLED IN THAT COURSE AND THEN IT DETERMINES WHICH RATE TO USE BY USING THE GET METHOD FROM THE s_in_state DICTIONARY.
# THEN THE FUNCTION CALCULATES THE TOTAL NUMBER OF HOURS AND MULTIPLIES THIS NUMBER BY THE DETERMINED RATE AND ADDS THE INITIALIZED COST VARIABLE.
# FINALLY IT RETURNS THESE VALUES AS 'hours' AND 'cost'.
def calculate_hours_and_bill(id, s_in_state, course_roster, course_hours):
    hours = 0
    cost = 0

    for course, roster in course_roster.items():
        if id in roster:
            if s_in_state.get(id):
                rate = 225
            else:
                rate = 850

            if id in roster:
                hours += course_hours[course]
                course_cost = course_hours[course] * rate
                cost += course_cost

    return hours, cost


# VERY SIMPLE FUNCTION THAT USES THE RETURN VALUES FROM THE calculate_hours_and_bill FUNCTION TO DISPLAY THOSE RESULTS.
def display_hours_and_bill(hours, cost):
    print(f"Course load: {hours} credit hours")
    print(f"Enrollment cost: ${cost:.2f}")
    print()
