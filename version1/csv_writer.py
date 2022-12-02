import csv
from email import header

import numpy as np
from itertools import product
from math import factorial
from typing import Union, Callable, Tuple, List, Set

def plus(a: int, b: int) -> int:
    return a + b

def minus(a: int, b: int) -> int:
    return a - b

def mult(a: int, b: int) -> int:
    return a * b

def div(a: int, b: int) -> Union[int, float]:
    if b != 0:
        if a % b == 0:
            return a // b
    return np.nan

def the_factorial(a: int) -> Union[int, float]:
    try:
        return factorial(int(a))
    except ValueError:
        return np.nan
    except OverflowError:
        return np.inf

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
                # TODO: Create equations by appling unitary operations (e.g.: 'the_factorial()') on members.
    return combs

def inverter(data: List[int]) -> List[Tuple[int, int, int]]:
    inverted_data = [-x for x in data]
    res = list(product(*zip(data, inverted_data)))
    return res

# Data to process.
INITIAL_DATA: List[str] = [
    "518-2",
    '533-3',
    # '534-0',
    # '000-3',
    # '000-4'
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
    print("number, solution, result")
    cases = 0   # Count all possible cases for the sake of curiosity :)
    for eq in INITIAL_DATA:
        # Get values before and after the hyphen.
        nums, res = eq.split('-')
        # Get combinations with inverted values.
        combs = inverter([int(n) for n in list(nums)])
        # Iterate over combinations and generate a list with their many possible solutions.
        solutions = [solve(i, FUNCTIONS) for i in combs]
        for i in solutions:
            for j in i:
                str_repr, value = j
                # Some values exceed the 4300 digits, hence the 'try-catch'.
                # The function 'sys.set_int_max_str_digits()' may be used instead to increase the str() capabilites.
                try:
                    str(value)
                except ValueError:
                    value = np.inf
                print(f"{eq}, {str_repr} = {value}, {res}")
                cases += 1
    print(f"\nTotal cases: {cases}")

if __name__ == "__main__":
    main()

# header = ['name', 'area', 'country_code2', 'country_code3']
# data = ['Afghanistan', 652090, 'AF', 'AFG']

# with open('countries.csv', 'w', encoding='UTF8') as f:
#     writer = csv.writer(f)

#     # write the header
#     writer.writerow(header)

#     # write the data
#     writer.writerow(data)

header = ['plate_num', 'solution', 'total_num']
