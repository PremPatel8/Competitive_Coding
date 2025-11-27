from collections import defaultdict
"""
[[1487799425,14,1], 
[1487799425,4,0], 
[1487799425,2,0], 8

[1487800378,10,1], 18

[1487801478,18,0], 
[1487801478,18,1], 18

[1487901013,1,0], 17

[1487901211,7,1], 
[1487901211,7,0]], 17

ans = 1487800378 
"""


def find_busiest_period(data):
    current_capacity = 0
    res = -1
    time_capacity = defaultdict(int)

    for data_pt in data:
        timestamp, v_count, direction = data_pt[0], data_pt[1], data_pt[2]

        time_capacity[timestamp] = current_capacity + \
            v_count if direction == 1 else current_capacity - v_count

        current_capacity = time_capacity[timestamp]

    current_capacity = 0

    for time in time_capacity:
        if time_capacity[time] > current_capacity:
            current_capacity = time_capacity[time]
            res = time

    return res


# inpt = [[1487799425, 14, 1], [1487799425, 4, 0], [1487799425, 2, 0], [1487800378, 10, 1], [
#     1487801478, 18, 0], [1487801478, 18, 1], [1487901013, 1, 0], [1487901211, 7, 1], [1487901211, 7, 0]]

inpt = [[1487799426, 21, 1]]

result = find_busiest_period(inpt)
print("result =", result)
# print(result == 1487800378)
print(result == 1487799426)
