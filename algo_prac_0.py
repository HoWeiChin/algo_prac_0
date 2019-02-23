print('hello world')

#returns the index of the target number
#return -1 if target number is not found

def binary_search_iter(target, sorted_arr):
    start = 0
    end = len(sorted_arr) - 1

    while start <= end:
        mid = (start + end)//2
        middle = sorted_arr[mid]

        if target < middle:
            end = mid - 1
        if target > middle:
            start = mid + 1
        if target == middle:
            return mid

    return -1

#binary search recursive
def binary_search_recursive(target, arr, start, end):
    mid = (start + end)//2
    if target == arr[mid]:
        return mid
    if start > end:
        return -1
    if target < arr[mid]:
        return binary_search_recursive(target, arr, start, mid-1)
    return binary_search_recursive(target,arr, mid + 1, end)

def find_window(arr):
    slow = 0
    fast = 2
    while arr[fast] != 0:
        print(arr[fast])
        slow = fast
        fast = fast * 2
    return (slow,fast)

def binary_search_in_window(arr, tup):
    start,end = tup
    while start != end :
        mid = (start + end) //2

        if arr[mid] != 0:
            start = mid + 1
        if arr[mid] == 0:
            end = mid
    return end
        



if __name__ == "__main__":
    arr = [1,4,5,2,7,8,9,10,11,0,0,0,0,0,0,0,0]
    #print(binary_search_recursive(0,arr,0, len(arr)-1))
    tup = find_window(arr)
    print(tup)
    print(binary_search_in_window(arr, tup))


