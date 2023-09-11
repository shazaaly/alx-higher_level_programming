# JavaScript Warm-Up Tasks

This repository contains a set of JavaScript warm-up tasks designed to help you practice your JavaScript skills.

## Task 0: First Constant, First Print

- Create a script that prints "JavaScript is amazing."
- Use a constant variable called `myVar` with the value "JavaScript is amazing."
- Print the output using `console.log(...)`.
- Avoid using `var`.

**Usage:**

```bash
$ ./0-javascript_is_amazing.js
```

## Task 1: 3 Languages

- Create a script that prints three lines:
  - "C is fun"
  - "Python is cool"
  - "JavaScript is amazing"
- Print the output using `console.log(...)`.
- Avoid using `var`.

**Usage:**

```bash
$ ./1-multi_languages.js
```

## Task 2: Arguments

- Create a script that prints a message based on the number of arguments passed:
  - If no arguments are passed, print "No argument."
  - If one argument is passed, print "Argument found."
  - If more than one argument is passed, print "Arguments found."
- Use `console.log(...)` to print the output.
- Reference: `process.argv`

**Usage:**

```bash
$ ./2-arguments.js
$ ./2-arguments.js Best
$ ./2-arguments.js Best School
```

## Task 3: Value of My Argument

- Create a script that prints the first argument passed to it:
  - If no arguments are passed, print "No argument."
- Use `console.log(...)` to print the output.
- Avoid using `var` and `length`.

**Usage:**

```bash
$ ./3-value_argument.js
$ ./3-value_argument.js School
```

## Task 4: Create a Sentence

- Create a script that prints two arguments passed to it in the format: " is ".
- Use `console.log(...)` to print the output.
- Avoid using `var`.

**Usage:**

```bash
$ ./4-concat.js c cool
$ ./4-concat.js c
$ ./4-concat.js
```

## Task 5: An Integer

- Create a script that prints "My number: <first argument converted to an integer>" if the first argument can be converted to an integer.
- If the argument can't be converted, print "Not a number."
- Use `console.log(...)` to print the output.
- Avoid using `var` and `try/catch`.

**Usage:**

```bash
$ ./5-to_integer.js
$ ./5-to_integer.js 89
$ ./5-to_integer.js "89"
$ ./5-to_integer.js 89.89
$ ./5-to_integer.js School
```

## Task 6: Loop to Languages

- Create a script that prints three lines using an array of strings and a loop:
  - "C is fun"
  - "Python is cool"
  - "JavaScript is amazing"
- Use `console.log(...)` to print the output.
- Avoid using `var` and any if/else statements.
- Use a loop (while, for, etc.).

**Usage:**

```bash
$ ./6-multi_languages_loop.js
```

## Task 7: I Love C

- Create a script that prints "C is fun" x times, where x is the first argument of the script.
- If the first argument can't be converted to an integer, print "Missing number of occurrences."
- Use `console.log(...)` to print the output.
- Avoid using `var`.
- Use a loop (while, for, etc.).

**Usage:**

```bash
$ ./7-multi_c.js 2
$ ./7-multi_c.js 5
$ ./7-multi_c.js
$ ./7-multi_c.js -3
```

## Task 8: Square

- Create a script that prints a square with the size specified as the first argument.
- If the first argument can't be converted to an integer, print "Missing size."
- Use the character 'X' to print the square.
- Use `console.log(...)` to print the output.
- Avoid using `var`.
- Use a loop (while, for, etc.).

**Usage:**

```bash
$ ./8-square.js
$ ./8-square.js School
$ ./8-square.js 2
$ ./8-square.js 6
$ ./8-square.js -3
```

## Task 9: Add

- Create a script that prints the addition of two integers.
- Use the first and second arguments as the integers to add.
- Define a function with the prototype: `function add(a, b)`.
- Use `console.log(...)` to print the output.
- Avoid using `var`.

**Usage:**

```bash
$ ./9-add.js
$ ./9-add.js 1
$ ./9-add.js 1 7
$ ./9-add.js 13 89
```

## Task 10: Factorial

- Create a script that computes and prints the factorial of an integer provided as an argument.
- If no argument is provided, assume a factorial of 1.
- Use recursion to calculate the factorial.
- Use a function.
- Use `console.log(...)` to print the output.
- Avoid using `var`.

**Usage:**

```bash
$ ./10-factorial.js
$ ./10-factorial.js 3
$ ./10-factorial.js 89
$ ./10-factorial.js 333
```

## Task 11: Second Biggest!

- Create a script that searches for the second biggest integer in the list of arguments.
- If no arguments are passed, print 0.
- If only one argument is passed, print 0.
- Use `console.log(...)` to print the output.
- Avoid using `var`.

**Usage:**

```bash
$ ./11-second_biggest.js
$ ./11-second_biggest.js 1
$ ./11-second_biggest.js 4 2 5 3 0 -3
```

## Task 12: Object

- Update the script to replace the value 12 with 89 in the object.

**Usage:**

```bash
$ ./12-object.js
```

## Task 13: Add File

- Create a function that returns the addition of two integers.
- The function must be visible from outside and named `add`.

**Usage:**

```javascript
const add = require("./13-add").add;
console.log(add(3, 5));
```

---

Feel free to explore each task and run the associated scripts to practice your JavaScript skills. Good luck with your software engineering journey!
