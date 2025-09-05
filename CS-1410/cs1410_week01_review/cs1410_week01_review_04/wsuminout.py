def suminout(nums,a,b):
    amount = 0
    for i in nums:
        if i == a or i == b:
            pass
        else:
            amount = amount + i
    return amount
print(suminout([1, 2, 3, 4], 1, 2))
