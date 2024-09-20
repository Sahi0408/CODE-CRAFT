def three_sum(nums):
    nums.sort()  # Step 1: Sort the array
    result = []
    
    for i in range(len(nums) - 2):
        # Skip duplicate elements to avoid redundant triplets
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        
        # Two-pointer approach
        left, right = i + 1, len(nums) - 1
        while left < right:
            s = nums[i] + nums[left] + nums[right]
            
            if s == 0:
                result.append([nums[i], nums[left], nums[right]])
                
                # Skip duplicates for the left pointer
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                # Skip duplicates for the right pointer
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                
                # Move both pointers after finding a valid triplet
                left += 1
                right -= 1
                
            elif s < 0:
                left += 1  # Increase the sum by moving left pointer to the right
            else:
                right -= 1  # Decrease the sum by moving right pointer to the left
    
    return result
