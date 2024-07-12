from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        # Initialize the variable to store the maximum area found
        largest = 0
        
        # Uncommented nested loop brute force method
        # This method checks all possible pairs of lines
        # It is commented out because it is less efficient (O(n^2) time complexity)
        # for i in range(0, len(height)):
        #     for j in range(i + 1, len(height)):
        #         h = min(height[i], height[j])  # Height of the container is the shorter line
        #         l = j - i  # Width of the container
        #         area = h * l  # Calculate the area
        #         if area > largest:  # Update the largest area if the current one is bigger
        #             largest = area
        
        # Two-pointer approach to find the maximum area in O(n) time complexity
        l = 0  # Left pointer starting at the beginning of the list
        r = len(height) - 1  # Right pointer starting at the end of the list

        # Loop until the two pointers meet
        while l < r:
            # Calculate the height and width of the current container
            h = min(height[l], height[r])  # Height is the shorter line
            w = r - l  # Width is the distance between the two pointers

            # Calculate the area of the container
            area = h * w
            # Update the largest area found
            largest = max(largest, area)

            # Move the pointer that points to the shorter line
            if height[l] < height[r]:
                l = l + 1
            else:
                r = r - 1

        # Return the maximum area found
        return largest

# Example usage:
# solution = Solution()
# result = solution.maxArea([1,8,6,2,5,4,8,3,7])
# print(result)  # Output should be 49
