import pandas as pd
from math import sqrt

df = pd.read_csv("quantity_template.csv", encoding="UTF-8", delimiter=",")

class Qopt:

    def calculations(self, order_quantity, ordering_cost, unit_price, holding_cost, unit_cost, period, num_of_days=360):
        df.loc[:,"Q"] = order_quantity / df.loc[:,"D"]
        df.loc[:,"Interval"] = num_of_days * period / df.loc[:,"D"]
        df.loc[:,"Avg qty"] = df.loc[:,"Q"] / 2
        df.loc[:,"Avg cost"] = df.loc[:,"Avg qty"] * unit_price
        df.loc[:,"Hold. cost"] = df.loc[:,"Avg qty"] * unit_price * holding_cost * period
        df.loc[:,"Order. cost"] = df.loc[:,"D"] * ordering_cost
        df.loc[:,"Total cost"] = df.loc[:,"Hold. cost"] + df.loc[:,"Order. cost"]
        df.loc[:,"Qopt checker"] = sqrt(2 * order_quantity * ordering_cost
                                       / (unit_cost * holding_cost * unit_price * period))
        print(df.round(1))
        print(f"\nOptimal order quantity can be found in the row:\n{df[df['Total cost'] == df['Total cost'].min()]}\n")
        self.save()

    def save(self, invalid_input=True):
        while invalid_input:
            user_input = input("Do you want to save this result as a CSV file (Y/N)? \n")
            if user_input == "Y" or user_input == "y":
                df.round(1).to_csv("quantity_results.csv", encoding="UTF-8", sep=",")
                print("A new file with the name 'quantity_results.csv' has been successfully created")
                invalid_input = False
            elif user_input == "N" or user_input == "n":
                print("Nothing has been created")
                invalid_input = False
            else:
                print("Invalid input. Please enter Y or N")

Qopt().calculations(4000, 1200, 300, 0.2, 1, 1)
input("You can exit the program by pressing any key")