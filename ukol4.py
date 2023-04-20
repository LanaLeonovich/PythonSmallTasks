#Co tento program dělá?
def compute(sequence):
    return [num for num in sequence if num % 6 == 0 or num % 8 == 0 or num % 3 == 0]

#Odpověď Tento program přijímá vstupní posloupnost čísel a vrací novou posloupnost
# obsahující pouze ta čísla, která jsou dělitelná buď 6, nebo 8, nebo 3.
# Konkrétně program projde každé číslo v zadané posloupnosti a ověří, zda je dělitelné 6, 8 nebo 3.
# Pokud ano, tak toto číslo přidá do výstupní posloupnosti.
# K tomu dochází díky použití list comprehension, což je způsob, jakým lze v Pythonu vytvořit
# nový seznam pomocí jednoho řádku kódu.