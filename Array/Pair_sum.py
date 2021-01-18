#naive approach to find a pair in the list with the given sum

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
