n = input("Enter a string: ")
vowels = "aeiouAEIOU"
count = 0

for char in n:
    if char in vowels:
        count += 1

print("Number of vowels:", count)
