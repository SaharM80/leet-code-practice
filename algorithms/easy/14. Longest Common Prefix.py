# Write a function to find the longest common prefix string amongst an array of strings.

# If there is no common prefix, return an empty string "".

 

# Example 1:

# Input: strs = ["flower","flow","flight"]
# Output: "fl"
# Example 2:

# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.
 

# Constraints:

# 1 <= strs.length <= 200
# 0 <= strs[i].length <= 200
# strs[i] consists of only lowercase English letters.

from typing import List

def longestCommonPrefix(strs: List[str]) -> str:

        shortest_word = min(strs, key=len)

        for i in range(len(shortest_word)):
            common_char = strs[0][i]
            for word in strs:
                if common_char != word[i]:
                    a = i
                    return strs[0][:a] 
            
        return shortest_word

print(longestCommonPrefix(['flower', 'flow', 'flight']))
print(longestCommonPrefix(['dog', 'cat', 'goose']))