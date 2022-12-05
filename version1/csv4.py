import re

data = [
    ['518-2, plus(minus(-5, 1!), 8) = 2, 12'], 
    ['518-2, minus(plus(-5, 1!), 8) = 2, 12'],
    ['000-4, minus(root(0!, 0), 0!) = -1, 0'],
    ['000-4, power_to(div(0!, 0), 0!) = 3, 0'],
    ['000-6, power_to(div(0!, 0), 0!) = 6, 0'],
    ['518-2, minus(mult(-5, 1!), 8) = 2, 12'],
]
# get_one = []

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

    wd = {s[0].split(',')[0]: s[0] for s in matching_middle}
    wod = {s[0].split(',')[0]: s[0] for s in non_matching_middle}
    keys = sorted(set(wd.keys()).union(wod.keys()), reverse=True)
    final = [[wd[k]] if k in wd else [wod[k]] for k in keys]
    return final

print(one(data))

# def one(data):
#     matching_middle = []
#     non_matching_middle = []

#     matching_final = []
#     nonmatching_final = []

#     for lst in data:
#         for stmnt in lst:
#             solution = re.findall(r'=([^,]*),', stmnt)[0]
#             after_hyphen = stmnt.split("-")[1][0]
#             if (int(solution) == int(after_hyphen)):
#                 matching_middle.append(lst)
#             if (int(solution) != int(after_hyphen)):
#                 non_matching_middle.append(lst)

#     wd = {s[0].split(',')[0]: s[0] for s in matching_middle}
#     wod = {s[0].split(',')[0]: s[0] for s in non_matching_middle}
#     for k, v in wd.items():
#         matching_final.append([v])

#     for k, v in wod.items():
#         nonmatching_final.append([v])

#     combined_final = matching_final + nonmatching_final

#     return combined_final
    # print(combined_final)

one(data)  

# def one(data):
#     matching_middle = []
#     non_matching_middle = []

#     matching_final = []
#     nonmatching_final = []

#     for lst in data:
#         for stmnt in lst:
#             solution = re.findall(r'=([^,]*),', stmnt)[0]
#             after_hyphen = stmnt.split("-")[1][0]
#             if (int(solution) == int(after_hyphen)):
#                 matching_middle.append(lst)
#             if (int(solution) != int(after_hyphen)):
#                 non_matching_middle.append(lst)

    # print(matching_middle)
    # print(non_matching_middle)
# one(data)