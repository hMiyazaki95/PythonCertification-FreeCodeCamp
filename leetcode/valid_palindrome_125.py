# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

# Given a string s, return true if it is a palindrome, or false otherwise.

class Solution(object):
    def isPalindrome(self, s):
        cleaned = "" # created the empty string to store cleaned strings
        for char in s:
            if char.isalnum(): # recognize only numeric or alphabetic
                cleaned += char.lower() # turn all uppercase char into lowercase
        return cleaned == cleaned[::-1] # if the condition above matches and 

        """
        :type s: str
        :rtype: bool
        """
        
# Inputs
# Example 1:

# Input: s = "A man, a plan, a canal: Panama"
# Output: true
# Explanation: "amanaplanacanalpanama" is a palindrome.
# Example 2:

# Input: s = "race a car"
# Output: false
# Explanation: "raceacar" is not a palindrome.
# Example 3:

# Input: s = " "
# Output: true
# Explanation: s is an empty string "" after removing non-alphanumeric characters.
# Since an empty string reads the same forward and backward, it is a palindrome.