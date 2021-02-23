#given integer array
#get sum of every sub-array
#find the max length subarray with highest sum


def findMaxLenSublist(arr,su):
    dict = {}   #empty dictionary to store the ending index
    dict[0] = -1 #if sum 'su' starts from index 0
    sum = 0
    length = 0 #stores max length of sublist with sum
    ending_index = -1 #ending index of max length
    for i in range(len(arr)):
        sum += arr[i]
        if sum not in dict:
            dict[sum] = i

        if sum - su in dict and length < i - dict[sum - su]:
            length = i - dict[sum - su]
            ending_index = i

    print((ending_index - length + 1, ending_index))

if __name__ == "__main__":
    arr = [5,6,-5,5,3,5,3,-2,0]
    sum = 8
    findMaxLenSublist(arr,sum)


#time complexity is O(n)
