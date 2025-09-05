Exercise: query01
----------------------

### Description

Write a function that receives a `Pencil` object as a parameter. It should
return the length of the current lead in the given pencil.

### Function Name

query01

### Parameters

* `p`: A `Pencil` object

### Return Value

The length of the current lead in `p`.

### Example

    from lib import pencil
    p = pencil.Pencil(3)
    p.click()
    print(query01(p)) # -> 9
