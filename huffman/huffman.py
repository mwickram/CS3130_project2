from collections import defaultdict
from heapq import *
#Author: Praminda Mahesh Imaduwa-Gamage, UMSL
#CMP3130: Algorithm Analysis and Design, Programming Assignment - 2 11/05/2017
def encode(char2freq):

    heap = [[freq, [char, ""]] for char, freq in char2freq.items()]
    heapify(heap)
    while len(heap) > 1:
        low = heappop(heap)
        high = heappop(heap)
        for pair in low[1:]:
            pair[1] = '0' + pair[1]
        for pair in high[1:]:
            pair[1] = '1' + pair[1]
        heappush(heap, [low[0] + high[0]] + low[1:] + high[1:])
    return sorted(heappop(heap)[1:], key = lambda pos: (len(pos[-1]), pos))

def charIn(charList, freqList):

    text = ""
    for freq in range(len(freqList)):
        text += charList[freq] * freqList[freq]

    char2freq = defaultdict(int)
    for ch in text:
        char2freq[ch] += 1

    huff = encode(char2freq)
    print("Char  Freq  Code")
    numBits = 0
    originalBits = sum(freqList) * 8
    for pos in huff:
        print(" %s     %s    %s" % (pos[0], char2freq[pos[0]], pos[1]))
        numBits += char2freq[pos[0]]*len(pos[1])
    print("")
    print("Memory saved: ", 100 * (originalBits - numBits)//originalBits, "%")

print('\n')
inputStr = input('Character:')
inputNum = input('Frequency:')
characters = list()
for char in inputStr:
    characters.append(char)

#charIn(['a', 'e', 'i', 'n', 'o', 's', 't'], [45, 65, 13, 45, 18, 22, 53])

numbers = inputNum.split(",")
numbers = [int(num) for num in numbers]
print('\n')
charIn(characters, numbers)

