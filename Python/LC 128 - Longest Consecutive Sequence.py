from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Convert the list to a set to allow O(1) average time complexity for lookups
        numset = set(nums)
        # Initialize the variable to keep track of the longest consecutive sequence length
        longest = 0

        # Iterate through each number in the original list
        for n in nums:
            # Check if the current number is the start of a sequence
            # A number n is the start of a sequence if n-1 is not in the set
            if n - 1 not in numset:
                # Initialize the length of the current sequence
                length = 0
                # While the next number in the sequence is in the set,
                # increment the length of the sequence
                while (n + length) in numset:
                    length += 1
                
                # Update the longest sequence length if the current sequence is longer
                longest = max(length, longest)
        
        # Return the length of the longest consecutive sequence found
        return longest

# Example usage:
nums = [100, 4, 200, 1, 3, 2]
solution = Solution()
print(solution.longestConsecutive(nums))  # Output should be 4 (sequence: 1, 2, 3, 4)
