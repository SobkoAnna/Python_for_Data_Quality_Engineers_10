import random
import string

merged_dict = {}
index_dict = {}
duplicates = set()
def create_single_dict(list_dict):
    final_dict = {}
    for key, max_value in merged_dict.items():
        if key in duplicates:
            new_key = f"{key}_{index_dict[key]}"  # create a new key with a dictionary index that contains the maximum value for that key
        else:
            new_key = key
        final_dict[new_key] = max_value
    print(final_dict)
    # Create a final dictionary with the required keys
    # final_dict = {f"{key}_{index_dict[key]}" if key in duplicates else key: max_value for key, max_value in merged_dict.items()}
    # print(final_dict)
def find_duplicates(list_dict):
    for idx, d in enumerate(list_dict, 1):
        for key, value in d.items():
            if key not in merged_dict:
                merged_dict[key] = value
                index_dict[key] = idx  # save the index of the first occurrence
            else:
                duplicates.add(key)
                if merged_dict[key] < value:  # check that the new value for repeated key is bigger than previous
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

# def main():
#     list_dict = [create_random_dict() for i in range(random.randint(2, 4))]
#     find_duplicates(list_dict)
#     create_single_dict(list_dict)
