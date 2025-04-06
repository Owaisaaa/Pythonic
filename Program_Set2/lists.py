
# Uncomment the code snippets to check the output 

# Adding two lists of equal size
# list1 = [10, 11, 12, 15, 20]
# list2 = [10, 11, 12, 15, 20]
# # Approach 1
# if len(list1)>len(list2):
#     m_list = len(list1)
# else:
#     m_list = len(list2)
# output = []
# for i in range(0, m_list):
#     sum = list1[i] + list2[i]
#     output.append(sum)
# print(f'Sum of the two lists : {output}')

# Approach 2  
# output = [x + y for x, y in zip(list1, list2)]
# print(f'Sum of the two lists : {output}')

# Python code to add two different
# length lists in cyclic manner
 
# Importing
from itertools import cycle

# List initialization
# list1 = [150, 177, 454, 126]
# list2 = [9, 44, 2, 168, 66, 80, 123, 6, 180, 184]
 
# # Using zip
# output = [x + y for x, y in zip(cycle(list1), list2)]
 
# # Printing output
# print(output)


# Counting the occurrences of elements in the list
# days = [1, 50, 100, 5, 1, 100]
# y = set(days)

# print([[x,days.count(x)] for x in y])

# Convert a list into a string, we can use the <.join()> method 
# which joins all the elements into one and returns as a string.
days = ['S','M','T','W','Tr','F','St'] 
ltos = ' '.join(days)
print(ltos)