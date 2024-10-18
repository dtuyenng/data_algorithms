nums = [0,0,1,1,1,2,2,3,3,4]

previous_item = None
unique_elements = 0

for index in range(0, len(nums)):
    # print(nums[index])
    if nums[index] == previous_item:
        nums[index] = "_"
    else:
        unique_elements += 1
        previous_item = nums[index]

nums.sort(key=str)
print(nums)
print(unique_elements)
