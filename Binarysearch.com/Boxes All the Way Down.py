class Solution:
    def solve(self, matrix):
        
        # Alt syntax
        matrix.sort(key=lambda x: [x[0], -x[1]])
        
        # Alt syntax
        # from operator import itemgetter
        # matrix.sort(key=itemgetter(1), reverse=True)
        # print(matrix)
        # matrix.sort(key=itemgetter(0))
        # print(matrix)

        
        # matrix = sorted(matrix, key=lambda x: [x[0], -x[1]])
        
        # print(matrix)
        
        sub = []

        for box in matrix:
            cur_w, cur_h = box

            index = self.insert_index(sub, cur_h)

            if index == len(sub):
                sub.append(cur_h)
            else:
                sub[index] = cur_h
        
        return len(sub)

    def insert_index(self, sub, this_h):
        lo = 0
        # not len(sub)-1 because the this_h might need to be appened to the end of the list
        hi = len(sub)

        while lo < hi:
            mid = lo + (hi - lo) // 2
            
            if sub[mid] < this_h:
                lo = mid + 1
            else:
                hi = mid
        
        return lo