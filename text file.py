def CreateNotes():
    with open("NOTES.TXT", "w") as f:
        while True:
            l = input("Line: ")
            f.write(l + "\n")
            if l == "":
                break


def CountAVD():
    A = V = D = 0
    try:
        with open("NOTES.TXT") as f:
            text = f.read()
            for i in text:
                if i.isalpha():
                    A += 1
                if i in "AEIOUaeiou":
                    V += 1
                if i.isdigit():
                    D += 1
            print(A)
            print(V)
            print(D)
    except:
        print("File not found")


def ShowNotes():
    try:
        with open("NOTES.TXT") as f:
            print(f.read())
    except:
        print("File not found")


def RevText():
    try:
        with open("NOTES.TXT") as f:
            for i in f.readlines():
                if i[0] in "Tt":
                    print(i[::-1])
    except:
        print("File not found")


def CountLines():
    try:
        with open("NOTES.TXT") as f:
            print(len(f.readlines()))
    except:
        print("File not found")


while True:
    ch = input("1: CreateNotes\n2: CountAVD\n3: ShowNotes\n4: RevText\n5: CountLines\n")
    if ch == "1":
        CreateNotes()
    if ch == "2":
        CountAVD()
    if ch == "3":
        ShowNotes()
    if ch == "4":
        RevText()
    if ch == "5":
        CountLines()
