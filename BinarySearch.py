def BinarySearch(numbers,target):
    low=0
    high=len(numbers)-1
    print("lower bound index : ",low)
    print("upper bound index :",high)
    
    
    while low<=high:
        mid=(low+high)//2
        if numbers[mid]==target:
            return mid
        elif numbers[mid]>target:
            high=mid-1
            print("lower bound index :",low)
            print("upper bound index :",high)
        else:
            low=mid+1
            print("lower bound index : ",low)
            print("upper bound index: ",high)
    return -1           


numbers=[11,24,35,56,67,78,86,99,102,124,153]
target=153
if target in numbers:
    print("number is present.")
    print("**********")
    res=BinarySearch(numbers,target)
    print("number found at index",res)
    print("**********")
else:
    print("number not present.")    
   


