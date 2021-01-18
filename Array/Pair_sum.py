#naive approach to find a pair in the list with the given sum
#not an ideal solution, gives time complexity of o(n^2), auxillary space used by this program is O(1)

def findPair(arr,sum):
  #consider each element except the last
  for i in range(len(arr) - 1):
    #start from i'th element till the last element
    for j in range(i+1,len(arr)):
      #if desired sum is found, print it and return 
      if arr[i] + arr[j] == sum:
        print("Pair found at index",i,"and",j)
        return 
      
  print("No Pair found!!!")
  
  if __name__ == "__main__":
    arr = [2,5,7,8,7]
    sum = 10
    findPair(arr,sum)
    

# O(nlog(n)) using Sorting:
def findPair(arr,sum):
  arr.sort() #sorting the list in ascending order
  
  (low,high) = (0,len(arr)-1) #two indices pointing to end-points of list
  #loop till search space is exhausted
  while low < high:
    if arr[low] + arr[high] == sum:
      print("Pair found at index",low,"and",high)    #index in the sorted array
      return 
    if arr[low] + arr[high] < sum:
      low += 1
    else:
      high -= 1
      
      
  print("No pair found!")
  
if __name__ == "__main__":
  arr = [8,7,2,5,3,1]
  sum = 10
  findPair(arr,sum)
