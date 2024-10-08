import os.path
import random
from datetime import datetime, date


class Main:
    def __init__(self):
        self.date_now = datetime.now()
        self.file_name = "news_feed.txt"

    @staticmethod
    def create_block(type_feeld, text, notes):
        return f"{type_feeld}\n{text}\n{notes}\n"

    def append_to_file(self, type_feeld, text, notes):
        file_exists = os.path.exists(self.file_name)
        with open(self.file_name, 'a') as file:
            if not file_exists or os.path.getsize(self.file_name) == 0:
                file.write("News feeds: \n")
            file.write(self.create_block(type_feeld, text, notes) + "\n")
            print("The data is recorded in a file. Choose the following actions")

    def menu(self):
        helps = """News feeds:
            1. News
            2. Private ad
            3. Rent Info
            0. Exit

        """
        print(helps)

    class News:
        def __init__(self, main, text, city):
            self.text = text
            self.city = city
            self.main = main
            self.date_time = self.main.date_now.strftime("%d/%m/%Y %H:%M")
            self.type = "News -----------"
            self.create_news()

        def create_news(self):
            self.notes = f"{self.city}, {self.date_time}"
            self.main.append_to_file(self.type, self.text, self.notes)

    class AD:
        def __init__(self, main, text, input_day, input_month, input_year):
            self.main = main
            self.text = text
            self.actual_until = datetime(input_year, input_month, input_day)
            self.type = "Private Ad -----------"
            self.create_news()

        def calculate_date(self):
            self.expiration = self.actual_until - self.main.date_now
            return self.expiration.days

        def create_news(self):
            self.notes = f"Actual until: {self.actual_until.strftime('%d/%m/%Y')}, {self.calculate_date()} day left"
            self.main.append_to_file(self.type, self.text, self.notes)

    class RentInfo:
        rent_thresholds = {
            "New York": (2000, 5000),
            "Los Angeles": (1500, 4000),
            "Chicago": (1000, 3000),
            "Austin": (800, 2500)
        }

        def __init__(self, main, city, rent_description, rent_price):
            self.city = city
            self.main = main
            self.rent_price = rent_price
            self.type = "RentInfo -----------"
            self.status = self.determine_rent_status()
            self.rent_description = rent_description
            self.create_news()

        def determine_rent_status(self):
            if self.city in self.rent_thresholds:
                min_rent, max_rent = self.rent_thresholds[self.city]
                if self.rent_price < min_rent:
                    return "Cheap housing"
                elif self.rent_price > max_rent:
                    return "Expensive housing"
                else:
                    return "Average price of housing"
            else:
                return "No data available for this city"

        def create_news(self):
            self.rent_query = f"City : {self.city}\nRent_description: {self.rent_description}, rent_price: {self.rent_price}"
            self.notes = f"Status: {self.status}"
            self.main.append_to_file(self.type, self.rent_query, self.notes)

    def run(self):
        while True:
            self.menu()
            choice = input("Select type of data by number of the category: ")

            if choice == "1":
                text = input("News text: ")
                city = input("City: ")
                self.News(menu, text, city)
                print()
            if choice == "2":
                text = input("Private AD text: ")
                print("Please input expiration date :")
                in_day = int(input("Day: "))
                in_month = int(input("Month: "))
                in_year = int(input("Year: "))
                self.AD(menu, text, in_day, in_month, in_year)
                print()

            if choice == "3":
                list_city = list(self.RentInfo.rent_thresholds.keys())
                print("Please Choice City from List: ", list_city)
                city = input("Enter your city: ")
                if city in list_city:
                    rent_description = input("Enter description: ")
                    rent_price = int(input("Enter your rental price per month: "))
                    self.RentInfo(menu, city, rent_description, rent_price)
                    print()
                else:
                    print("Please Check Name")
            elif choice == "0":
                break


menu = Main()