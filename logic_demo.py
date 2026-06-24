# Function - takes a name and returns a greeting string
def greet(name):
    return f"Hello, {name}!"


# For loop - calls the greet function 3 times with different names
names = ["Bilal", "Sara", "Omar"]
for name in names:
    print(greet(name))

# If/else - checks whether a number is even or odd
number = 7
if number % 2 == 0:
    print(f"{number} is even")
else:
    print(f"{number} is odd")


# Function - takes a string and returns how many vowels it contains
def count_vowels(text):
    vowels = "aeiouAEIOU"
    count = 0
    for letter in text:
        if letter in vowels:
            count += 1
    return count


print(count_vowels("architecture"))
