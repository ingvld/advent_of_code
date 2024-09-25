class Hand:
    def __init__(self,cards,bet):
        self.hand_type = None
        self.bet = int(bet)
        self.cards = cards

        self.read_hand(cards)

    CARD_ORDER = {'A':14,'K':13,'Q':12,'J':11,'T':10,
                  '9':9,'8':8,'7':7,'6':6,'5':5,'4':4,'3':3,'2':2}

    def read_hand(self,cards):
        count = {}

        for card in cards:
            if card not in count:
                count[card] = 0
            count[card] += 1
        
        count = sorted(count.items(), key=lambda x: x[1],reverse=True)

        if count[0][1] == 5:
            self.hand_type = 6
        elif count[0][1] == 4:
            self.hand_type = 5
        elif count[0][1] == 3 and count[1][1] == 2:
            self.hand_type = 4
        elif count[0][1] == 3:
            self.hand_type = 3
        elif count[1][1] == 2:
            self.hand_type = 2
        elif count[0][1] == 2:
            self.hand_type = 1
        else:
            self.hand_type = 0

    def __lt__(self,other):
        if self.hand_type != other.hand_type:
            return self.hand_type < other.hand_type
        
        for mine,yours in zip(self.cards,other.cards):
            my_val,your_val = self.CARD_ORDER[mine],self.CARD_ORDER[yours]
            if my_val != your_val:
                return my_val < your_val

def oppg1(filename):
    hands = []

    with open(filename) as f:
        for line in f.readlines():
            hands.append(Hand(*line.split()))

    hands.sort(reverse=True)
    total = 0

    for i in range(1,len(hands)+1):
        total += i * hands.pop().bet

    print(total)

oppg1('7-input.txt')