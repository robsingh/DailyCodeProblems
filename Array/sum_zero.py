#given an integer array, print all subarrays with zero-sum
#naive approach to solve this problem with time complexity O(n^3) 

def printAllSublist(arr):
    for i in range(len(arr)):
        sum = 0
        for j in range(i,len(arr)):
            sum += arr[j]
            if sum == 0:
                print("Sublist: ",(i,j))

if __name__ == "__main__":
    arr = [3, 4, -7, 3, 1, 3, 1, -4, -2, -2]
    printAllSublist(arr)

#second approach, using multimap to print all subarrays
