import os.path
import time
from datetime import datetime
import os
import sys
import re
parent_dir = os.path.abspath(os.path.join(os.getcwd(), '..'))
sys.path.append(parent_dir)
from modules import function_3_lab as func_file
from collections import Counter
import csv
import json
import xml.etree.ElementTree as ET

class Main:
    def __init__(self):
        self.date_now = datetime.now()
        self.file_name = "news_feed.txt"
        self.new_file_name = "new_news_feed.txt"
        self.folder_path = "./news_feed.txt"
        self.json_path = "./file.json"
        self.xml_path = "./file.xml"
        self.yellow = "\033[33m"
        self.reset = "\033[0m"

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

        self.CsvFile()

    def check_exist_file(self, file):
        try:
            if not os.path.exists(file):
                raise FileNotFoundError
        except FileNotFoundError:
            print(self.yellow + f"Error when try read file: {file}" + self.reset)
            sys.exit(1)
        return True
    def menu(self):
        helps = """News feeds:
            1. News
            2. Private ad
            3. Rent Info
            4. Provide records by text file
            5. Provide records by json file
            6. Provide records by xml file
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
                self.content = file.read()
            list_records = self.content.split('\n\n')
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

    class CsvFile:
        def __init__(self):
            self.folder_path = "./news_feed.txt"
            self.word_count_file = 'word_count.csv'
            self.letter_count_file = "letter_count.csv"
            self.word_count()
            self.letter_count()

        def read_file(self):
            with open(self.folder_path, 'r') as file:
                self.content = file.read()
            return self.content
        def word_count(self):
            content = self.read_file()
            content_lower = content.lower()
            splited_list = re.findall(r'\b[a-zA-Z]+\b', content_lower)
            word_count = Counter(splited_list)

            self.write_word_count(word_count)
        def letter_count(self):
            content = self.read_file()
            content_lower = content.lower()
            letters = [char for char in content_lower if char.isalpha()]
            count_all = len(letters)
            letter_count = Counter(letters)
            uppercase_count = Counter (char for char in content if content.upper())
            self.write_letter_count(count_all, letter_count, uppercase_count)

        def write_word_count(self,word_count):
            with open(self.word_count_file, 'w', newline='',encoding='utf-8') as file:
                writer = csv.writer(file, delimiter='-')
                writer.writerow(["word", "count"])
                for word, count in word_count.items():
                    writer.writerow([word,count])
        def write_letter_count(self, count_all, letter_count, uppercase_count):
            with open(self.letter_count_file, 'w', newline='',encoding='utf-8') as file:
                writer = csv.writer(file, delimiter=';')
                writer.writerow(["letter", "count_all", "count_uppercase", "percentage_uppercase"])
                for letter,count in letter_count.items():
                    uppercase = uppercase_count[letter.upper()] if letter.upper() in uppercase_count else 0
                    percentage = count * 100 / count_all
                    writer.writerow([letter,count,uppercase,f"{percentage:.2f}%"])


    class JsonFile:
        def __init__(self,main, numb_records,json_path):
            self.main = main
            self.json_path = json_path
            self.numb_records = numb_records
            self.list_records = []
            self.read_file()
            self.get_records()
        def read_file(self):
            self.main.check_exist_file(self.json_path)
            with open(self.json_path) as file:
                data = json.load(file)
            data_records = data

            if type(data_records) == dict:
                if len(data_records) == 1:
                    for key, records in data_records.items():
                        self.list_records = data_records[key]
            elif type(data_records) == list:
                self.list_records = data_records
            return self.list_records
        def get_records(self):
            self.yellow = "\033[33m"
            self.reset = "\033[0m"
            list_feeds = self.list_records

            if abs(self.numb_records) > len(list_feeds):
                print(self.yellow + "There are ",len(list_feeds),"records in the file. All records will be moved." + self.reset)
                self.numb_records = len(list_feeds)
            if self.numb_records > 0:
                test_list = list_feeds[:self.numb_records]
            else:
                 test_list = list_feeds[self.numb_records:]
            self.writeJsonTxt(test_list)

        def writeJsonTxt(self, test_list):
            with open("output.txt", "a", encoding="utf-8") as file:
                for dictionary in test_list:
                    for key, value in dictionary.items():
                        if key == 'type':
                            file.write(f"{value}\n")
                        else:
                            file.write(f"{key}: {value}\n")
                    file.write("\n")

    class XMLFile:
        def __init__(self,main, numb_records,xml_path):
            self.main = main
            self.xml_path = xml_path
            self.numb_records = numb_records
            self.list_records = []

            self.read_file()
            self.get_records()
        def read_file(self):
            self.main.check_exist_file(self.xml_path)
            # Парсим XML файл
            tree = ET.parse(self.xml_path)
            root = tree.getroot()
            # Проходим по каждому элементу "feed" в корневом элементе
            for feed_element in root:
                feed_data = {}
                # Проходим по каждому подэлементу внутри "feed"
                for child in feed_element:
                    # Добавляем данные в словарь
                    feed_data[child.tag] = child.text
                # Добавляем словарь в список
                self.list_records.append(feed_data)
            #print(self.list_records)
            return self.list_records
        def get_records(self):
            self.yellow = "\033[33m"
            self.reset = "\033[0m"
            list_feeds = self.list_records

            if abs(self.numb_records) > len(list_feeds):
                print(self.yellow + "There are ",len(list_feeds),"records in the file. All records will be moved." + self.reset)
                self.numb_records = len(list_feeds)
            if self.numb_records > 0:
                test_list = list_feeds[:self.numb_records]
            else:
                 test_list = list_feeds[self.numb_records:]
            self.writeXMLTxt(test_list)

        def writeXMLTxt(self, test_list):
            with open("output.txt", "a", encoding="utf-8") as file:
                for dictionary in test_list:
                    for key, value in dictionary.items():
                        if key == 'type':
                            file.write(f"{value}\n")
                        else:
                            file.write(f"{key}: {value}\n")
                    file.write("\n")

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

            if choice == "5":
                numb_records = int(input("Enter the number of records to be moved: "))
                print()
                print('Default path to file: ',self.json_path)
                json_path = input("If the path to the file is different, enter it: ")
                if len(json_path) == 0:
                    json_path = self.json_path
                self.JsonFile(menu, numb_records, json_path)
                self.MoveInfo.remove_file(menu, json_path)
                print('Successful')
                time.sleep(2)
                break

            if choice == "6":
                numb_records = int(input("Enter the number of records to be moved: "))
                print()
                print('Default path to file: ',self.xml_path)
                xml_path = input("If the path to the file is different, enter it: ")
                if len(xml_path) == 0:
                    xml_path = self.xml_path
                self.XMLFile(menu, numb_records, xml_path)
                self.MoveInfo.remove_file(menu, xml_path)
                print('Successful')
                time.sleep(2)
                break

            elif choice == "0":
                break

menu = Main()
#menu.XMLFile(menu,2, "file.xml")