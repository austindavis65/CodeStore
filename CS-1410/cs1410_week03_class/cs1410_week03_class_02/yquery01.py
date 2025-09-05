from lib import pencil
p = pencil.Pencil(3)
p.click()
def query01(p):
    return p.get_current_lead_length()

print(query01(p))
