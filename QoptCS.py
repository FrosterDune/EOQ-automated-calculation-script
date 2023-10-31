import pandas as pd
from math import sqrt

df = pd.read_csv("quantity_sablona.csv", encoding="UTF-8", delimiter=";")

class Qopt:

    def vypocty(self, velikost_dodavek, objednavaci_naklady, cena_kus, naklady_drzeni, naklady_jednice, obdobi, pocetdni=360):
        df.loc[:,"Q"] = velikost_dodavek / df.loc[:,"D"]
        df.loc[:,"Interval"] = pocetdni * obdobi / df.loc[:,"D"]
        df.loc[:,"Avg ks"] = df.loc[:,"Q"] / 2
        df.loc[:,"Avg czk"] = df.loc[:,"Avg ks"] * cena_kus
        df.loc[:,"Ns"] = df.loc[:,"Avg ks"] * cena_kus * naklady_drzeni * obdobi
        df.loc[:,"Npz"] = df.loc[:,"D"] * objednavaci_naklady
        df.loc[:,"N"] = df.loc[:,"Ns"] + df.loc[:,"Npz"]
        df.loc[:,"Qopt kontrola"] = sqrt(2 * velikost_dodavek * objednavaci_naklady
                                       / (naklady_jednice * naklady_drzeni * cena_kus * obdobi))
        print(df.round(1))
        print(f"\nOptimální objednávací dávka se nachází v řádku:\n{df[df['N'] == df['N'].min()]}\n")
        self.ulozit()

    def ulozit(self, invalid_input = True):
        while invalid_input:
            user_input = input("Chcete tento výsledek uložit jako soubor CSV (A/N)? \n")
            if user_input == "A" or user_input == "a":
                df.round(1).to_csv("quantity_vysledky.csv", encoding="UTF-8", sep=";")
                print("Novy soubour s názvem qopt_vysledky.csv byl úspěšně vytvořen")
                invalid_input = False
            elif user_input == "N" or user_input == "n":
                print("Nothing has been created")
                invalid_input = False
            else:
                print("Neplatné zadání. Zadejte A nebo N")

Qopt().vypocty(10000, 5000, 1, 400, 1, 0.25)
input("Program ukončíte zmáčknutím libovolné klávesy")