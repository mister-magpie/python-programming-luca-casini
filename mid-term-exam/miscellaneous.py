# miscellaneous.py
# For the following exercises, pseudo-code is not required

# Exercise 1
# Create a list L of numbers from 21 to 39
# print the numbers of the list that are even
# print the numbers of the list that are multiples of 3
print("\nExercise 1 \n")

L = range(21,40)
print([el for el in L if el%2 == 0])
print([el for el in L if el%3 == 0])

# Exercise 2
# Print the last two elements of L
print("\nExercise 2 \n")


print(L[-2:])


# Exercise 3
# What's wrong with the following piece of code? Fix it and
# modify the code in order to have it work AND to have "<i> is in the list"
# printed at least once
print("\nExercise 3 \n")



L = [1, 2, 3]
for i in range(0,10):
    if i in L:
        print("%d is in the list" % i)
    else:
        print("%d not found" % i)


# Exercise 4
# Read the first line from the sprot_prot.fasta file
# Split the line using 'OS=' as delimiter and print the second element
# of the resulting list
print("\nExercise 4\n")

with open('sprot_prot.fasta.txt') as f:
    r = f.read()
    r = r.split("OS=")
    print(r[1])

# Exercise 5
# Split the second element of the list of Exercise 4 using blanks
# as separators, concatenate the first and the second elements and print
# the resulting string
print("\nExercise 5 \n")

s = r[1].split()
print(s[0] + s[1])

# Exercise 6
# reverse the string 'asor rosa'

print("\nExercise 6 \n")


rosa = "asor rosa"
reverse = ""
for i in range(len(rosa)-1,0,-1):
    reverse += rosa[i]
print(rosa, reverse)


# Exercise 7
# Sort the following list: L = [1, 7, 3, 9]
print("\nExercise 7\n")

L7 = [1, 7, 3, 9]
L7.sort()
print(L7)

# Exercise 8
# Create a new sorted list from L = [1, 7, 3, 9] without modifying L

print("\nExercise 8 \n")
L8 = [1, 7, 3, 9]
L_sorted = sorted(L8)
print(L_sorted)


# Exercise 9
# Write to a file the following 2 x 2 table:
# 2 4
# 3 6
print("\nExercise 9 -> saves tabella.txt\n")

with open("tabella","w") as f:
    f.write("2 \t 4 \n3 \t 6 ")
