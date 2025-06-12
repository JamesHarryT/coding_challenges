def factOfFact(n: int):
    factOfFact = 1
    for i in range(n):
        fact = 1
        for i in range(1, n + 1):
            fact *= i
        factOfFact *= fact
        if n >= 1:
            n -= 1
    print(factOfFact)

factOfFact(4)
#output = 288

factOfFact(5)
#output = 34560

factOfFact(6)
#output = 24883200
