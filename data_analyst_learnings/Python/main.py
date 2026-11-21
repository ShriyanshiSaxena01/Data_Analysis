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