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

    @staticmethod
    def get_unique(data):
        def designated_version(item):
            return item[0].split(',')[0]

        return [list(v)[0] for _, v in groupby(sorted(data, 
                                                    key = designated_version),
                                            designated_version)]