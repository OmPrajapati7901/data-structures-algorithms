from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # Initialize two pointers, l starting from the beginning and r from the end of the list
        l, r = 0, len(numbers) - 1

        # Loop until the two pointers meet
        while l < r:
            # Calculate the sum of the two elements pointed by l and r
            current_sum = numbers[l] + numbers[r]

            # If the sum is greater than the target, move the right pointer leftward
            if current_sum > target:
                r -= 1
            # If the sum is less than the target, move the left pointer rightward
            elif current_sum < target:
                l += 1
            # If the sum equals the target, return the indices (1-based)
            else:
                return [l + 1, r + 1]

        # If no solution is found, return an empty list
        return []

# Example usage:
# Instantiate the solution class
solution = Solution()
# Example list of numbers and a target sum
numbers = [2, 7, 11, 15]
target = 9
# Call the twoSum method and print the result
print(solution.twoSum(numbers, target))  # Output: [1, 2]
