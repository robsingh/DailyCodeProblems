#function to find a duplicate element in a limited range list
def findDuplicate(arr):
    #create a visited list of size n+1
    visited = [False] * (len(arr) + 1)
    #for each element in the list, mark it as visited and return if seen before
    for i in range(len(arr)):
        if visited[arr[i]]:    #if element is seen before
            return arr[i]

        #mark element as visited
        visited[arr[i]] = True

    return -1    #no duplicate found


if __name__ == "__main__":
    arr = [1,2,3,3,5]
    print("The duplicate element is:",findDuplicate(arr))
