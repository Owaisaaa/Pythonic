def CountFrequency(my_list):
 
    # Creating an empty dictionary
    freq = {}
    for items in my_list:
        freq[items] = my_list.count(items)
    return freq
    

# my_list = [1, 1, 1, 5, 5, 3, 1, 3, 3, 1, 4, 4, 4, 2, 2, 2, 2]
my_list = "owaisahmad"
# my_list.sort()
# print(my_list)
freq = CountFrequency(my_list)


# Number of vowel characters in a string
freq_vow = {}
vow = ['a','e','i', 'o', 'u']
for i in my_list:
    if i in vow:
        freq_vow [i] = my_list.count(i)
print(freq)
print(freq_vow)

# Remove spaces at the beginning and at the end of the string - strip()
txt = "     banana     "

x = txt.strip()

print("of all fruits", x, "is my favorite")

# Remove the leading and trailing characters
txt = ",,,,,rrttgg.....banana....rrr"

x = txt.strip(",.grt")

print(x)