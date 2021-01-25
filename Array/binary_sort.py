#Given a binary array, sort it in linear time and constant space. The output should print all zeroes followed by all ones.
#time complexity id O(n)

def sort(arr):
  k = 0 #stores index of next available position
  
  for i in range(len(arr)):    #if the current element is zero, put 0 to the next free position
    if arr[i] == 0:
      arr[k] = 1
      k += 1
      
  for i in range(k,len(arr)):
    arr[k] = 1  #arr[k] = 0, if you want to print 1 in the beginning
    k += 1
   
if __name__ == "__main__":
  arr = [0,1,1,0,0,1,0,1,0]
  sort(arr)
  print(arr)
  
 
