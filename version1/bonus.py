from typing import List
import re

data = [
    "518-2, minus(plus(-5, -1), -8) = 2, 12",
    "000-4, root(root(0, 0!), 0!) = 1, 0"
]


def has_solution(data:List)->List:
    filtered = []
    for stmnt in data:
        solution = re.findall(r'=([^,]*),', stmnt)[0]
        after_hyphen = stmnt.split("-")[1][0]
        plate_num = stmnt.split(",")[0]
        if (int(solution) == int(after_hyphen)):
            filtered.append(f"{plate_num}, true")
        elif (int(solution) != int(after_hyphen)):
            filtered.append(f"{plate_num}, false")
    return filtered

if __name__ == "__main__":
    print(has_solution(data))