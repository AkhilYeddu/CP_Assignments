def marrays(arr1, arr2):
    merged_array=[]
    i=0
    j=0

    while i<len(arr1) and j<len(arr2):
        if arr1[i] < arr2[j]:
            merged_array.append(arr1[i])
            i += 1
        else:
            merged_array.append(arr2[j])
            j += 1

    while i<len(arr1):
        merged_array.append(arr1[i])
        i += 1

    while j<len(arr2):
        merged_array.append(arr2[j])
        j += 1

    return merged_array


arr1_size = int(input())
arr1 = list(map(int, input().split()))
arr2_size = int(input())
arr2 = list(map(int, input().split()))

merged_array = marrays(arr1, arr2)
for num in merged_array:
    print(num, end=" ")