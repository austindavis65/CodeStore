Exercise: Triad Method
-------------------------

### Description

Triad colors are used to make good color choices
for interface design. Triad colors are
three colors are are spread out evenly around the color wheel.  

In this exercise, you will add to your `Color` class
a method to convert a color into its next triad partner.
You can calculate the
red, green, blue values for the next triad color quickly.
The triad color's red value is the current color's green.
The triad color's green value is the current color's blue.
The triad color's blue value is the current color's red.

For example, if the color has 15 red, 45 green, and 199 
blue.  Then the next triad color has 45 red,
199 green, and 15 blue.
The other triad color has 199 red,
15 green, and 45 blue.


### Class Name

`Color`

### Method

`triad()`

### Parameters

* `self` : the `Color` object to use

### Action

Changes the red, green, and blue values
for the color into those of the next triad color.

### Return Value

`True`.

### Examples

    c = Color(15, 45, 199)
    c.getRed() -> 15
    c.getGreen() -> 45
    c.getBlue() -> 199
    c.triad()
    c.getRed() -> 45
    c.getGreen() -> 199
    c.getBlue() -> 15
    c.triad()
    c.getRed() -> 199
    c.getGreen() -> 15
    c.getBlue() -> 45
    c.triad()
    c.getRed() -> 15
    c.getGreen() -> 45
    c.getBlue() -> 199

### Hints

- Remember, you're adding to the code from the previous step.
