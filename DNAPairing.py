def DnaPair(id):
    if id == "A":
        return ["A", "T"]
    elif id == "T":
        return ["T", "A"]
    elif id == "C":
        return ["C", "G"]
    elif id == "G":
        return ["G", "C"]
    else:
        pass
def pairElement(Entry):
    finalPair = []
    for i in Entry:
        temp = DnaPair(i)
        finalPair.append(temp)
    return finalPair
    
test = pairElement("TTGAG")
print(test)