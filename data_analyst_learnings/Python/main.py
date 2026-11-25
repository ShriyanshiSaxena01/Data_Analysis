# a=23          #integer
# name ="John Doe" #string
# is_admin = True   #boolean
# is_banned = False
# price = 23.5       #float


# print(type(a))
# print(type(name))
# print(type(is_admin))
# print(type(is_banned))
# print(type(price))



# comments
# typeconversion
# age = "45" #string 
# print(int(age) + 5) #integer


#how to take inpput from user

# pauses the program and waits for the user to enter some data
# user presses enter key to submit the input
# always returns a string
# used to get data directly from the user

# name = input("Enter your name: ")
# print("Hello " + name)

# print("Welcome to the program")
# name = input("Enter your name: ")
# age = input("Enter your age: ")
# print("Hello " + name + ", you are " + age + " years old.")

# convert the age to an integer
# age = int(input("Enter your age: "))

# input() pauses the program ececution and waits for the user to enter some data. The user presses the enter key to submit the input. The input() function always returns a string, so if you want to work with numbers, you need to convert the input to the appropriate type (e.g., int or float).
# accepts an optional prompt string that is displayed to the user before they enter their input. This can be used to provide instructions or context for the input.
# always returns a string, so if you want to work with numbers, you need to convert the input to the appropriate type (e.g., int or float).
# must convert the input to the appropriate type (e.g., int or float) if you want to work with numbers.



# what is operators
# operators are special symbols that perform specific operations on one or more operands.
#  They are used to manipulate data and variables in programming.
#  Operators can be classified into several categories based on the type of operation they perform.
#  Here are some common types of operators:
#  1. Arithmetic Operators: +, -, *, /, %, **
#  2. Comparison Operators: ==, !=, <, >, <=, >=
#  3. Logical Operators: and, or, not
#  4. Assignment Operators: =, +=, -=, *=, /=, %=
#  5. Membership Operators: in, not in  (for lists, strings, and other iterable objects)
#  6. Identity Operators: is, is not (for comparing object identity)
#  7. Floor Division Operator:
#  // returns the quotient of a division operation, discarding the remainder. It is represented by the symbol //.
#  % modulus operator returns the remainder of a division operation. It is represented by the symbol %.
# exponentiation operator is represented by the symbol ** and is used to raise a number to the power of another number.
# 5+3=8 {operation}
# 5 and 3 are operands and + is the operator.  and 8 is the result of the operation.
# operation precedence is the order in which operations are performed in an expression.
#  In Python, the order of precedence is as follows:
# 1. Parentheses ()
# 2. Exponentiation **  
# 3. Multiplication *, Division /, Floor Division //, Modulus %
# 4. Addition +, Subtraction -
# 5. Comparison Operators: ==, !=, <, >, <=, >=
# 6. Logical Operators: and, or, not

# practice
# arithmetic operators
# a=10
# b=3  

# print("Addition:", a + b)        # Addition
# print("Subtraction:", a - b)     # Subtraction  
# print("Multiplication:", a * b)  # Multiplication
# print("Division:", a / b)        # Division
# print("Modulus:", a % b)         # Modulus
# print("Floor Division:", a // b) # Floor Division
# print("Exponentiation:", a ** b) # Exponentiation

# # comparison operators
# x = 5
# y = 10
# print("Equal:", x == y)          # Equal
# print("Not Equal:", x != y)      # Not Equal
# print("Greater Than:", x > y)    # Greater Than
# print("Less Than:", x < y)       # Less Than
# print("Greater Than or Equal:", x >= y)  # Greater Than or Equal
# print("Less Than or Equal:", x <= y)    # Less Than or Equal

# # logical operators
# p = True
# q = False
# print("and:", p and q)    # and
# print("or:", p or q)      # or
# print("not:", not p)      # not

