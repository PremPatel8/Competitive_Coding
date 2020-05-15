# def longest(s1, s2):
#     s1Uni = list(set(s1))
#     s2Uni = list(set(s2))
#     ans = set()
#     i = 0

#     while i < len(s1Uni) or i < len(s2Uni):
#         c1 = s1Uni[i] if i<len(s1Uni) else False
#         c2 = s2Uni[i] if i<len(s2Uni) else False

#         if c1 and c2 and c1 == c2:
#             ans.add(c1)
#         else:
#             if c1:
#                 ans.add(c1)
#             if c2:
#                 ans.add(c2)
#         i += 1
    
#     ans = "".join(sorted(ans))

#     return ans

def longest(s1, s2):
    combinedSet = set(s1+s2)
    return "".join(sorted(combinedSet))


print(longest("xyaabbbccccdefww","xxxxyyyyabklmopq") == "abcdefklmopqwxy")

print(longest("aretheyhere", "yestheyarehere") == "aehrsty")

print(longest("loopingisfunbutdangerous", "lessdangerousthancoding") == "abcdefghilnoprstu")

result = longest("inmanylanguages", "theresapairoffunctions")

print(result, result == "acefghilmnoprstuy")