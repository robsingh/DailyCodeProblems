#given an array containing only 0's,1's and 2's, sort it in linear time and using constant space

def swap(arr,i,j):   #swapping element i,j in the list
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp

def threewaypartition(arr,end):
    start = mid = 0
    pivot = 1

    while mid <= end:
        if arr[mid] < pivot:    #current element = 0
            swap(arr,start,mid)
            start += 1
            mid += 1
        elif arr[mid] > pivot:  #current element = 2
            swap(arr,mid,end)
            end -= 1
        else:                   #current element = 1
            mid += 1

if __name__ == '__main__':
    arr = [0,1,2,2,2,1,0,1,2,1,0,2]
    threewaypartition(arr,len(arr) - 1)
    print(arr)
