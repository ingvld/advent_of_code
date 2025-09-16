import sys
from functools import reduce

class Monkey:
    def __init__(self,items,op,test_divisor,iftrue,iffalse):
        self.items = items
        self.test_divisor = test_divisor
        self.iftrue = int(iftrue)
        self.iffalse = int(iffalse)
        self.inspect_count = 0

        if op[1] == 'old':
            self.op = lambda x: x+x if op[0] == '+' else x*x
        else:
            self.op = lambda x: x+int(op[1]) if op[0] == '+' else x*int(op[1])

    def get_item(self,item):
        self.items.append(item)

    def has_items(self):
        return len(self.items) > 0

    def inspect_item(self):
        self.inspect_count += 1
        item = self.op(self.items.pop(0))
        if item % self.test_divisor:
            return (item,self.iffalse)
        return (item,self.iftrue)

    def print_monkey(self):
        print(f'My items are {self.items}')
        print(f'My op with 3 = {self.op(3)}')
        print(f'My test divisor is {self.test_divisor}')
        print(f'If true I throw to monkey {self.iftrue}')
        print(f'If not I throw to monkey {self.iffalse}')
        print()


with open(sys.argv[1]) as f:
    monkey_data = [monkey.split('\n') for monkey in f.read().split('\n\n')]
    monkeys = []
    tests = []

    for data in monkey_data:
        items = list(map(int,data[1][18:].split(', ')))
        op = data[2][23:].split()
        test = int(data[3][21:])
        tests.append(test)
        iftrue,iffalse = int(data[4][29:]),int(data[5][29:])
        monkeys.append(Monkey(items,op,test,iftrue,iffalse))

common_test_multiple = reduce(lambda x,y: x*y, tests)
round = 0

while round < 10000:
    for monkey in monkeys:
        while monkey.has_items():
            item,monkey_index = monkey.inspect_item()
            item %= common_test_multiple
            monkeys[monkey_index].get_item(item)
    round += 1

monkey_activity = sorted([monkey.inspect_count for monkey in monkeys],reverse=True)

print(monkey_activity[0]*monkey_activity[1])
