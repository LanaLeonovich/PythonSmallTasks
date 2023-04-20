#Napište funkci v Pythonu, která převede každou hodnotu ve
#vstupním slovníku na integer a vrátí nový slovník.
#Hodnoty ve slovníku jsou datové typy, které lze bezpečně
#převést na int. Není nutno vyvolávat žádnou výjimku
#ani validovat vstup.

def convert_values_to_int(input_dict):
    # Vytvoření prázdného slovníku pro výstup
    output_dict = {}
    # Projití každého klíče a hodnoty ve vstupním slovníku
    for key, value in input_dict.items():
        # Převod hodnoty na int a uložení do výstupního slovníku
        output_dict[key] = int(value)
    # Vrácení výstupního slovníku
    return output_dict
