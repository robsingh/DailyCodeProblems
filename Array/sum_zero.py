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

#second approach

#function to insert key,value pair into the dictionary
def insert(dict,key,value):
    dict.setdefault(key,[]).append(value) #if the key is seen for the first time, initialize the list

#function to print all sublists with zero sum
def printSubLists(arr):
    dict = {} #empty dictionary to store the ending index of all sublists having the same sum
    insert(dict,0,-1) #case when sublist with zero sum starts from index 0
    sum = 0
    for i in range(len(arr)):
        sum += arr[i] #sum of elements
        if sum in dict:
            list = dict.get(sum)
            for value in list:
                print("Sublist is: ",(value+1,i))

        insert(dict,sum,i) #inserting (sum so far, index) into the dictionary

if __name__ == "__main__":
    arr = [3,4,-7,3,1,3,1,-4,-2,-2]
    printSubLists(arr)

