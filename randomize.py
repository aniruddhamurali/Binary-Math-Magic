import random

def randomize():
    cards = []
    with open('sorted_cards.txt', 'r') as file:
        for line in file.readlines():
            line = line.strip()
            line = line.split(' ')
            nums = line[1].split(',')
            random.shuffle(nums)
            cards.append(nums)

    with open('randomized_cards.txt', 'w') as file:
        string = ""
        for k in range(0, len(cards)):
            string += str(2**k) + ": "
            for n in cards[k]:
                string += str(n) + ","
            string = string[:len(string)-1]
            string += "\n"
        file.write(string)

randomize()
