import numpy as np
from itertools import product
from math import factorial
from typing import Union, Callable, Tuple, List, Set
import re
# import csv_preprocessor
import csv


def get_matching(data):
    """
        First pass filtering. Used as a callable by get_matching_final.
        Removes nan instances from the data set the hands it off to
        get_matching_final for further processing.
    """
    removed_nan = []
    w_solution = []
    wo_solution = []
    the_solutions = []
    for lst in data:
        for stmnt in lst:
            solution = re.findall(r'=([^,]*),', stmnt)[0]
            after_hyphen = stmnt.split("-")[1][0]
            if (solution != " nan" and int(solution) == int(after_hyphen)):
                w_solution.append(lst)
            if (solution != " nan" and int(solution) != int(after_hyphen)):
                wo_solution.append(lst)

    joined_list = [*w_solution, *wo_solution]
    return joined_list
    # w_combined =  w_solution + wo_solution #used for second pass

def get_matching_final(data):
        matching_middle = []
        non_matching_middle = []

        matching_final = []
        nonmatching_final = []
        # keys = []

        for lst in data:
            for stmnt in lst:
                solution = re.findall(r'=([^,]*),', stmnt)[0]
                after_hyphen = stmnt.split("-")[1][0]
                #key
                key = stmnt.split(",")[0]
                # keys.append(key)
                #/key
                if (int(solution) == int(after_hyphen)):
                    matching_middle.append(lst)
                elif (int(solution) != int(after_hyphen)):
                    non_matching_middle.append(lst)

        wd = {s[0].split(',')[0]: s[0] for s in matching_middle}
        wod = {s[0].split(',')[0]: s[0] for s in non_matching_middle}
        keys = sorted(set(wd.keys()).union(wod.keys()), reverse=True)
        final = [[wd[k]] if k in wd else [wod[k]] for k in keys]
        # final_list = [x for x in final]
        # final_list_unique = np.unique(final_list) 
        return final


def plus(a: int, b: int) -> int:
    return a + b


def minus(a: int, b: int) -> int:
    return a - b


def mult(a: int, b: int) -> int:
    return a * b


def div(a: int, b: int) -> Union[int, float]:
    try:
        retval = int(a / b)
    except (ValueError, ZeroDivisionError):
        retval = np.nan
    return retval


def the_factorial(a: int) -> Union[int, float]:
    try:
        return factorial(int(a))
    except ValueError:
        return np.nan
    except OverflowError:
        # return np.inf
        return np.nan


def power_to(a: int, b: int) -> Union[int, float]:
    try:
        return int(a ** b)
    except (ValueError, ZeroDivisionError):
        return np.nan


def root(a: int, b: int) -> Union[int, float]:
    try:
        return int(b ** (1 / a))
    except (TypeError, ZeroDivisionError, ValueError):
        return np.nan


def solve(values: Tuple[int, int, int], ops: List[Callable]) -> list[Tuple[str, int]]:
    # Iterate over available functions.
    combs = list()
    for f in FACTORS:
        # Get values to operate with.
        x, y, z = values
        sx, sy, sz = x, y, z
        a, b, c = f
        # Calculate the factorial for the values (if applicable).
        if a == 1:
            sx = f"{x}!"
            x = the_factorial(x)
        if b == 1:
            sy = f"{y}!"
            y = the_factorial(y)
        if c == 1:
            sz = f"{z}!"
            z = the_factorial(z)
        for ext_op in ops:  # External operation.
            for int_op in ops:  # Internal operation.
                # Create equations by grouping the first 2 elements, e.g.: ((x + y) * z).
                eq_str = f"{ext_op.__name__}({int_op.__name__}({sx}, {sy}), {sz})"
                eq_val = ext_op(int_op(x, y), z)
                combs.append((eq_str, eq_val))
                # Create equations by grouping the last 2 elements, e.g.: (x + (y * z)).
                eq_str = f"{ext_op.__name__}({sx}, {int_op.__name__}({sy}, {sz}))"
                eq_val = ext_op(x, int_op(y, z))
                combs.append((eq_str, eq_val))
    return combs


def inverter(data: List[int]) -> List[Tuple[int, int, int]]:
    """
        Creates a cartesian product of all possible sign variations
        for every digit in a three digit list comprising a given registration
        number.
    """
    inverted_data = [-x for x in data]
    res = list(product(*zip(data, inverted_data)))
    return res


# Data to process.
INITIAL_DATA: List[str] = [
    "518-2",
    # '533-3',
    # '534-0',
    # '000-3',
    '000-4'
]
# Available functions.
FUNCTIONS: List[Callable] = [   # the_factorial() removed, see solve().
    plus,
    minus,
    mult,
    div,
    power_to,
    root
]
# Get posible combinations to apply the factor operation.
FACTORS: Set[Tuple] = set(product([1, 0, 0], repeat=3))


def main():
    cases = 0       # Count all possible cases (for each input value).
    data = list()   # List with all final data to be dumped in CSV.
    # print("number, solution, number_of_solutions")
    csv_data = []
    csv_data_match = []
    # Iterate over all initial data.
    for eq in INITIAL_DATA:
        # Get values before and after the hyphen.
        nums, res = eq.split('-')
        res = int(res)
        # Get combinations with inverted values.
        combs = inverter([int(n) for n in list(nums)])
        # Iterate over combinations and generate a list with their many possible solutions.
        sol_cnt = 0         # Number of solutions (for each input value).
        solutions = list()  # List with all final data to be dumped in CSV.
        for i in [solve(i, FUNCTIONS) for i in combs]:
            for j in i:
                str_repr, value = j
                # Some values exceed the 4300 digits, hence the 'try-catch'.
                # The function 'sys.set_int_max_str_digits()' may be used instead to increase the str() capabilites.
                try:
                    str(value)
                except ValueError:
                    value = np.nan
                if value == res:
                    sol_cnt += 1
                solutions.append((eq, str_repr, value))
                cases += 1
        # Iterate over all data gathered, and add number of solutions.
        for i in range(len(solutions)):
            eq, str_repr, value = solutions[i]
            solutions[i] += (sol_cnt,)
            # print(f"{eq}, {str_repr} = {value}, {sol_cnt}")

            #unique
            csv_data.append([f"{eq}, {str_repr} = {value}, {sol_cnt}"])
            #/unique
        data.extend(solutions)
        # Print all the solutions for this input.
        # print(f"\nThese are the {sol_cnt} solutions for input {eq}:")
        solutions = [s for s in solutions if (type(s[2]) is int and s[2] == res)]

        f_data = [] #-1
        for i in get_matching_final(get_matching(csv_data)):

            f_data.append(i)
        new_list = [x for x in get_matching_final(get_matching(csv_data))[-1]]
        new_list2 = []
        new_dict = {}

        header = ['plate_num', 'solution', 'total_num']
        
        #Use a context manager instead.
        f = open('registration.csv', 'w')
        writer = csv.writer(f)
        writer.writerow(header)
        writer.writerows(f_data)
        f.close()



if __name__ == "__main__":
    main()







