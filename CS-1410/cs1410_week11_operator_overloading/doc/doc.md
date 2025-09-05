Exercise: Blob Movement
-------------------------

### Description

For this exercise, you will create a method to
move a blob.  This will be done by overriding the
right shift and change operator, `>>=`.

### Class Name

`Blob`

### Method

* `__irshift__()`

### Parameters

* `self`  : the `Blob` object to grow
* `distance` : a float value

### Action

This method will change the `mX` and `mY` data members
of the `self` blob.  `mX` will be updated by adding
`mDx` times `distance` to it.

To avoid going off of the screen, if `mX` is so large
that part of the circle would be off of the screen, then
`mX` is set to the largest value that would not have it
off of the screen.

Or, if `mX` is so small that part of the circle would be
off of the screen, then `mX` is set to the smallest value
that would not have it off of the screen.

The value of `mY` is handled in a similar fashion.

### Return Value

`self` as done in a previous operator.

### Examples

    import blob
    b1 = blob.Blob(1.5, 23, 37, 800, 600, blob.KIND_PLAYER)
    b1 >>= 3.5 # tries to move b1 3.5 pixels in its current direction

### Hints

- The farthest right point on the blob is one radius distance
  to the right of center.
- The farthest left point on the blob is one radius distance
  to the left of center.
- `getRadius()` will tell you the radius of your blob's circle
- The world's width and height can be found in data members.
