'''
Problem Statement  
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

Objective
    To determine the probability of missing a graduation ceremony given the number of days (N) 
    and the constraint that no more than a certain number 
    of consecutive absences (abs_limit) are allowed.
    
Problem Breakdown
    Total Number of Patterns: For N days, each day can be either attended (present) or missed (absent), 
        resulting in 2^N possible attendance patterns.
        
    Valid Patterns: Out of these 2^N patterns, we need to filter those that do not have abs_limit or 
        more consecutive absences.
    
    Missing Graduation: From the valid patterns, identify those that end in an absence (indicating 
        missing the graduation ceremony).
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

    Time and Space Complexity(brute force)
        Time Complexity - O(2^N * N)
        Space Complexity: O(2^N * N)
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

def missing_graduation_probability_optimised(days, abs_limit):
    """
    Calculate the number of ways a person can attend graduation and the probability of missing.

    Args:
    days (int): The number of days
    abs_limit (int): The limit for abs

    Returns:
    str: A string representing the number of ways to attend over the total possibilities
    Time and Space Complexity(brute force)
        Time Complexity - O(days*abs_limit) = O(days)
        Space Complexity: O((days+1) x abs_limit) = O(days)
    """
    # Initialize a 2D array to store the number of ways to attend on each day
    attendance_pattern = [[0]*abs_limit for _ in range(days+1)]
    
    # Base case: day 0
    attendance_pattern[0][0] = 1

    for i in range(1, days+1):
        # Calculate the number of ways to attend on day i
        attendance_pattern[i][0] = sum(attendance_pattern[i-1][:abs_limit])
        for j in range(1, abs_limit):
            attendance_pattern[i][j] = attendance_pattern[i-1][j-1]
    
    # Return the result as a string
    return str(sum(attendance_pattern[days][1:])) + '/' + str(sum(attendance_pattern[days]))


if __name__ == '__main__':
    days =  int(input())  # Number of days 
    abs_limit = int(input())  # Absence limit 
    print(missing_graduation_probability(days, abs_limit))  # Calculate and print the probability
    print(missing_graduation_probability_optimised(days, abs_limit))  # Calculate and print the probability
