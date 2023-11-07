import pandas as pd
from math import sqrt

df = pd.read_csv(filepath_or_buffer="quantity_sablona.csv", encoding="UTF-8", delimiter=",")

class Qopt:

    def vypocitany_qopt(self, velikost_dodavek, objednavaci_naklady, cena_kus, naklady_drzeni, naklady_jednice, obdobi,
                        pocetdni=360):
        df.loc[:,"Q"] = velikost_dodavek / df.loc[:,"D"]
        df.loc[:,"Interval"] = pocetdni * obdobi / df.loc[:,"D"]
        df.loc[:,"Avg ks"] = df.loc[:,"Q"] / 2
        df.loc[:,"Avg czk"] = df.loc[:,"Avg ks"] * cena_kus
        df.loc[:,"Ns"] = df.loc[:,"Avg ks"] * cena_kus * naklady_drzeni * obdobi
        df.loc[:,"Npz"] = df.loc[:,"D"] * objednavaci_naklady
        df.loc[:,"N"] = df.loc[:,"Ns"] + df.loc[:,"Npz"]
        df.loc[:,"Qopt kontrola"] = sqrt(2 * velikost_dodavek * objednavaci_naklady
                                       / (naklady_jednice * naklady_drzeni * cena_kus * obdobi))
        return df.round(1)

    def ulozit(self, invalid_input = True):
        print(f"\nOptimální objednávací dávka se nachází v řádku:\n{df[df['N'] == df['N'].min()]}\n")
        while invalid_input:
            user_input = input("Chcete tento výsledek uložit jako soubor CSV (A/N)? \n")
            if user_input == "A" or user_input == "a":
                df.round(1).to_csv("quantity_vysledky.csv", encoding="UTF-8", sep=",")
                print("Novy soubour s názvem qopt_vysledky.csv byl úspěšně vytvořen")
                invalid_input = False
            elif user_input == "N" or user_input == "n":
                print("Nothing has been created")
                invalid_input = False
            else:
                print("Neplatné zadání. Zadejte A nebo N")

if __name__ == "__main__":
    qopt = Qopt()
    print(qopt.vypocitany_qopt(10000, 5000, 1, 400, 1, 0.25))
    qopt.ulozit()
    input("Program ukončíte zmáčknutím libovolné klávesy")