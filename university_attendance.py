'''
In a university, your attendance determines whether you will be
allowed to attend your graduation ceremony.
You are not allowed to miss classes for four or more consecutive days.
Your graduation ceremony is on the last day of the academic year,
which is the Nth day.



Your task is to determine the following:

1. The number of ways to attend classes over N days.
2. The probability that you will miss your graduation ceremony.

Represent the solution in the string format as "Answer of (2) / Answer
of (1)", don't actually divide or reduce the fraction to decimal

Test cases:

for 5 days: 14/29
for 10 days: 372/773

'''
import itertools

def attendance_allowed(attendance, abs_limit):
    """
    Checks if an attendance pattern is allowed based on the constraint of
    not having absences for 'abs_limit' or more consecutive days.

    Parameters:
    attendance (list): A list representing attendance pattern where 0 is absent and 1 is present.
    abs_limit (int): The limit for consecutive days of absence.

    Returns:
    bool: True if the attendance pattern is allowed, False otherwise.
    """
    abs_consecutively = 0
    
    # Check each day's attendance
    for day in attendance:
        if day == 0:
            abs_consecutively += 1
            if abs_consecutively >= abs_limit:
                return False
        else:
            abs_consecutively = 0
    return True

def missing_graduation_probability(days, abs_limit):
    """
    Calculates the probability of missing the graduation ceremony by checking
    all possible attendance patterns for the given number of days and absence limit.

    Parameters:
    days (int): The total number of days.
    abs_limit (int): The limit for consecutive days of absence.

    Returns:
    str: A string representing the fraction of ways to miss the graduation ceremony over the allowed attendance patterns.
    """
    absent = 0
    present = 1
    available_options = [absent, present]

    # Generate all possible attendance combinations
    possible_attendance_combinations = [combination for combination in itertools.product(available_options, repeat=days)]
    
    # Filter out the allowed combinations based on the absence constraint
    permitted_combinations = [attendance for attendance in possible_attendance_combinations if attendance_allowed(attendance, abs_limit)]
    
    # Count the allowed combinations that end with an absence (miss graduation ceremony)
    missing_graduation_count = [attendance for attendance in permitted_combinations if attendance[-1] == 0]

    # Return the probability as a fraction string
    return f'{len(missing_graduation_count)}/{len(permitted_combinations)}'

if __name__ == '__main__':
    days =  int(input())  # Number of days 
    abs_limit = int(input())  # Absence limit 
    print(missing_graduation_probability(days, abs_limit))  # Calculate and print the probability
