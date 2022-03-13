def getCard():
    input_string = input("Enter all the cards you get separated by comma ")
    card = input_string.split(",")
    while (len(card) != 13):
        print("invalid number of card please input again")
        print("")
        input_string = input("Enter all the cards you get separated by comma ")
        card = input_string.split(",")
    return card


def checkCard(card):
    diamonds = ["2d", "3d", "4d", "5d", "6d", "7d", "8d", "9d", "10d", "Jd", "Qd", "Kd", "Ad"]
    clubs = ["2c", "3c", "4c", "5c", "6c", "7c", "8c", "9c", "10c", "Jc", "Qc", "Kc", "Ac"]
    hearts = ["2h", "3h", "4h", "5h", "6h", "7h", "8h", "9h", "10h", "Jh", "Qh", "Kh", "Ah"]
    spades = ["2s", "3s", "4s", "5s", "6s", "7s", "8s", "9s", "10s", "Js", "Qs", "Ks", "As"]
    point = [None] * 13
    for i in range(len(card)):
        if (card[i] == diamonds[0]):
            point[i] = 2
        elif (card[i] == diamonds[1]):
            point[i] = 3
        elif (card[i] == diamonds[2]):
            point[i] = 4
        elif (card[i] == diamonds[3]):
            point[i] = 5
        elif (card[i] == diamonds[4]):
            point[i] = 6
        elif (card[i] == diamonds[5]):
            point[i] = 7
        elif (card[i] == diamonds[6]):
            point[i] = 8
        elif (card[i] == diamonds[7]):
            point[i] = 9
        elif (card[i] == diamonds[8]):
            point[i] = 10
        elif (card[i] == diamonds[9]):
            point[i] = 11
        elif (card[i] == diamonds[10]):
            point[i] = 12
        elif (card[i] == diamonds[11]):
            point[i] = 13
        elif (card[i] == diamonds[12]):
            point[i] = 14
        elif (card[i] == clubs[0]):
            point[i] = 2
        elif (card[i] == clubs[1]):
            point[i] = 3
        elif (card[i] == clubs[2]):
            point[i] = 4
        elif (card[i] == clubs[3]):
            point[i] = 5
        elif (card[i] == clubs[4]):
            point[i] = 6
        elif (card[i] == clubs[5]):
            point[i] = 7
        elif (card[i] == clubs[6]):
            point[i] = 8
        elif (card[i] == clubs[7]):
            point[i] = 9
        elif (card[i] == clubs[8]):
            point[i] = 10
        elif (card[i] == clubs[9]):
            point[i] = 11
        elif (card[i] == clubs[10]):
            point[i] = 12
        elif (card[i] == clubs[11]):
            point[i] = 13
        elif (card[i] == clubs[12]):
            point[i] = 14
        elif (card[i] == hearts[0]):
            point[i] = 2
        elif (card[i] == hearts[1]):
            point[i] = 3
        elif (card[i] == hearts[2]):
            point[i] = 4
        elif (card[i] == hearts[3]):
            point[i] = 5
        elif (card[i] == hearts[4]):
            point[i] = 6
        elif (card[i] == hearts[5]):
            point[i] = 7
        elif (card[i] == hearts[6]):
            point[i] = 8
        elif (card[i] == hearts[7]):
            point[i] = 9
        elif (card[i] == hearts[8]):
            point[i] = 10
        elif (card[i] == hearts[9]):
            point[i] = 11
        elif (card[i] == hearts[10]):
            point[i] = 12
        elif (card[i] == hearts[11]):
            point[i] = 13
        elif (card[i] == hearts[12]):
            point[i] = 14
        elif (card[i] == spades[0]):
            point[i] = 2
        elif (card[i] == spades[1]):
            point[i] = 3
        elif (card[i] == spades[2]):
            point[i] = 4
        elif (card[i] == spades[3]):
            point[i] = 5
        elif (card[i] == spades[4]):
            point[i] = 6
        elif (card[i] == spades[5]):
            point[i] = 7
        elif (card[i] == spades[6]):
            point[i] = 8
        elif (card[i] == spades[7]):
            point[i] = 9
        elif (card[i] == spades[8]):
            point[i] = 10
        elif (card[i] == spades[9]):
            point[i] = 11
        elif (card[i] == spades[10]):
            point[i] = 12
        elif (card[i] == spades[11]):
            point[i] = 13
        elif (card[i] == spades[12]):
            point[i] = 14
        else:
            print("error : invalid card")
    return point


def merge(arr, l, m, r, card1):
    n1 = m - l + 1
    n2 = r - m
    L = [0] * (n1)
    R = [0] * (n2)
    L1 = [0] * (n1)
    R1 = [0] * (n2)
    for i in range(0, n1):
        L[i] = arr[l + i]
        L1[i] = card1[l + i]
    for j in range(0, n2):
        R[j] = arr[m + 1 + j]
        R1[j] = card1[m + 1 + j]
    i = 0
    j = 0
    k = l
    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            card1[k] = L1[i]
            i += 1
        else:
            arr[k] = R[j]
            card1[k] = R1[j]
            j += 1
        k += 1
    while i < n1:
        arr[k] = L[i]
        card1[k] = L1[i]
        i += 1
        k += 1
    while j < n2:
        arr[k] = R[j]
        card1[k] = R1[j]
        j += 1
        k += 1


