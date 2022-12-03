import csv
from itertools import groupby
import re

# print(re.findall(r'=([^,]*),', word)[0])
# word = '518-2, root(5, plus(-1, 8)) = 1, 12'
#digit = re.findall(r'=([^,]*),', word)[0]
#digit.strip()


# new_data = [['518-2, root(5, plus(-1, 8)) = 2, 12']]

class CSVPreprocessor:

    @staticmethod
    def create_csv(data):
        header = ['plate_num', 'solution', 'total_num']
        with open('registration.csv', 'a', encoding='UTF8') as f:
            writer = csv.writer(f, delimiter='\t',lineterminator='\n')
            writer.writerow(header)
            for i in data:
                writer.writerow(i)

    @staticmethod
    def get_unique(data):
        def designated_version(item):
            return item[0].split(',')[0]

        return [list(v)[0] for _, v in groupby(sorted(data, 
                                                    key = designated_version),
                                            designated_version)]

    @staticmethod
    def get_solution(data):
        for lst in data:
            for stmnt in lst:
                # print(stmnt.split(",")[-1])
                after_hyphen = stmnt.split("-")[1][0]
                after_hyphen.strip()
                digit = re.findall(r'=([^,]*),', stmnt)[0]
                digit.strip()
        # print(f"{after_hyphen} : {digit}")
                if int(after_hyphen) == int(digit):
                    return lst

    