Exercise: modify04
----------------------

### Description

Write a function that receives a `Pencil` object as a parameter. It should click
the pencil until its current lead length is at the maximum possible value, then
return the pencil. Assume that the given pencil will always have enough lead.

### Function Name

modify04

### Parameters

* `pencil`: A `Pencil` object

### Return Value

The modified `pencil` with its current lead length at the maximum.

### Examples

    import pencil
    p = pencil.Pencil(5)
    p.click()
    print(p.get_current_lead_length()) # -> 9
    p = modify04(p)
    print(p.get_current_lead_length()) # -> 10
