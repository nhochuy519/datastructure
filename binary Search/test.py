
def binarySearch(arr:list[int],target:int) -> int:
    arr = sorted(arr)
    left=0
    right=len(arr)-1
    print(arr)
    while left<=right:
        # mid = (left+right)//2
        mid = left + (right-left)//2
        if arr[mid] == target:
            return mid;
        elif target > arr[mid]:
            left = mid +1
        else :
            right = mid -1
    return -1



print(binarySearch([1,7,2,6,2,1,5,1,1000,23,21,17],1))

#[1,2,3,4,5,6]



def condition_based_binary_search(arr, target):
    left, right = 0, len(arr) - 1
    result = -1
    
    while left <= right:
        mid = left + (right - left) // 2
        
        # Điều kiện tùy chỉnh: tìm phần tử đầu tiên >= target
        if arr[mid] <= target:
            result = mid
              # Tìm về bên trái
            left = mid + 1 
        else:
            # Tìm về bên phải
            right = mid - 1
    
    return result

print(condition_based_binary_search([1,2,3,3,4,5],target=3))