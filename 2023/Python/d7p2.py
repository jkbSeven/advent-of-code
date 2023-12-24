def getType(hand):
    highest = 0
    second_highest = 0
    cards = {}

    for card in hand:
        cards[card] = cards.get(card, 0) + 1

    jokers = cards.pop("J", 0)

    if len(cards) == 0:
        highest = 5
    elif len(cards) == 1:
        highest = list(cards.values())[0]
    else:
        for quantity in cards.values():
            if quantity > highest:
                second_highest = highest 
                highest = quantity
            elif quantity > second_highest:
                second_highest = quantity

    if highest == 5:
        return 5
    if highest == 4:
        return 4 + jokers
    if highest == 3 and second_highest == 2:
        return 3.5
    if highest == 3:
        return 3 + jokers
    if highest == 2 and second_highest == 2:
        return 3.5 if jokers else 2.5
    if highest == 2:
        return 2 + jokers
    else:
        return 1 + jokers

def getStrength(hand):
    return (getType(hand), "".join(mapping.get(card, card) for card in hand))

def main():
    games = []
    with open("input.txt", "r") as file:
        for line in file:
            hand, bid = line.split()
            games.append((hand, int(bid)))

    games.sort(key=(lambda game: getStrength(game[0])))

    total = 0
    for rank, (hand, bid) in enumerate(games, 1):
        total += rank * bid
        
    print(total)

if __name__ == "__main__":
    mapping = {"A": "E", "K": "D", "Q": "C", "J": "1", "T": "A"}
    main()

