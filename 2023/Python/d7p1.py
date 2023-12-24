# inspired by hyper-neutrino's solution (https://github.com/hyper-neutrino) bcs my script wasn't giving the proper answer
# while redoing it I found out why on my own

def getType(hand):
    highest = 0
    second_highest = 0
    cards = {}

    for card in hand:
        cards[card] = cards.get(card, 0) + 1

    for quantity in cards.values():
        if quantity > highest:
            second_highest = highest # thats where the mistake was made, didnt add this line in initial solution
            highest = quantity
        elif quantity > second_highest:
            second_highest = quantity

    if highest == 5:
        return 5
    if highest == 4:
        return 4
    if highest == 3 and second_highest == 2:
        return 3.5
    if highest == 3:
        return 3
    if highest == 2 and second_highest == 2:
        return 2.5
    if highest == 2:
        return 2
    else:
        return 1

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
    mapping = {"A": "E", "K": "D", "Q": "C", "J": "B", "T": "A"}
    main()
