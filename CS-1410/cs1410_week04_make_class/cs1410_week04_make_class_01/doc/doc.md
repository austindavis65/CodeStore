Exercise: Brake Method
-------------------------

### Description

In this exercise, you will add to your `Car` class
a method to apply the brake and reduce the speed of an instance.

### Class Name

`Car`

### Method

`brake()`

### Parameters

* `self` : the `Car` object to use
* `delta_speed` : a number, the desired value to subtract from the speed data member.

### Action

Subtracts `delta_speed` from the speed of the object.  If the
new speed is below 0, then set the speed to 0.

Only do this action of `delta_speed` is positive, and
the `Car` isn't already stopped.

### Return Value

`True` if a change occurred, `False` otherwise.

### Examples

    c = Car()
    c.setSpeed(40.) -> True
    c.brake(25.) -> True
    c.brake(30.) -> True
    c.brake(1.) -> False
    c.brake(-1.) -> False

### Hints

- Remember, you're adding to the code from the previous step.
- You may want to use the global constant from your file
  regarding the maximum allowed speed.
