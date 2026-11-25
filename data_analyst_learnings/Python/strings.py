# day 4

name = "shriyanshi"

# print(name[0])  # Accessing the first character
# print(name[1])  # Accessing the second character
# print(name[2])  # Accessing the third character
# print(name[3])  # Accessing the fourth 
# # print(name[10])  # throws an error because the index is out of range


poem="""Roses are red,
Violets are blue,
Sugar is sweet,
And so are you."""

print(poem)  # Printing the multi-line string
print(poem[0])  # Accessing the first character of the multi-line string



# name[0]="g"  # This will throw an error because strings are immutable in Python

# methods
print(len(name))  # Length of the string
print(len(poem))  # Length of the multi-line string
print(name.capitalize())  # Capitalize the first letter
print(name.upper())  # Convert to uppercase
print(name.lower())  # Convert to lowercase
print(name.title())  # Convert to title case
print(name.strip())  # Remove leading and trailing whitespace
print(len(name.strip()))  # Length after stripping whitespace
print(name.replace("shriyanshi", "shri"))  # Replace substring
print(name.split())  # Split the string into a list of words
print(name.isalpha())  # Check if all characters are alphabetic
print(name.isnumeric())  # Check if all characters are digits


# string slicing
print(name[0:5])  # Slicing from index 0 to 4
print(name[2:5])  # Slicing from index 2 to 4
print(name[2:-1])  # Slicing from index 1 to the second last character