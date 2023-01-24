# 0x05. Python - Exceptions

[0-safe_print_list.py](./0-safe_print_list.py) - Write a function that prints x elements of a list.

- Prototype: def safe_print_list(my_list=[], x=0):
- my_list can contain any type (integer, string, etc.)
- All elements must be printed on the same line followed by a new line.
- x represents the number of elements to print
- x can be bigger than the length of my_list
- Returns the real number of elements printed
- You have to use try: / except:
- You are not allowed to import any module
- You are not allowed to use len()

[1-safe_print_integer.py](./1-safe_print_integer.py) - Write a function that prints an integer with "{:d}".format().

- Prototype: def safe_print_integer(value):
- value can be any type (integer, string, etc.)
- The integer should be printed followed by a new line
- Returns True if value has been correctly printed (it means the value is an integer)
- Otherwise, returns False
- You have to use try: / except:
- You have to use "{:d}".format() to print as integer
- You are not allowed to import any module
- You are not allowed to use type()

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

You don’t need to understand \_\_import\_\_

[8-uppercase.py](./8-uppercase.py) - Write a function that prints a string in uppercase followed by a new line.

- Prototype: def uppercase(str):
- You can only use no more than 2 print functions with string format
- You can only use one loop in your code
- You are not allowed to import any module
- You are not allowed to use str.upper() and str.isupper()
- Tips: ord()

You don’t need to understand \_\_import\_\_

[9-print_last_digit.py](./9-print_last_digit.py) - Write a function that prints the last digit of a number.

- Prototype: def print_last_digit(number):
- Returns the value of the last digit
- You are not allowed to import any module

You don’t need to understand \_\_import\_\_

[10-add.py](./10-add.py) - Write a function that adds two integers and returns the result.

- Prototype: def add(a, b):
- Returns the value of a + b
- You are not allowed to import any module

You don’t need to understand \_\_import\_\_

[11-pow.py](./11-pow.py) - Write a function that computes a to the power of b and return the value.

- Prototype: def pow(a, b):
- Returns the value of a ^ b
- You are not allowed to import any module

You don’t need to understand \_\_import\_\_

[100-write.py](./100-write.py) - Write a Python script that prints exactly and that piece of art is useful - Dora Korpar, 2015-10-19, followed by a new line.

- Use the function write from the sys module
- You are not allowed to use print
- Your script should print to stderr
- Your script should exit with the status code 1

[101-compile](./101-compile) - Write a script that compiles a Python script file.

The Python file name will be stored in the environment variable $PYFILE

The output filename has to be $PYFILEc (ex: export PYFILE=my_main.py => output filename: my_main.pyc)
