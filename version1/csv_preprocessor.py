import stat


import csv
from itertools import groupby

class CSVPreprocessor:

    @staticmethod
    def create_csv(data):
        header = ['plate_num', 'solution', 'total_num']
        with open('registration.csv', 'a', encoding='UTF8') as f:
            writer = csv.writer(f, delimiter='\t',lineterminator='\n')
            writer.writerow(header)
            for i in data:
                writer.writerow(i)