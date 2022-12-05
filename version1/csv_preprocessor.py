import csv
from itertools import groupby
import re
import numpy as np

# print(re.findall(r'=([^,]*),', word)[0])
# word = '518-2, root(5, plus(-1, 8)) = 1, 12'
#digit = re.findall(r'=([^,]*),', word)[0]
#digit.strip()

#get the one with a solution,
#one without
#combine the lists

# new_data = [['518-2, root(5, plus(-1, 8)) = 2, 12']]
# new_data = [['518-2, root(5, plus(-1, 8)) = 2, 12'],
# ['000-4, root(0, root(0!, 0!)) = nan, 0']
# ]
# def get_solution(data):

#     for lst in data:
#         for stmnt in lst:
#             # print(stmnt.split(",")[-1])
#             after_hyphen = stmnt.split("-")[1][0]
#             after_hyphen.strip()
#             # after_hyphen
#             solution = re.findall(r'=([^,]*),', stmnt)[0]
#             solution.strip()   
#             # solution       
#             print(type(after_hyphen), type(solution))
#     try:
#         if int(after_hyphen) == int(solution):
#             # print(lst)
#             return lst
#     except ValueError:
#         data.remove(lst)
#         modified_list = data
#         get_solution(modified_list)
#         return

# get_solution(new_data)
# def get_solution(data):

#     for lst in data:
#         for stmnt in lst:
#             # print(stmnt.split(",")[-1])
#             after_hyphen = stmnt.split("-")[1][0]
#             after_hyphen.strip()
#             solution = re.findall(r'=([^,]*),', stmnt)[0]
#             solution.strip()
#             try:
#                 if int(after_hyphen) == int(solution):
#                     return lst
#                 return
#             except ValueError:
#                 data.remove(lst)
#                 modified_list = data
#                 if int(after_hyphen) == int(solution):
#                     return lst
#                 return 

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
#     # return removed_nan
#     return removed_nan

class CSVPreprocessor:

    # @staticmethod
    # def create_csv(data):
    #     header = ['plate_num', 'solution', 'total_num']
    #     with open('registration.csv', 'a', encoding='UTF8') as f:
    #         writer = csv.writer(f, delimiter='\t',lineterminator='\n')
    #         writer.writerow(header)
    #         for i in data:
    #             writer.writerow(i)
    @staticmethod
    def create_csv(data):
        header = ['plate_num', 'solution', 'total_num']
        with open('registration.csv', mode='w', newline='') as csv_file:
            csv_writer = csv.writer(csv_file)
            csv_writer.writerow(header)
            for row in data:
                csv_writer.writerow(row)

    @staticmethod
    def get_unique(data):
        def designated_version(item):
            return item[0].split(',')[0]

        return [list(v)[0] for _, v in groupby(sorted(data, 
                                                    key = designated_version),
                                            designated_version)]

    @staticmethod
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
        final_list = [x for x in final]
        final_list_unique = np.unique(final_list) 
        return final_list_unique
        

        # keys_unique_set = set(keys)
        # keys_unique_lst = []
        # for k in keys_unique_set:
        #     keys_unique_lst.append(k)
        # print(keys_unique_lst)

        # for lst in data:
        #     for stmnt in lst:
        #         solution = re.findall(r'=([^,]*),', stmnt)[0]
        #         after_hyphen = stmnt.split("-")[1][0]
        #         if (int(solution) == int(after_hyphen)):
        #             matching_middle.append(lst)
        #         if (int(solution) != int(after_hyphen)):
        #             non_matching_middle.append(lst)

        # return matching_middle
        # print(matching_middle)
        # print(non_matching_middle)
        # wd = {s[0].split(',')[0]: s[0] for s in matching_middle}
        # wod = {s[0].split(',')[0]: s[0] for s in non_matching_middle}

        # return wod

        # print(matching_middle)
        # print(non_matching_middle)
        # wd = {s[0].split(',')[0]: s[0] for s in matching_middle}
        # wod = {s[0].split(',')[0]: s[0] for s in non_matching_middle}
        # # return wod
        # for k, v in wd.items():
        #     matching_final.append([v])

        # for k, v in wod.items():
        #     nonmatching_final.append([v])
        # combined_final = matching_final + nonmatching_final
        # return combined_final


    #First pass
    @staticmethod
    def get_matching(data):
        removed_nan = []
        w_solution = []
        wo_solution = []
        for lst in data:
            for stmnt in lst:
                solution = re.findall(r'=([^,]*),', stmnt)[0]
                after_hyphen = stmnt.split("-")[1][0]
                if (solution != " nan" and int(solution) == int(after_hyphen)):
                    w_solution.append(lst)
                if (solution != " nan" and int(solution) != int(after_hyphen)):
                    wo_solution.append(lst)

        w_combined =  w_solution + wo_solution #used for second pass
        # return w_combined
        # return CSVPreprocessor.get_matching_final(w_combined)
        return CSVPreprocessor.get_matching_final(w_combined)




#     @staticmethod
#     def get_matching(data):
# #     #This works
#         removed_nan = []
#         matches = []
#         for lst in data:
#             for stmnt in lst:
#                 solution = re.findall(r'=([^,]*),', stmnt)[0]
#                 after_hyphen = stmnt.split("-")[1][0]
#                 if solution != " nan":
#                     removed_nan.append(lst)
#                 if (solution == after_hyphen):
#                     matches.append(lst)
#         return matches

#     @staticmethod
#     def get_matching(data):
# #     #This works
#         removed_nan = []
#         for lst in data:
#             for stmnt in lst:
#                 solution = re.findall(r'=([^,]*),', stmnt)[0]
#                 if solution != " nan":
#                     removed_nan.append(lst)
#         # print(removed_nan)
#         return removed_nan

    # @staticmethod
    # def get_matching(data):

    #     #This works
    #     removed_nan = []
    #     unique_data = CSVPreprocessor.get_unique(data)
    #     for lst in unique_data:
    #         for stmnt in lst:
    #             solution = re.findall(r'=([^,]*),', stmnt)[0]
    #             after_hyphen = stmnt.split("-")[1][0]
    #             if (solution != " nan" and solution == after_hyphen) or (solution != " nan" and solution != after_hyphen):
    #                 removed_nan.append(lst)
    #     return removed_nan

    # @staticmethod
    # def get_csv_final(data):
    #     # unique = CSVPreprocessor.get_unique(data)
    #     matching = CSVPreprocessor.get_matching(data)
    #     return matching
   

    # @staticmethod
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
    #     # return removed_nan
    #     return removed_nan
                    
          




    