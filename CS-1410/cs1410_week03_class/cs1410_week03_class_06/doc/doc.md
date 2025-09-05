Exercise: modify02
----------------------

### Description

Write a function that receives a `Pencil` object as a parameter. It should add
two leads to the pencil and then return the pencil.

### Function Name

modify02

### Parameters

* `pencil`: A `Pencil` object

### Return Value

The modified `pencil`.

### Example

    import pencil
    p = pencil.Pencil(2)
    p = modify02(p)
    print(p.get_num_leads()) # -> 4
