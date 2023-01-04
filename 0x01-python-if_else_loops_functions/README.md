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

[3-print_alphabt.py](./3-print_alphabt.py) - Write a program that prints the ASCII alphabet, in lowercase, not followed by a new line.

- Print all the letters except q and e
- You can only use one print function with string format
- You can only use one loop in your code
- You are not allowed to store characters in a variable
- You are not allowed to import any module

[4-print_hexa.py](./4-print_hexa.py) - Write a program that prints all numbers from 0 to 98 in decimal and in hexadecimal (as in the following example)

- You can only use one print function with string format
- You can only use one loop in your code
- You are not allowed to store numbers or strings in a variable
- You are not allowed to import any module

[5-print_comb2.py](./5-print_comb2.py) - Write a program that prints numbers from 0 to 99.

- Numbers must be separated by ,, followed by a space
- Numbers should be printed in ascending order, with two digits
- The last number should be followed by a new line
- You can only use no more than 2 print functions with string format
- You can only use one loop in your code
- You are not allowed to store numbers or strings in a variable
- You are not allowed to import any module

[6-print_comb3.py](./6-print_comb3.py) - Write a program that prints all possible different combinations of two digits.

- Numbers must be separated by ,, followed by a space
- The two digits must be different
- 01 and 10 are considered the same combination of the two digits 0 and 1
- Print only the smallest combination of two digits
- Numbers should be printed in ascending order, with two digits
- The last number should be followed by a new line
- You can only use no more than 3 print functions with string format
- You can only use no more than 2 loops in your code
- You are not allowed to store numbers or strings in a variable
- You are not allowed to import any module

[7-islower.py](./7-islower.py) - Write a function that checks for lowercase character.

- Prototype: def islower(c):
- Returns True if c is lowercase
- Returns False otherwise
- You are not allowed to import any module
- You are not allowed to use str.upper() and str.isupper()
- Tips: ord()

You don’t need to understand **import**

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
