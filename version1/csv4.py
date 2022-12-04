data = [
    ['518-2, plus(minus(-5, 1!), 8) = 2, 12'], 
    ['518-2, minus(plus(-5, 1!), 8) = 2, 12'],
    ['000-4, minus(root(0!, 0), 0!) = -1, 0'],
    ['000-4, power_to(div(0!, 0), 0!) = nan, 0'],
    ['000-6, power_to(div(0!, 0), 0!) = 6, 0'],
]
get_one = []

def one(data):
    for lst in data:
        for stmnt in lst:
            print(stmnt.split(",")[0])
one(data)