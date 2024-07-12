class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Initialize an empty string to store alphanumeric characters in lowercase
        nums = ''

        # Iterate through each character in the input string
        for i in s:
            # Check if the character is either an alphabet letter or a digit
            if i.isalpha() or i.isdigit():
                # If it is, convert it to lowercase (if it's a letter) and add it to nums
                nums = nums + i.lower()

        # Print the reversed nums string for debugging (optional)
        # print(nums[::-1])

        # Check if the processed string is the same forwards and backwards
        return nums == nums[::-1]

# Example usage:
# solution = Solution()
# print(solution.isPalindrome("A man, a plan, a canal: Panama"))  # Output: True
