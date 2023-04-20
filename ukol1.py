#Napište program v Pythonu, který vypíše do konzole seznam
#obsahující prvky Fibonacciho posloupnosti.
#Vstupem bude počet prvků, které mají být v seznamu.
#Fibonacciho posloupnost je posloupnost čísel, kde následující
#číslo je součtem dvou předchozích.
#Na první pozici je umístěna 0, na druhé 1. Další číslo je tudíž
#součtem 0 a 1 čili 1. Následující pak součtem
#1 a 1 čilic 2 atd.
def fibonacci(n):
    if n in (1, 2):
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


print(fibonacci(10))