# # assignment operators
# num = 10
# print("Initial value:", num)  # Initial value
# num += 5  # Equivalent to num = num + 5
# print("After += 5:", num)    # After += 5
# num -= 3  # Equivalent to num = num - 3
# print("After -= 3:", num)    # After -= 3
# num *= 2  # Equivalent to num = num * 2
# print("After *= 2:", num)    # After *= 2
# num /= 4  # Equivalent to num = num / 4
# print("After /= 4:", num)    # After /= 4






# # Python – Day 4 Notes

# ## 1. What is a String in Python?

# A string is a sequence of characters enclosed in single quotes (`' '`), double quotes (`" "`), or triple quotes (`''' '''` or `""" """`).

# Strings are used to store text, names, sentences, and other character-based information.

# **Examples:**

# ```python
# name = "Shriyanshi"
# city = 'Bhopal'
# message = """Welcome to Python"""
# ```

# ## 2. String Indexing

# Indexing means accessing individual characters of a string using their position.

# In Python, indexing starts from **0**, not 1.

# Example:

# ```python
# name = "shriyanshi"

# print(name[0])  # First character
# print(name[1])  # Second character
# print(name[2])  # Third character
# print(name[3])  # Fourth character
# ```

# **Output:**

# ```text
# s
# h
# r
# i
# ```

# ### Understanding String Indexing

# For the string `"shriyanshi"`:

# | Character | s | h | r | i | y | a | n | s | h | i |
# |---|---|---|---|---|---|---|---|---|---|---|
# | Positive Index | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |
# | Negative Index | -10 | -9 | -8 | -7 | -6 | -5 | -4 | -3 | -2 | -1 |

# **Important:**
# - Positive indexing starts from the left at 0.
# - Negative indexing starts from the right at -1.
# - Accessing an index outside the string's range causes an `IndexError`.

# Example:

# ```python
# print(name[10])
# ```

# This produces an `IndexError` because the string does not have an index 10.

# ## 3. Multi-line Strings

# Python allows us to create strings containing multiple lines using triple quotes.

# We can use:
# - Triple double quotes (`""" """`)
# - Triple single quotes (`''' '''`)

# **Example:**

# ```python
# poem = """Roses are red,
# Violets are blue,
# Sugar is sweet,
# And so are you."""

# print(poem)
# ```

# **Output:**

# ```text
# Roses are red,
# Violets are blue,
# Sugar is sweet,
# And so are you.
# ```

# We can also access individual characters from a multi-line string using indexing.

# ```python
# print(poem[0])
# ```

# **Output:**

# ```text
# R
# ```

# ## 4. String Immutability

# Strings in Python are **immutable**, which means their individual characters cannot be changed after the string has been created.

# Example:

# ```python
# name = "shriyanshi"

# name[0] = "g"
# ```

# **Output:**

# ```text
# TypeError
# ```

# Explanation:

# Python does not allow direct modification of a character inside an existing string.

# However, we can create a new string using methods such as `replace()`.

# Example:

# ```python
# name = "shriyanshi"
# new_name = name.replace("shriyanshi", "shri")

# print(new_name)
# ```

# **Output:**

# ```text
# shri
# ```

# ## 5. String Length – len()

# The `len()` function returns the total number of characters in a string, including spaces and punctuation.

# **Example:**

# ```python
# name = "shriyanshi"

# print(len(name))
# ```

# **Output:**

# ```text
# 10
# ```

# Another example:

# ```python
# poem = """Roses are red,
# Violets are blue,
# Sugar is sweet,
# And so are you."""

# print(len(poem))
# ```

# `len()` also counts spaces and newline characters.

# ## 6. Python String Methods

# String methods are built-in functions used to perform different operations on strings.

# ### 1. capitalize()

# Converts the first character to uppercase and the remaining characters to lowercase.

# ```python
# name = "shriyanshi"
# print(name.capitalize())
# ```

# Output:

# ```text
# Shriyanshi
# ```

# ### 2. upper()

# Converts all characters into uppercase.

# ```python
# print(name.upper())
# ```

# Output:

# ```text
# SHRIYANSHI
# ```

# ### 3. lower()

# Converts all characters into lowercase.

# ```python
# print(name.lower())
# ```

# Output:

# ```text
# shriyanshi
# ```

