# count the number of time a substring occurs in a string in python:
# input: ABCDCDC
# substring: CDC

def count_substring(string, sub_string):
    count = 0
    for i in range(len(string)):
        if string[i:i+len(sub_string)] == sub_string:
            count += 1
    return count
    
string = input().strip()
sub_string = input().strip()
count = count_substring(string, sub_string)
print(count)

# check string is anagrams or not
str1 = "python"
str2 = "yonthp"
if (sorted(str1) == sorted(str2)):
    print("Anagram")
else:
    print("Not an anagram")
    
# check string is palindrome or not
string = "madam"
if(string == string[:: - 1]):
   print("Palindrome")
else:
    print("Not a Palindrome") 

# 
def split_and_join(line):
    # write your code here
    line = line.split(" ") # line is converted to a list of strings.
    print(line)
    line = "-".join(line)
    return line


# line = input()
line = "This is a string"
result = split_and_join(line)
print(result)
