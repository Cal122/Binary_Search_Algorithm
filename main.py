def binary_search(nums, target):
    low = 0
    high = len(nums) - 1

    while low <= high:
        middle = (low + high) // 2
        
        if nums[middle] == target:
            return middle
        
        elif nums[middle] > target:
            high = middle - 1
        
        else:
            low = middle + 1
    
    return ("Value not found")

num_list = [1,3,5,9,12,15,17]
target1 = 15

binary_index = binary_search(num_list, target1)
print(binary_index)
