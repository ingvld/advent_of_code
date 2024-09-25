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


with open('11-test.txt') as f:
    monkey_data = [monkey.split('\n') for monkey in f.read().split('\n\n')]
    monkeys = []

    for data in monkey_data:
        items = list(map(int,data[1][18:].split(', ')))
        op = data[2][23:].split()
        test = int(data[3][21:])
        iftrue,iffalse = int(data[4][29:]),int(data[5][29:])
        monkeys.append(Monkey(items,op,test,iftrue,iffalse))

round = 0
last_inspect_counts = None

while round <= 500:
    for monkey in monkeys:
        while monkey.has_items():
            item,monkey_index = monkey.inspect_item()
            monkeys[monkey_index].get_item(item)
    round += 1

monkey_activity = sorted([monkey.inspect_count for monkey in monkeys],reverse=True)

print(monkey_activity[0]*monkey_activity[1])