import random

# create list of 100 random numbers from 0 to 1000
list_num =[]
for i in range(0, 100):
    list_num.append(random.randint(0, 1000)) # random function generates a number and adds it to the list
print(list_num)

# sort list from min to max
for i in range(1, 100):
    key = list_num[i] # number is taken from the list
    j = i - 1 # index of the previous number
    while j >= 0 and key < list_num[j]: # comparing two adjacent numbers
        list_num[j + 1] = list_num[j] # numbers are interchanged
        j -= 1
        list_num[j + 1] = key
print(list_num)

# Splitting the list into two separate ones: even and odd numbers
even_num=[]
odd_num=[]
for i in list_num:
    if i % 2 == 0: # check if the number is even
        even_num.append(i) # adding a number to a list
    else:
        odd_num.append(i) # else the number is odd
print(even_num)
print(odd_num)

# calculate average for even numbers
average = 0
if len(even_num) == 0: # check that the list is not empty
    print('empty list') # print result
else:
    average = sum(even_num) / len(even_num)
    print('Average for even numbers', average)

# calculate average for odd numbers
if len(odd_num) == 0: # check that the list is not empty
    print('empty list') # print result
else:
    average = sum(odd_num) / len(odd_num)
    print('Average for odd numbers', average)
