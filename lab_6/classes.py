import os.path
import time
from datetime import datetime
import os
import sys
parent_dir = os.path.abspath(os.path.join(os.getcwd(), '..'))
sys.path.append(parent_dir)
from modules import function_3_lab as func_file

class Main:
    def __init__(self):
        self.date_now = datetime.now()
        self.file_name = "news_feed.txt"
        self.new_file_name = "new_news_feed.txt"
        self.folder_path = "./news_feed.txt"


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
            4. Provide records by text file
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
            "Houston": (2000, 5000),
            "Boston": (1500, 4000),
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

    class MoveInfo:
        def __init__(self, main, numb_records, folder_path, new_file_name):
            self.main = main
            self.numb_records = numb_records
            self.folder_path = folder_path
            self.new_file_name = new_file_name
            self.list_records = []
            self.read_file()
            self.get_records()
            self.move_to_file()

        def read_file(self):
            with open(self.folder_path, 'r') as file:
                content = file.read()
            list_records = content.split('\n\n')
            self.list_records = [block.splitlines() for block in list_records]
            return self.list_records

        def get_records(self):
            self.yellow = "\033[33m"
            self.reset = "\033[0m"
            if abs(self.numb_records) > len(self.list_records):
                print(self.yellow + "There are ",len(self.list_records),"records in the file. All records will be moved." + self.reset)
                self.numb_records = len(self.list_records)
            if self.numb_records > 0:
                test_list = self.list_records[:self.numb_records]
            else:
                 test_list = self.list_records[self.numb_records:]
            self.new_i = [[func_file.func_normalized_sentences(item) for item in sublist] for sublist in test_list]
            return self.new_i

        def move_to_file(self):
            with open(self.new_file_name, 'a') as file:
                for item in self.new_i:
                    if len(item) > 0:
                        test_temp = "\n".join(item)
                        file.writelines(f"{test_temp}\n\n")
            print("The data is moved to the file.")

        def remove_file(self, file):
            try:
                if os.path.exists(file):
                    os.remove(file)
                    print(f"File {file} deleted")
                else:
                    print(f"{file} can't find")
            except Exception as e:
                print(f"Error whe try delete file: {e}")

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

            if choice == "4":
                numb_records = int(input("Enter the number of records to be moved: "))
                print()
                print('Default folder: ',self.folder_path)
                folder_path = input("If the path to the file is different, enter it: ")
                if len(folder_path) == 0:
                    folder_path = self.folder_path
                new_file_name = self.new_file_name
                self.MoveInfo(menu, numb_records, folder_path, new_file_name)
                self.MoveInfo.remove_file(menu, folder_path)
                print('Successful')
                time.sleep(2)
                break
            elif choice == "0":
                break

menu = Main()