#problem - Find largest sub-array formed by consecutive integers.
#what is sub-array? An array composed from a contiguous block of the original array's elements.


#function to check if subarray 'arr[i...j]' is formed by consecutive integers
def consec_elem(arr,i,j,min,max):
    #criteria for consecutive elements, the diff between the min and max element should be == j-1
    if max - min != j-i:
        return False

    visited = [False] * (j-i+1)  #created a visited list

    #check if element occurs only once
    for k in range(i,j+1):
        if visited[arr[k] - min]:
            return False   #if the element is seen before, return False

        visited[arr[k] - min] = True

    return True #point where all the elements are distinct

def findMax(arr):
    length = 1
    start = end = 0
    for i in range(len(arr) - 1):
        min_val = arr[i]
        max_val = arr[i]

        for j in range(i+1,len(arr)):
            min_val = min(min_val,arr[j])
            max_val = max(max_val,arr[j])

            if consec_elem(arr,i,j,min_val,max_val):   #checking if arr[i..j] is formed by consecutive integers
                if length < max_val - min_val + 1:
                    length = max_val - min_val + 1
                    start = i
                    end = j

    print("Largest sublist is: ",(start,end))





if __name__ == "__main__":
    arr = [2,0,2,1,4,3,1,0]
    print(findMax(arr))
