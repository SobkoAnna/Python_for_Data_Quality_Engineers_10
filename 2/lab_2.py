import random
import string

list_dict= []  # Empty list to store dictionaries
# Generate a random number of dictionaries between 2 and 10
# Loop to generate dictionaries and add them to the list
for i in range(random.randint(2, 10)):
    dictionary = {}
    for j in range(random.randint(1, 28)):
        key = random.choice(string.ascii_lowercase)
        value = random.randint(1, 100)
        dictionary[key] = value
    list_dict.append(dictionary)

merged_dict = {}
index_dict = {}
duplicates = set()

# Merged of all dictionaries, determining the maximum values and their indices
for idx, d in enumerate(list_dict, 1):
    for key, value in d.items():
        if key not in merged_dict:
            merged_dict[key] = value
            index_dict[key] = idx  # save the index of the first occurrence
        else:
            duplicates.add(key)
            if value > merged_dict[key]: # check that the new value for repeated key is bigger than previous
                merged_dict[key] = value
                index_dict[key] = idx

# Create a final dictionary with the required keys
final_dict = {}
for key, max_value in merged_dict.items():
    if key in duplicates:
        new_key = f"{key}_{index_dict[key]}"  # create a new key with a dictionary index that contains the maximum value for that key
    else:
        new_key = key
    final_dict[new_key] = max_value

print(final_dict)

