from collections import defaultdict

def anagrams(word, words):
    w_dict = defaultdict(int)
    
    ans = []
    flag = False
    
    for c in word:
        w_dict[c] += 1
        
    
    for wrd in words:
        wrds_dict = w_dict.copy()
        
        if len(wrd) != len(word):
            continue
        else:
            for c in wrd:
                if c in wrds_dict and wrds_dict[c] > 0:
                    wrds_dict[c] -= 1
                else:
                    flag = True
                    break
            if flag:
                flag = False
                continue
            else:
                ans.append(wrd)
      
    return ans


print(anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada']))