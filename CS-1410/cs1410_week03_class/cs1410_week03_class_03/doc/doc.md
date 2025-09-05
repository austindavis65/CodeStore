Exercise: modify01
----------------------

### Description

Write a function that receives a `Pencil` object as a parameter. It should
`click` the pencil 13 times and return the pencil.

### Function Name

modify01

### Parameters

* `pencil`: A `Pencil` object

### Return Value

The modified `pencil`.

### Example

    import pencil
    p = pencil.Pencil(3)
    p = modify01(p)
    print(p.get_num_leads()) # -> 2
    print(p.get_current_lead_length()) # -> 7
