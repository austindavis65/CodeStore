from lib import pencil
def create01():
    p = pencil.Pencil(3)
    return p
print(create01().get_num_leads())
