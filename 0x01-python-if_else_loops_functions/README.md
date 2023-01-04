# 0x01. Python - if/else, loops, functions

[0-positive_or_negative.py](./0-positive_or_negative.py) - This program will assign a random signed number to the variable number each time it is executed. Complete the source code in order to print whether the number stored in the variable number is positive or negative.

- You can find the source code [here](https://github.com/holbertonschool/0x01.py/blob/master/0-positive_or_negative_py)
- The variable number will store a different value every time you will run this program
- You don’t have to understand what import, random. randint do. Please do not touch this code
- The output of the program should be:
  - The number, followed by
    - if the number is greater than 0: is positive
    - if the number is 0: is zero
    - if the number is less than 0: is negative
  - followed by a new line

[1-last_digit.py](./1-last_digit.py) - This program will assign a random signed number to the variable number each time it is executed. Complete the source code in order to print the last digit of the number stored in the variable number.

- You can find the source code [here](https://github.com/holbertonschool/0x01.py/blob/master/1-last_digit_py)
- The variable number will store a different value every time you will run this program
- You don’t have to understand what import, random.randint do. Please do not touch this code. This line should not change: number = random.randint(-10000, 10000)
- The output of the program should be:
  - The string Last digit of, followed by
  - the number, followed by
  - the string is, followed by the last digit of number, followed by
    - if the last digit is greater than 5: the string and is greater than 5
    - if the last digit is 0: the string and is 0
    - if the last digit is less than 6 and not 0: the string and is less than 6 and not 0
  - followed by a new line

[2-print_alphabet.py](./2-print_alphabet.py) - Write a program that prints the ASCII alphabet, in lowercase, not followed by a new line.

- You can only use one print function with string format
- You can only use one loop in your code
- You are not allowed to store characters in a variable
- You are not allowed to import any module

[3-print_number.py](./3-print_number.py) - Complete this source code in order to print the integer stored in the variable number, followed by Battery street, followed by a new line.

- You can find the source code [here](https://github.com/holbertonschool/0x00.py/blob/master/3-print_number.py)
- The output of the script should be:
  - the number, followed by Battery street,
  - followed by a new line
- You are not allowed to cast the variable number into a string
- Your code must be 3 lines long
- You have to use f-strings tips

[4-print_float.py](./4-print_float.py) - Complete the source code in order to print the float stored in the variable number with a precision of 2 digits.

- You can find the source code [here](https://github.com/holbertonschool/0x00.py/blob/master/4-print_float.py)
- The output of the program should be:
  - Float:, followed by the float with only 2 digits
  - followed by a new line
- You are not allowed to cast number to string
- You have to use f-strings

[5-print_string.py](./5-print_string.py) - Complete this source code in order to print 3 times a string stored in the variable str, followed by its first 9 characters.

- You can find the source code here
- The output of the program should be:
  - 3 times the value of str
  - followed by a new line
  - followed by the 9 first characters of str
  - followed by a new line
- You are not allowed to use any loops or conditional statement
- Your program should be maximum 5 lines long

[6-concat.py](./6-concat.py) - Complete this source code to print Welcome to Holberton School!

- You can find the source code here
- You are not allowed to use any loops or conditional statements.
- You have to use the variables str1 and str2 in your new line of code
- Your program should be exactly 5 lines long

[7-edges.py](./7-edges.py) - Complete this [source code](https://github.com/holbertonschool/0x00.py/blob/master/7-edges.py)

- You can find the source code [here](https://github.com/holbertonschool/0x00.py/blob/master/7-edges.py)
- You are not allowed to use any loops or conditional statements
- Your program should be exactly 8 lines long
- word_first_3 should contain the first 3 letters of the variable word
- word_last_2 should contain the last 2 letters of the variable word
- middle_word should contain the value of the variable word without the first and last letters

[8-concat_edges.py](./8-concat_edges.py) - Complete this [source code](https://github.com/holbertonschool/0x00.py/blob/master/8-concat_edges.py) to print object-oriented programming with Python, followed by a new line.

- You can find the source code [here](https://github.com/holbertonschool/0x00.py/blob/master/8-concat_edges.py)
- You are not allowed to use any loops or conditional statements
- Your program should be exactly 5 lines long
- You are not allowed to create new variables
- You are not allowed to use string literals

[9-easter_egg.py](./9-easter_egg.py) - Write a Python script that prints “The Zen of Python”, by TimPeters, followed by a new line.

- Your script should be maximum 98 characters long (please check with wc -m 9-easter_egg.py)

[10-check_cycle.c](./10-check_cycle.c) - Write a function in C that checks if a singly linked list has a cycle in it.

- Prototype: int check_cycle(listint_t \*list);
- Return: 0 if there is no cycle, 1 if there is a cycle

[100-write.py](./100-write.py) - Write a Python script that prints exactly and that piece of art is useful - Dora Korpar, 2015-10-19, followed by a new line.

- Use the function write from the sys module
- You are not allowed to use print
- Your script should print to stderr
- Your script should exit with the status code 1

[101-compile](./101-compile) - Write a script that compiles a Python script file.

The Python file name will be stored in the environment variable $PYFILE

The output filename has to be $PYFILEc (ex: export PYFILE=my_main.py => output filename: my_main.pyc)