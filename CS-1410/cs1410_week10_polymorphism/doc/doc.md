Exercise: AdditionProblem Class
-------------------------

### Description

Remember, in this series of exercises, you will create
several classes that will be useful in a
program to help grade school children learn
math facts.  The classes will be used to
represent individual math problems, such as
`2 + 5` or `8 * 3`.  The classes will store
the problem related information, format a
text string to display a problem, and
check a user's answer for correctness.

For this exercise, you will create the `AdditionProblem`
class, and its constructor.  This class will be used
to represent math problems of the form `2 + 5`.  The
class should inherit from `MathProblem`.

### Files

* `additionproblem.py` : Python file with class definition

### Class Name

`AdditionProblem`

### Constructor

`__init__()`

### Parameters

* `self` : the `AdditionProblem` object to initialize
* `lhs`    : a number, the left hand side operand
* `rhs`    : a number, the right hand side operand

### Action

Uses constructor chaining to initialize
the `MathProblem` portions of the class.  Then, use
the method from `MathProblem` to set the operator to
the string `"+"`.

### Examples

    p = AdditionProblem(1, 3) -> p is an AdditionProblem object with operands 1 and 3, and operator of "+".

### Hints

- Remember, you're inheriting from `MathProblem`.
