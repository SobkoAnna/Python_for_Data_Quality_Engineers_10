import random
import string

merged_dict = {}
index_dict = {}
duplicates = set()

def create_single_dict():
    final_dict = {}
    for key, max_value in merged_dict.items():
        if key in duplicates:
            new_key = f"{key}_{index_dict[key]}"
        else:
            new_key = key
        final_dict[new_key] = max_value
    print(final_dict)

def find_duplicates(list_dict):
    for idx, d in enumerate(list_dict, 1):
        for key, value in d.items():
            if key not in merged_dict:
                merged_dict[key] = value
                index_dict[key] = idx
            else:
                duplicates.add(key)
                if merged_dict[key] < value:
                    merged_dict[key] = value
                    index_dict[key] = idx
    return  merged_dict, index_dict

def create_random_dict():
    dictionary = {}
    for j in range(random.randint(1, 28)):
        key = random.choice(string.ascii_lowercase)
        value = random.randint(1, 100)
        dictionary[key] = value
    return dictionary
