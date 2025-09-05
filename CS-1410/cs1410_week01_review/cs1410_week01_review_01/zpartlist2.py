def partlist2(nums,a,c):
    new = nums[a::c]
    return new
print(partlist2([ 2, 3, 5, 7, 11, 13 ], 2, 3))