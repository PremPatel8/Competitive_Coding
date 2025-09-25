# def first_non_dupe(input_arr):
#     curr_map = {}
#     result = -1
    
#     for idx, no in enumerate(imput_arr):
#         if no in curr_map:
#             curr_map.pop(no)
#         else:
#             curr_map[no] = idx

#     if len(curr_map) == 0:
#         return result

#     min_index = float('inf')
    
#     for no, idx in curr_map.items():
#         if idx < min_index:
#             min_index = idx
#             result = no
    
#     return result

def first_non_dupe(nos):
    unique_nos = set()
    result = -1
    
    for no in nos:
        if no not in unique_nos:
            unique_nos.add(no)
        else:
            unique_nos.remove(no)
    
    if len(unique_nos) == 0:
        return result
    
    for no in nos:
        if no in unique_nos:
            result = no
            break
    
    return result


print(first_non_dupe([4,5,1,2,0,4]))
        