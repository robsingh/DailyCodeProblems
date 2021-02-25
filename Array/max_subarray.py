#function to find max length sublist having an equal number of 0's and 1's

def findMaxLenSub(arr):
    dict = {}
    dict[0] = -1 #case when sublist with zero sum starts from index 0
    length = 0 #stores max length
    end_index = 1
    sum = 0
    for i in range(len(arr)):
        sum += -1 if (arr[i] == 0) else 1  #sum of elements (replace 0 with -1)

        if sum in dict:
            if length < i - dict.get(sum):   #update length and end index
                length = i - dict.get(sum)
                ending_index = i

        else:
            dict[sum] = i

    if ending_index != -1:
        print((ending_index - length + 1,ending_index))
    else:
        print("No sublist exists")



if __name__ == "__main__":
    # arr = [1,0,1,1,0,1,1,1,0,0]
    arr = [0,0,1,0,1,0,0]
    findMaxLenSub(arr)

#time complexity - O(n)
