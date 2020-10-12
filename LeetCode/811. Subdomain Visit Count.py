from collections import defaultdict
from typing import List

"""
Problem Name: 811. Subdomain Visit Count

Problem Section: Dict / Hash Table

Problem Statement:
A website domain like "discuss.leetcode.com" consists of various subdomains. At the top level, we have "com", at the next level, we have "leetcode.com", and at the lowest level, "discuss.leetcode.com". When we visit a domain like "discuss.leetcode.com", we will also visit the parent domains "leetcode.com" and "com" implicitly.

Now, call a "count-paired domain" to be a count (representing the number of visits this domain received), followed by a space, followed by the address. An example of a count-paired domain might be "9001 discuss.leetcode.com".

We are given a list cpdomains of count-paired domains. We would like a list of count-paired domains, (in the same format as the input, and in any order), that explicitly counts the number of visits to each subdomain.

Example 2:
Input: 
["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"]
Output: 
["901 mail.com","50 yahoo.com","900 google.mail.com","5 wiki.org","5 org","1 intel.mail.com","951 com"]
Explanation: 
We will visit "google.mail.com" 900 times, "yahoo.com" 50 times, "intel.mail.com" once and "wiki.org" 5 times. For the subdomains, we will visit "mail.com" 900 + 1 = 901 times, "com" 900 + 50 + 1 = 951 times, and "org" 5 times.

Resources:
"""

""" 52 / 52 test cases passed.
	Status: Accepted
Runtime: 48 ms
Memory Usage: 14.1 MB """

# Solution techniques are iterate input split on space and then '.' update freq dict

# Time complexity : O(n) Space complexity : O()


class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        domain_freq = defaultdict(int)

        for cpwebsite in cpdomains:
            count, website = cpwebsite.split(" ")
            count = int(count)

            web_split = website.split(".")
            domain_freq[website] += count

            if len(web_split) == 3:
                domain_freq[web_split[len(web_split)-1]] += count
                tmp = web_split[len(web_split)-2] + "." + \
                    web_split[len(web_split)-1]
                domain_freq[tmp] += count
            else:
                domain_freq[web_split[len(web_split)-1]] += count

        # for key, val in domain_freq.items():
        #     print(str(val)+" "+key)

        return [str(val)+" "+key for key, val in domain_freq.items()]


myobj = Solution()
inpt = ["9001 discuss.leetcode.com"]
print(myobj.subdomainVisits(inpt))
