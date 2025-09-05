Exercise: create03
----------------------

### Description

Write a function that receives one integer parameter. It should return a
`Pencil` object constructed with the number of leads matching the value of the
parameter.

### Function Name

create03

### Parameters

* `num_leads` : An integer (the number of leads to 'put' in the pencil)

### Return Value

A `Pencil` object constructed with `num_leads` leads.

### Examples

    p1 = create07(0)
    print(p1.get_num_leads()) # -> 0
    print(p1.get_current_lead_length()) # -> 10

    p2 = create07(4)
    print(p1.get_num_leads()) # -> 4
    print(p1.get_current_lead_length()) # -> 10

    p3 = create07(10)
    print(p1.get_num_leads()) # -> 5
    print(p1.get_current_lead_length()) # -> 10
