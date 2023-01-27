
# Python Function: cheat_assignment_1
# Type in the number of the exercise from assignment 1 to see the solution

def cheat(exercise_number):
    solution = {
        1.1: "import numpy as np\import pandas as pd",
        1.2: "another_array = np.zeros((2, 4, 6))\print(another_array[-1, 0, 2])",
        1.3: "In Python, when using =, we only assign a reference to an object in memory\
            so both new_array and another_array are pointing to the same memory allocation\
            namely, the one created by np.zeros().\
            To make a true copy, you can use the .copy() method or np.copy().\
            it is only defined for iPython terminal execution",
        1.4: "does not work in a script, it is only defined for iPython terminal execution"
    }
    if exercise_number in solution:
        return solution[exercise_number]
    else:
        return "Invalid exercise number. Number should be between 1.1 and 1.4"


