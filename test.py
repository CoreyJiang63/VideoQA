nums = [2,3,-2,4]
max_num = -1e8
max_st, max_end = 0,0
def save_arr(i,j):
    max_arry= []
    return max_arry
for i in range(len(nums)):
    temp_max = nums[i]
    for j in range(i,len(nums)):
        temp_max *= nums[j]
        if temp_max>max_num:
            max_num = temp_max
            max_st = i
            max_end = j
print(max_st)
# print(max_st)
print(max_end)
print(nums[max_st:max_end]) 