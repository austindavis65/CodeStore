Exercise: modify03
----------------------

### Description

Write a function that receives a `Pencil` object as a parameter. It should click
the pencil 53 times then add two additional leads. Finally, it will click the
pencil 13 more times and return the pencil.

### Function Name

modify03

### Parameters

* `pencil`: A `Pencil` object

### Return Value

The modified `pencil`.

### Examples

    import pencil
    p = pencil.Pencil(5)
    p = modify03(p)
    print(p.get_num_leads()) # -> 1
    print(p.get_current_lead_length()) # -> 4