def mergeSort(arr, l, r, card1):
    if l < r:
        m = l + (r - l) // 2
        mergeSort(arr, l, m, card1)
        mergeSort(arr, m + 1, r, card1)
        merge(arr, l, m, r, card1)


def checkpair(point):
    pair = [None]
    i = len(point) - 1
    while i > 0:
        j = 0
        a = [None] * 2
        if point[i] == point[i - 1]:
            a[j] = i
            a[j + 1] = i - 1
            pair = pair + a
            i = i - 2
            j = j + 2
        else:
            i = i - 1
    pair.pop(0)
    return pair


def checkstraight(point):
    straight = [None]
    i = len(point) - 1
    while i >= 0:
        m = i - 4
        if (m >= 0):
            flag = 1
            OS = [None] * 5
            p = 0
            while i >= m and flag:
                if (point[i] - 1 == point[i - 1]):
                    OS[p] = i
                    p = p + 1
                    i = i - 1
                elif (point[i] == point[i - 1]):
                    i = i - 1
                    m = m - 1
                    if (m <= 0):
                        OS[p] = i
                else:
                    i = i - 1
                    flag = 0
            if (OS[4] != None):
                straight = straight + OS
        else:
            i = i - 1
    straight.pop(0)
    return straight


def Arrange(point, card):
    line1, line2, line3 = 0, 0, 0
    Straight = checkstraight(point)
    check = 0
    while (Straight != []):
        i = 0
        counter = 0
        while counter < 5:
            print(card[Straight[i]], end=' ')
            card.pop(Straight[i])
            point.pop(Straight[i])
            Straight.pop(i)
            counter = counter + 1
        check = check + 1
        Straight = checkstraight(point)
        print("")
    if (check == 1):
        line3 = 1
    elif (check == 2):
        line3 = 1
        line2 = 1
    if (line3 == 0):
        Pair = checkpair(point)
        if (Pair != []):
            counter = 0
            while (Pair != []):
                i = 0
                j = 0
                while (j < 4 and Pair != []):
                    print(card[Pair[i]], end=' ')
                    card.pop(Pair[i])
                    point.pop(Pair[i])
                    Pair.pop(i)
                    j = j + 1
                    counter = counter + 1
                print("")
            if (counter <= 4 and counter > 0):
                line3 = 1
            elif (counter <= 8 and counter > 0):
                line3 = 1
                line2 = 1
            elif (counter <= 10):
                line1 = 1
                line2 = 1
                line3 = 1
        if (line3 == 0):
            position = len(point) - 1
            print(card[position - 2])
            print(card[position - 1])
            print(card[position])
            card.pop(position)
            card.pop(position - 1)
            card.pop(position - 2)
        elif (line2 == 0):
            position = len(point) - 1
            print(card[position - 1])
            print(card[position])
            card.pop(position)
            card.pop(position - 1)
        elif (line1 == 0):
            position = len(point) - 1
            print(card[position])
            card.pop(position)
    elif (line2 == 0):
        Pair = checkpair(point)
        if (Pair != []):
            counter = 0
            while (Pair != []):
                i = 0
                j = 0
                while (j < 4 and Pair != []):
                    print(card[Pair[i]], end=' ')
                    card.pop(Pair[i])
                    point.pop(Pair[i])
                    Pair.pop(i)
                    j = j + 1
                    counter = counter + 1
                print("")
            if (counter <= 4 and counter > 0):
                line2 = 1
            elif (counter <= 8 and counter > 0):
                line2 = 1
                line1 = 1
        if (line2 == 0):
            position = len(point) - 1
            print(card[position - 1])
            print(card[position])
            card.pop(position)
            card.pop(position - 1)
        elif (line1 == 0):
            position = len(point) - 1
            print(card[position])
            card.pop(position)
    else:
        Pair = checkpair(point)
        if (Pair != []):
            counter = 0
            while (Pair != []):
                i = 0
                j = 0
                while (j < 4 and Pair != []):
                    print(card[Pair[i]], end=' ')
                    card.pop(Pair[i])
                    point.pop(Pair[i])
                    Pair.pop(i)
                    j = j + 1
                    counter = counter + 1
                print("")
            if (counter <= 4 and counter > 0):
                line1 = 1
        if (line1 == 0):
            position = len(point) - 1
            print(card[position])
            card.pop(position)
    print("Unvaluable card: ")
    while (card != []):
        print(card[0], end=' ')
        card.pop(0)
    print("")


card = getCard()
point = checkCard(card)
mergeSort(point, 0, 12, card)
print("Your card combination to maximize your winning probability should be : ")
Arrange(point, card)
