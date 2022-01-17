import heapq

# min heap solution

""" The heapq functions do not keep your list sorted, but only guarantee that the heap property is maintained:

    heap[k] <= heap[2*k+1]
    heap[k] <= heap[2*k+2]

Consequently, heap[0] is always the smallest item.

When you want to iterate over the items in order of priority, 
you cannot simply iterate over the heap but need to pop() items off until the queue is empty. 
heappop() will take the first item, then reorganize the list to fulfil the heap invariant. """


def klargest_min_heap(arr, k):
    tmp = []
    heapq.heapify(tmp)

    for order, no in arr:
        print(f"order, no = {order, no}")
        print(f"tmp before = {tmp}")

        heapq.heappush(tmp, (no, order))
        if len(tmp) > k:
            heapq.heappop(tmp)

        print(f"tmp after = {tmp}")

    print(f"tmp outside = {tmp}")
    res = []

    while tmp:
        res.append(heapq.heappop(tmp)[1])

    return res[::-1]


arr = [(1, 80), (2, 100), (3, 50)]
k = 2

print(klargest_min_heap(arr, k))
