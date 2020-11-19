class Solution:
    # Sliding Window Optimized using Dict
    """ Complexity Analysis
    Time complexity : O(n). Index j will iterate n times.
    Space complexity (HashMap) : O(min(m,n)). Same as the previous approach.
    Space complexity (Table / array / list): O(m). m is the size of the charset. 

    987 / 987 test cases passed.
    Runtime: 60 ms
    Memory Usage: 14.1 MB """

    # def lengthOfLongestSubstring(self, s: str) -> int:
    #     strLen = len(s)
    #     longest_substr_len = 0
    #     left = right = 0
    #     index_map = dict()

    #     for right in range(strLen):
    #         curr_char = s[right]

    #         if curr_char in index_map:
    #             left = max(left, index_map[curr_char])

    #         longest_substr_len = max(longest_substr_len, right-left+1)

    #         index_map[curr_char] = right+1

    #     return longest_substr_len

    # Sliding Window Optimized with a list / ASCII table (space optimized)
    """ Commonly used tables are:
        int[26] for Letters 'a' - 'z' or 'A' - 'Z'
        int[128] for ASCII
        int[256] for Extended ASCII """

    def lengthOfLongestSubstring(self, s: str) -> int:
        strLen = len(s)
        max_sub_len = 0
        left = right = 0
        index = [0]*256

        for right in range(strLen):
            curr_char = s[right]
            left = max(left, index[ord(curr_char)-ord('a')])

            max_sub_len = max(max_sub_len, right-left+1)

            index[ord(curr_char)-ord('a')] = right+1

        return max_sub_len

    # Sliding window Basic
    """ Complexity Analysis
    Time complexity : O(2n)=O(n). In the worst case each character will be visited twice by i and j.
    Space complexity : O(min(m,n)). Same as the previous approach. We need O(k) space for the sliding window, where k is the size of the Set. 
    The size of the Set is upper bounded by the size of the string n and the size of the charset/alphabet m. 
    
    987 / 987 test cases passed.
    Runtime: 68 ms
    Memory Usage: 14.1 MB """

    # def lengthOfLongestSubstring(self, s: str) -> int:
    #     longest_substr_len = 0
    #     left = right = 0
    #     strLen = len(s)
    #     seen = set()

    #     while left < strLen and right < strLen:
    #         curr_char = s[right]

    #         if curr_char not in seen:
    #             seen.add(curr_char)
    #             right += 1
    #             # longest_substr_len = max(longest_substr_len, right-left)
    #             longest_substr_len = max(longest_substr_len, len(seen))
    #         else:
    #             temp_char = s[left]
    #             seen.remove(temp_char)
    #             left += 1

    #     return longest_substr_len


myObj = Solution()
# inpt = "abcabcbb"
inpt = "bacabcbb"
print(myObj.lengthOfLongestSubstring(inpt))
