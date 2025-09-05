def create_monster_cast():
    empty = {}
    return empty

def add_cast_member(monsters,character,cast_member):
    monsters[character] = cast_member
    return monsters

def get_cast_member(monsters,character):
    if monsters[character]:
        return monsters[character]

def get_cast_size(monsters):
    count = 0
    for cast in monsters:
        count += 1
    return count

def change_cast_member(monsters,character,cast_member):
    monsters[character] = cast_member
    return monsters

def has_character(monsters,character):
    if character in monsters:
        return True
    else:
        return False

def has_cast_member(monsters,cast_member):
    cast = monsters.values()
    if cast_member in cast:
        return True
    else:
        return False

def get_longest_cast_member(monsters):
    cast = monsters.values()
    casts = []
    for i in cast:
        casts.append(i)
    long = len(casts[0])
    for member in casts:
        if len(member) > long:
            return member

        
