# Determines the numbers to put on each of the six cards for the magic trick

def bits(n):
    binNum = bin(n)
    binNum = binNum[2:]
    b = [int(i) for i in binNum]
    b.reverse()
    for j in range(0, 6-len(b)):
        b.append(0)
    return b


def main():
    bitReps = []
    for i in range(1,64):
        # The number (i) is index+1
        # bitReps[i] is the binary representation of i
        bitReps.append(bits(i))

    # 6 elements, each element represents a card
    cards = [ [], [], [], [], [], [] ]

    for j in range(0,len(bitReps)):
        if bitReps[j][0] == 1:
            cards[0].append(j+1)
        if bitReps[j][1] == 1:
            cards[1].append(j+1)
        if bitReps[j][2] == 1:
            cards[2].append(j+1)
        if bitReps[j][3] == 1:
            cards[3].append(j+1)
        if bitReps[j][4] == 1:
            cards[4].append(j+1)
        if bitReps[j][5] == 1:
            cards[5].append(j+1)

    with open('sorted_cards.txt', 'w') as file:
        string = ""
        for k in range(0, len(cards)):
            string += str(2**k) + ": "
            for n in cards[k]:
                string += str(n) + ","
            string = string[:len(string)-1]
            string += "\n"
        file.write(string)
                
            
main()

