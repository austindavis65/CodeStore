Exercise: Get Longest Monster Cast Member
-------------------------

### Description

In this series of exercises, you will create functions
to create, modify and examine dictionaries that
represent characters in an animated film, and the
cast members who voice the characters.  The
keys of the dictionary will be character names.
The values in the dictionary will be voice actor
names.

For this exercise, you will create a function that
finds the voice actor with the longest name.

### Files

* `monsterfunctions.py` : set of functions to work with monster cast dictionaries.

### Function Name

`get_longest_cast_member`

### Parameters

* `monsters`: a dictionary

### Action

Finds the value in the dictionary that is the
longest string.  You may assume that all cast
members will have different length names.

### Return Value

A string, the value in the dictionary that is the longest
string.

### Examples

    monsters = create_monster_cast()
    monsters = add_cast_member(monsters, "Mike", "Billy Crystal")
    monsters = add_cast_member(monsters, "Sully", "John Goodman")
    get_longest_cast_member(monsters) -> "Billy Crystal"
