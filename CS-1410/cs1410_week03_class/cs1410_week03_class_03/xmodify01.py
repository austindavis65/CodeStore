from lib import pencil
p = pencil.Pencil(3)
penlist= [0,1,2,3,4,5,6,7,8,9,10,11,12]
def modify01(pencil):
    for i in penlist:
        pencil.click()
    return pencil
print(p.get_num_leads())
print(p.get_current_lead_length())
