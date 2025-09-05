Exercise: query03
----------------------

### Description

Write a function that receives a `Pencil` object as a parameter. It should
return the total length of lead in the pencil. This includes the current lead
length, as well as the full length of all other leads. Remember, the current
lead is not included in the `_num_leads` count (see examples below).

### Function Name

query03

### Parameters

* `pencil`: A `Pencil` object

### Return Value

The total lead length in `pencil`.

### Examples

    p = Pencil(0)
    print(query03(p)) # -> 10

    p1 = Pencil(1)
    print(query03(p1)) # -> 20
