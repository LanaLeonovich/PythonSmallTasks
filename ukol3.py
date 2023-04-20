#Reálný problém. Na vstupu jsou 2 řetězce a je nutné je oba
#porovnat.
#Kontrolují se první 2 znaky, prostřední dva a koncové 4. Oba
#řetězce jsou stejně dlouhé, mají vždy sudou délku a zároveň
#počet znaků obou řetězců je minimálně 10.
#Napište program, který bude provádět tuto kontrolu a pokud
#vznikne shoda, program vrátí True, v opačném
#případě vrátí False.
#

def compare_strings(str1, str2):
    if len(str1) < 10 or len(str2) < 10:
        return False
    if len(str1) % 2 != 0 or len(str2) % 2 != 0:
        return False
    if str1[:2] == str2[:2] and str1[2:-2] == str2[2:-2] and str1[-4:] == str2[-4:]:
        return True
    else:
        return False

print(compare_strings("5NDOOR1G1QI5SHGHUJ95RF2PKSVK5EC2C0LR8GLX2LJ8VH269UGNHE6YD29EBXLPW6AUT3" ,"5NDOOR1G1QI5SHGHUJ95RF2PKSVK5EC2C0LR8GLX2LJ8VH269UGNHE6YD29EBXLPW6AUT3"))

