Instructions
------------

Calculate the Hamming Distance between two DNA strands.

Your body is made up of cells that contain DNA. Those cells
regularly wear out and need replacing, which they achieve by
dividing into daughter cells. In fact, the average human body
experiences about 10 quadrillion cell divisions in a lifetime!

When cells divide, their DNA replicates too. Sometimes during this
process mistakes happen and single pieces of DNA get encoded with
the incorrect information. If we compare two strands of DNA and
count the differences between them we can see how many mistakes
occurred. This is known as the “Hamming Distance”.

We read DNA using the letters C, A, G and T. Two strands might look
like this:

GAGCCTACTAACGGGAT
CATCGTAATGACGGCCT
^ ^ ^  ^ ^    ^^

They have 7 differences, and therefore the Hamming Distance is 7.

The Hamming Distance is useful for lots of things in science, not
just biology, so it's a nice phrase to be familiar with :)

Write your code as a single function in `compute.c` (you can find
the prototype in `compute.h`). Given two strings, return the Hamming
distance between the two strings. If the strings are of different
lengths, return -1 instead.

Visualization
-------------

A helpful way to test this code is to use the Python Tutor:

* https://pythontutor.com/

Find the link to use C instead of Python and follow it. Then go down
to the editor at the bottom and copy your code over. Add this
definition for `main` at the bottom:

``` c
int main() {
    char *first = "CAGC";
    char *second = "CATC";
    int result = compute(first, second);
    return 0;
}
```

Then click the “Visualize Execution” button to start the
visualization and step through your code one line at a time.

A few suggestions to make the visualization more helpful:

*   Write your code to advance pointers through each string instead
    of treating them like arrays:

    *   Use `*a` to get the current character from string `a`, and
        `a++` to move it to the next character. Same for `b`. This
        will give the visualizer a pointer that it can display so
        you can see where `a` and `b` are currently pointing after
        they move past the beginning of each string.

    *   Get each character of each string like this:

            char aa = *a;
            char bb = *b;

        Then you will be able to see each character in its own box
        and you can see where each came from by looking at the
        arrows.

    *   The loop should end when either `aa` or `bb` is zero, so
        you can test for the end of the loop using `!aa || !bb`.

    *   You may just want to start with an infinite loop and then
        explictly `break` when you detect the end.

*   The visualizer shows one step per line of code, so if it is
    doing too much in a single step, try breaking your code into
    simple steps so you can see a rendering for each individual
    step.

*   Try changing the strings in `main` to run different tests. For
    example, make one string longer than the other to see how your
    code handles it.
