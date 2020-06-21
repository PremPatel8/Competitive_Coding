from collections import OrderedDict
from collections import defaultdict
from typing import List


class Solution:
    def getFolderNames(self, names: List[str]) -> List[str]:
        ans = []
        unique_names = set()
        postfix_val = defaultdict(lambda: 1)

        for name in names:
            if name not in unique_names:
                name_to_add = name
            else:
                while True:
                    name_to_add = "%s(%s)" % (name, postfix_val[name])

                    if name_to_add not in unique_names:
                        break

                    postfix_val[name] += 1

            ans.append(name_to_add)
            unique_names.add(name_to_add)

        return ans


myClass = Solution()

names = ["kaido", "kaido(1)", "kaido", "kaido(1)"]

print(myClass.getFolderNames(names))
