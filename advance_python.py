# Advanced Python
# The "advanced" features most relavent to DSA:
# Comprehensions

# List, Dict, set comprehension

# An example
squares = [x**2 for x in range(10) if x % 2 != 0]
#  Two pointers/sliding window with Python idioms
"""
left = right = 0
while right < len(s):
    # expand window
    right += 1

    while condition:
        left += 1 # shrink
"""
### Arrays:
# Core patterns to master:
# Two pointers -- Works on sorted arrays or palindorme checks


# def two_sum_sorted(arr: list[int], target: int):
#     l, r = 0, len(arr) - 1

#     while l < r:
#         s = arr[l] + arr[r]
#         if s == target:
#             return [l, r]
#         elif s > target:
#             r -= 1
#         else:
#             l += 1


# print(two_sum_sorted([2, 5, 8, 10, 99], 18))


### Sliding Window - Subarray problems


# Strings in Python are immutable -- every concatenation creates a new object. Use "".join(list) for O(n) instead of  O(n**2) string building.
# Key Operations:
"""
s.split(), s.strip(), s.lower(), s.upper()
"""

s = "Gopal123"
# print(s.lower().strip(), s.upper().strip())
# print(s[::-1], f"type is: {type(s[::-1])}")  # reverse
# print(s.isalnum())  # alphanumeric check
# print(ord("a"))
# print(ord("A"))
# print(ord("G"))
# print(ord("g"))
# print(chr(103))  # int to char
# print(chr(71))  # int to char
