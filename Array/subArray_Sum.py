#Check if array contains a sub-array having sum=0

def check_Array(arr):
  #create an empty set to store sum of elements of each sublist where 0 <= i < len(arr)
  s = set()
  s.add(0) #inserting zero to handle the case when sublist with 0 sum starts from index 0
  sum = 0
  for i in arr:
    sum += i
    if sum in s:
      return True
    s.add(sum)
    
  return False

if __name__ == "__main__":
  arr = [6,3,-1,-3,4,-2,2,4,6,-12,7]
  if check_Array(arr):
    print("Sublist exists")
  else:
    print("Sublist does not exists!!")
