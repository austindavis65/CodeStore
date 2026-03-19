Expression evaluator
====================

In this assignment you will implement an evaluator/interpreter for a
simple expression language. This language supports the following:

* Integer literals: 1, 2, 7, -3, etc.
* Plus operations: (5 + 3), etc.
* Minus operations: (3 - 2), etc.
* Negation operations: -3, -(5 + 3), etc.

in any combination:

* -((4 + 5) - (2 - -9)) + 6

You will not be parsing these expressions: they will exist as data
structures in memory with in-memory layouts as described below. The
data structure is called an *abstract syntax tree* (AST).

When you write a program in any programming language, you type text
into an editor. This is called the *concrete syntax*, i.e., the
actual way a program is written down. When it is read and processed
into a data structure, it becomes the *abstract syntax* (not how it
is written down) and this data structure is typically a tree, hence
*abstract syntax tree*.

In Python you might represent it like this:

``` python
class Exp:
    pass

class Literal(Exp):
    def __init__(self, n: int):
        self.n = n

class Plus(Exp):
    def __init__(self, left: Exp, right: Exp):
        self.left = left
        self.right = right

class Minus(Exp):
    def __init__(self, left: Exp, right: Exp):
        self.left = left
        self.right = right

class Negate(Exp):
    def __init__(self, child: Exp):
        self.child = child
```

In a language like Rust with *algebraic datatypes* it would look
like:

``` rust
enum Exp {
    Literal { n: i64 },
    Plus { left: Box<Exp>, right: Box<Exp> },
    Minus { left: Box<Exp>, right: Box<Exp> },
    Negate { child: Box<Exp> },
}
```

Don't worry about the exact syntax and ignore the `Box` part. What
this says in both languages is essentially:

> An expression is a data type that can have four different variants
> or shapes: a literal that stores an integer, a plus that links to
> two other expressions, a minus with the same structure, or a
> negate that has one child expression.

The critical part is the an expression is *one* data type that can
have four different variants. You can have an array of expressions
or write a function that expects an expression as its input and
giving any of those four variants is okay.

The way these are stored in memory in Rust, C, etc. (Python is a
different case with its OOP approach) is to start with a *tag*, an
integer that tells which variant it is, and then the values that
variant holds.

Every expression object is the same size (so they can be stored in
arrays or embedded in other objects), which is the size of the
largest variant plus the size of the tag. Here is what the four
variants looks like in memory. The object is represeted by `ptr`, a
pointer (address) to where the object is located in memory. Here are
illustrations made to look similar to stack frame diagrams, but they
can be located anywhere in memory. An expression always takes 24
bytes in our representation:


### int literal expression object storage:

            +---------------+
            | (unused)      | 16
            +---------------+
            | n: int        | 8
            +---------------+
    ptr ->  | tag: int = 1  | 0
            +---------------+

So an int literal with the value 7 would consist of three 64-bit
values:

    1, 7, <unused>

If you had a pointer to it in `a0`, you would start by loading the
tag. Then if the tag was a 1 you could load the value:

    ld  t0, (a0)    # load the tag
    li  t1, 1       # check if it is a 1
    bne t0, t1, 1f  # not a literal
    ld  t2, 8(a0)   # load the value


### plus expression object storage:

            +---------------+
            | right: *exp   | 16
            +---------------+
            | left: *exp    | 8
            +---------------+
    ptr ->  | tag: int = 2  | 0
            +---------------+

### minus expression object storage:

            +---------------+
            | right: *exp   | 16
            +---------------+
            | left: *exp    | 8
            +---------------+
    ptr ->  | tag: int = 3  | 0
            +---------------+


### negation expression object storage:

            +---------------+
            | (unused)      | 16
            +---------------+
            | child: *exp   | 8
            +---------------+
    ptr ->  | tag: int = 4  | 0
            +---------------+

This is a recursive data type. A plus expression is defined as two
expressions to be added together. In memory, we link them by storing
pointers (addresses) for the left and right subexpressions. Similar
for minus and negate. So, for example, the expression:

    (3 + (5 - 2))

Could be represented in memory like this:

    address:    value:
                +---------------+
    0x1070      | 0x1030        | pointer to (5 - 2)
                +---------------+
    0x1068      | 0x1048        | pointer to 3
                +---------------+
    0x1060      | 0x2           | plus
                +---------------+
    0x1058      | (unused)      |
                +---------------+
    0x1050      | 0x3           | 3
                +---------------+
    0x1048      | 0x1           | literal
                +---------------+
    0x1040      | 0x1018        | pointer to 2
                +---------------+
    0x1038      | 0x1000        | pointer to 5
                +---------------+
    0x1030      | 0x3           | minus
                +---------------+
    0x1028      | (unused)      |
                +---------------+
    0x1020      | 0x2           | 2
                +---------------+
    0x1018      | 0x1           | literal
                +---------------+
    0x1010      | (unused)      |
                +---------------+
    0x1008      | 0x5           | 5
                +---------------+
    0x1000      | 0x1           | literal
                +---------------+

and the `(3 + (5 - 2))` expression would be represented by the
address 0x1060.


First step
----------

In this step you will write the beginning of a function to evaluate
expressions. For this step you only need to handle the cast of
integer literals, so nothing recursive. The structure of your
function should look like this in anticipation of the full version
that you will write in the next step:

    def eval(exp: *expression) -> int:
        set up stack frame (needed in the next step)

        tag = exp.tag
        if tag == 1:        # literal case
            # use the memory layout of a literal variant
            result = exp.n

        else:
            result = -1

        clean up stack frame
        return result
