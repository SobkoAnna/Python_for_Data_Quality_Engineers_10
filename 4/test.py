from function_lab_2 import find_duplicates
#function for finding duplicates in list with dicts
import function_lab_2
import random

# function_lab_2.


list_dict = [function_lab_2.create_random_dict() for i in range(random.randint(2, 4))]
function_lab_2.find_duplicates(list_dict)
function_lab_2.create_single_dict(list_dict)

# find_duplicates([{"djsk":3},{"djsk":10}])