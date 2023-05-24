"""
Given an unsorted array of integers, find the length of the longest consecutive elements sequence.

For example, given [100, 4, 200, 1, 3, 2], the longest consecutive element sequence is [1, 2, 3, 4]. 
Return its length: 4.

Your algorithm should run in O(n) complexity.
"""
# ordered and changeable - dictionary


def longest_length(elements):
    sorted_elem = sorted(elements)
    max_length = 0 
    curr_length = 1

    for i in range(1, len(sorted_elem)):
        if sorted_elem[i] == sorted_elem[i-1] + 1:
            curr_length += 1
        elif sorted_elem[i] != sorted_elem[i-1]:
            max_length = max(max_length, curr_length)
            curr_length = 1
        
    max_length = max(max_length, curr_length)
    return max_length


elements = [100,4,200,1,3,2]
print(longest_length(elements))