# ### 4. title()

# Converts the first character of each word into uppercase.

# ```python
# name = "shriyanshi saxena"
# print(name.title())
# ```

# Output:

# ```text
# Shriyanshi Saxena
# ```

# ### 5. strip()

# Removes leading and trailing whitespace from a string.

# ```python
# name = "  shriyanshi  "

# print(name.strip())
# ```

# Output:

# ```text
# shriyanshi
# ```

# It does not remove spaces between words.

# ### 6. replace()

# Replaces a specified part of a string with another value.

# ```python
# name = "shriyanshi"

# print(name.replace("shriyanshi", "shri"))
# ```

# Output:

# ```text
# shri
# ```

# ### 7. split()

# Splits a string into a list of words or parts.

# ```python
# name = "John Doe"

# print(name.split())
# ```

# Output:

# ```text
# ['John', 'Doe']
# ```

# By default, `split()` separates text using whitespace.

# ### 8. isalpha()

# Checks whether all characters in a string are alphabetic letters.

# Returns `True` if all characters are letters and the string is not empty.

# ```python
# name = "shriyanshi"

# print(name.isalpha())
# ```

# Output:

# ```text
# True
# ```

# ### 9. isnumeric()

# Checks whether all characters in a string are numeric characters.

# Returns `True` if all characters are numeric and the string is not empty.

# ```python
# number = "12345"

# print(number.isnumeric())
# ```

# Output:

# ```text
# True
# ```

# ## 7. String Slicing

# String slicing means extracting a specific part of a string using index positions.

# **Syntax:**

# ```python
# string[start:end:step]
# ```

# - `start` – Starting index (included).
# - `end` – Ending index (excluded).
# - `step` – Number of positions to move at a time.

# ### Practical Examples

# ```python
# name = "shriyanshi"

# print(name[0:5])
# print(name[2:5])
# print(name[2:-1])
# ```

# **Output:**

# ```text
# shriy
# riy
# riyansh
# ```

# ### Understanding the Examples

# **1. `name[0:5]`**

# Extracts characters from index 0 to index 4.

# Output: `shriy`

# **2. `name[2:5]`**

# Extracts characters from index 2 to index 4.

# Output: `riy`

# **3. `name[2:-1]`**

# Starts from index 2 and stops before the last character.

# Output: `riyansh`

# ### More Slicing Examples

# ```python
# name = "shriyanshi"

# print(name[:5])    # Beginning to index 4
# print(name[5:])    # Index 5 to the end
# print(name[-3:])   # Last three characters
# print(name[::-1])  # Reverse the string
# ```

# **Output:**

# ```text
# shriy
# anshi
# shi
# ihsnayirhs
# ```

# ## 8. Quick Revision

# | Concept | Meaning |
# |---|---|
# | String | Sequence of characters |
# | Indexing | Accessing individual characters |
# | Positive indexing | Starts from 0 |
# | Negative indexing | Starts from -1 |
# | Multi-line string | Uses triple quotes |
# | Immutable | Cannot directly change individual string characters |
# | `len()` | Returns the string length |
# | `capitalize()` | Capitalizes the first character |
# | `upper()` | Converts text to uppercase |
# | `lower()` | Converts text to lowercase |
# | `title()` | Capitalizes each word |
# | `strip()` | Removes leading and trailing whitespace |
# | `replace()` | Replaces part of a string |
# | `split()` | Splits a string into a list |
# | `isalpha()` | Checks for alphabetic characters |
# | `isnumeric()` | Checks for numeric characters |
# | Slicing | Extracts a part of a string |

# ## Day 4 – Topics Covered

# - Introduction to Python strings
# - String indexing
# - Positive and negative indexing
# - Multi-line strings
# - String immutability
# - Finding string length using `len()`
# - Python string methods
# - `capitalize()`, `upper()`, `lower()` and `title()`
# - `strip()`, `replace()` and `split()`
# - `isalpha()` and `isnumeric()`
# - String slicing
# - Understanding start, end and step
# - Reversing a string using slicing











