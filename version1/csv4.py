import re

data = [
    ['518-2, plus(minus(-5, 1!), 8) = 2, 12'], 
    ['518-2, minus(plus(-5, 1!), 8) = 2, 12'],
    ['000-4, minus(root(0!, 0), 0!) = -1, 0'],
    ['000-4, power_to(div(0!, 0), 0!) = 3, 0'],
    ['000-6, power_to(div(0!, 0), 0!) = 6, 0'],
]
get_one = []

def one(data):
    matching_middle = []
    non_matching_middle = []

    matching_final = []
    nonmatching_final = []

    for lst in data:
        for stmnt in lst:
            solution = re.findall(r'=([^,]*),', stmnt)[0]
            after_hyphen = stmnt.split("-")[1][0]
            if (int(solution) == int(after_hyphen)):
                matching_middle.append(lst)
            if (int(solution) != int(after_hyphen)):
                non_matching_middle.append(lst)

    print(matching_middle)
    print(non_matching_middle)
one(data)