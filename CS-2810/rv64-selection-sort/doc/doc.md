Find smallest
=============

Write a function called `find_smallest` in `find_smallest.s` that
finds the smallest element in an array. In the event of a tie (the
smallest element appears multiple times in the list), return the
address of the first occurance of the smallest value.

    find_smallest(begin_address, end_address) -> address_of_smallest

It is given the address of the beginning of an array and the address
of the end of the array. Note: `end_address` is the first address
that is past the valid elements of the array. This is similar to how
in a list with 10 elements, 10 is the first index that is past the
end of the list.

The elements are 64-bit values. You should return the address of the
smallest element in the array.
