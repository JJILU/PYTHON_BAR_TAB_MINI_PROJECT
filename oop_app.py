import csv
from pathlib import  Path

class BarTab:
    def __init__(self):
        self.table_number = 0
        self.drinks = []
        self.total = 0
        self.tip = 0
        self.grand_total = 0


    def get_table_no(self):
        # get table number from user
        try:
            table_no = int(input("Table number: "))
            self.table_number = table_no
            print("my table no: {t}".format(t=table_no))
            print(f"Starting a tab for table {self.table_number}")
            print(f"New tab created for table {self.table_number}")
        except:
            print("Not a valid table number. Exiting program.")
            return

    def serve_user(self):
        while True:
            name = input("Drink name (or type 'f' to finish): ")
            if name == 'f':
                break

            try:
                cost = float(input(f"{name} price: "))
            except ValueError:
                print("The price must be a number")
                continue

            self.drinks.append((name, cost))

    def calculate_totals(self):
        for _, cost in self.drinks:
            self.total += cost

        self.tip = self.total * 0.20
        self.grand_total = self.total + self.tip

    def create_csv(self):
        # check if there drinks
        if not self.drinks:
            print("No drinks added. Exiting Program")
            return

        # create file path using table number
        path = Path(__file__).parent / f"table_{self.table_number}.csv"
        print(path)
        with path.open('w', newline='') as file:
            writer = csv.writer(file)

            writer.writerow(["Drink name", "Cost"])
            writer.writerows(self.drinks)
            writer.writerow(["Total", self.total])
            writer.writerow(["Tip", self.tip])
            writer.writerow(["Grand Total", self.grand_total])

            print(f"The bar tab has been saved to {path}")






def main():

    # # get table number from user
    # try:
    # table_no = int(input("Table number: "))
    #     print(f"Starting a tab for table {table_no}")
    # except:
    #     print("Not a valid table number. Exiting program.")
    #     return

    # create file path using table number
    # path = Path(__file__).parent / f"table_{table_no}.csv"
    # print(path)

    tab = BarTab()
    tab.get_table_no()
    tab.serve_user()
    tab.calculate_totals()
    tab.create_csv()

    # 2nd instance
    tab_two = BarTab()
    tab_two.get_table_no()
    tab_two.serve_user()
    tab_two.calculate_totals()
    tab_two.create_csv()


    return

if __name__ == "__main__":
    main()