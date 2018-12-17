def giveMeFibonacci(size):
    fibTable = []
    i = 0
    while i < size:
        if len(fibTable) == 0:
            fibTable.append(0)
        elif len(fibTable) == 1:
            fibTable.append(1)
        else:
            newValue = fibTable[-2] + fibTable[-1]
            fibTable.append(newValue)
        i += 1
    for c in fibTable:
        print c

giveMeFibonacci(50)