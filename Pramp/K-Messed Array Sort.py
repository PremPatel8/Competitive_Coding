import heapq

""" 
A simple solution would be to use an efficient sorting algorithm to sort the whole array again. The worst case time complexity of this approach will be O(N⋅log(N)) where N is the size of the input array. This method also do not use the fact that array is k-sorted.

We can also use insertion sort that will correct the order in just O(N∙K) time. Insertion Sort performs really well for small values of k but it is not recommended for large value of k (use it for k < 12).

However, we can do better than that. If we use min heap, we can get an asymptotically better time complexity. We can solve this problem in O(N⋅log(K)). The idea is to construct a min-heap of size k+1 and insert first k+1 elements into the heap. Then we remove min from the heap and insert next element from the array into the heap and continue the process until both array and heap are exhausted. Each pop operation from the heap should insert the corresponding top element in its correct position in the array.

Time Complexity: building a heap takes O(K) time for K+1 elements. Insertion into and extraction from the min-heap take O(log(K)), each. Across all three loops, we do at least one of these actions N times, so the total time complexity is O(N⋅log(K)). if K is substantially smaller than N, then we can consider log(K) constant and argue that the complexity is practically linear.

Space Complexity: we need to a maintain min-heap of size K+1 throughout the algorithm, so the auxiliary space complexity is O(K).
"""


def sort_k_messed_array(arr, k):
    minHeap = arr[:k+1]
    arrLen = len(arr)

    heapq.heapify(minHeap)

    for i, no in enumerate(arr[k+1:], start=k+1):
        #arr[i-(k+1)] =  heapq.heappop(minHeap)
        #heapq.heappush(minHeap, no)

        # alt method
        arr[i-(k+1)] = heapq.heappushpop(minHeap, no)

    i = 0
    while(minHeap):
        arr[arrLen-(k+1)+i] = heapq.heappop(minHeap)
        i += 1

    return arr


#arr = [1, 4, 5, 2, 3, 7, 8, 6, 10, 9]
#k = 2
#print(sort_k_messed_array(arr, k))
