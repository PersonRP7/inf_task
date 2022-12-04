import re
from itertools import groupby

# data = [
#     ['518-2, div(5!, div(1, 8!)) = nan, 12'],
#     ['518-2, div(5, minus(-1!, 8!)) = nan, 12'],
#     ['518-2, div(5!, power_to(1, 8!)) = 120, 12'],
#     ['518-2, div(5!, plus(1, 8!)) = 0, 12'],
#     ['518-2, plus(minus(-5, 1!), 8) = 2, 12'],
#     ['000-4, minus(root(0!, 0), 0!) = -1, 0'],
#     ['000-4, power_to(div(0!, 0), 0!) = nan, 0'],

# ]
data = [
    ['518-2, div(5!, div(1, 8!)) = nan, 12'],
    ['518-2, div(5, minus(-1!, 8!)) = nan, 12'],
    ['518-2, div(5!, power_to(1, 8!)) = 120, 12'],
    ['518-2, div(5!, plus(1, 8!)) = 0, 12'],
    ['518-2, plus(minus(-5, 1!), 8) = 2, 12'],
    ['518-2, minus(plus(-5, 1!), 8) = 2, 12'],
    ['000-4, minus(root(0!, 0), 0!) = -1, 0'],
    ['000-4, power_to(div(0!, 0), 0!) = nan, 0'],
    ['000-6, power_to(div(0!, 0), 0!) = 6, 0'],
]

   
def get_unique(data):
    def designated_version(item):
        return item[0].split(',')[0]

    return [list(v)[0] for _, v in groupby(sorted(data, 
                                                key = designated_version),
                                        designated_version)]

def get_matching(data):
    #After separating w_solution and w_solution,
    #run get_unique on each list then combine them.
    #This works
    removed_nan = []
    w_solution = []
    wo_solution = []
    ###############################
    for lst in data:
        for stmnt in lst:
            solution = re.findall(r'=([^,]*),', stmnt)[0]
            after_hyphen = stmnt.split("-")[1][0]
            if (solution != " nan" and int(solution) == int(after_hyphen)):
                w_solution.append(lst)
            if (solution != " nan" and int(solution) != int(after_hyphen)):
                wo_solution.append(lst)

    w_solution_unique = get_unique(w_solution)
    wo_solutin_unique = get_unique(wo_solution)
    # print(w_solution_unique)
    # print("#################")
    # print(wo_solutin_unique)
    # combined = w_solution_unique + wo_solutin_unique
    # return combined
    # print(w_solution)
    # print(wo_solution)

# get_matching(data)

# print(get_matching(data))
# def get_matching(data):

#     #This works
#     removed_nan = []
#     # remove_nan = [item for item in data ]
#     for lst in data:
#         for stmnt in lst:
#             solution = re.findall(r'=([^,]*),', stmnt)[0]
#             after_hyphen = stmnt.split("-")[1][0]
#             if (solution != " nan" and solution == after_hyphen) or (solution != " nan" and solution != after_hyphen):
#                 removed_nan.append(lst)
#     print(removed_nan)


# get_matching(data)

# def get_matching(data):

#     #This works
#     removed_nan = []
#     # remove_nan = [item for item in data ]
#     for lst in data:
#         for stmnt in lst:
#             solution = re.findall(r'=([^,]*),', stmnt)[0]
#             if solution != " nan":
#                 removed_nan.append(lst)
#     print(removed_nan)


# get_matching(data)

# def get_matching(data):

#     for lst in data:
#         for stmnt in lst:
#             after_hyphen = stmnt.split("-")[1][0]
#             solution = re.findall(r'=([^,]*),', stmnt)[0]
#             after_hyphen.strip()
#             solution.strip()
#             if solution == " nan":
#                 # print(solution)
#                 data.remove(lst)
#                 # print(data)
#     modified_data = data
#     print(data)

# get_matching(data)