# K DISTINCT SUB-LISTS
# ARYAN B13 29

def atMostK(arr, n, k):
    count = 0
    left = 0
    right = 0
    map = {}
    while right < n:
        if arr[right] not in map:
            map[arr[right]] = 0
        map[arr[right]] += 1
        while (len(map) > k):
            if arr[left] not in map:
                map[arr[left]] = 0
            map[arr[left]] -= 1
            if map[arr[left]] == 0:
                del map[arr[left]]
            left += 1
        count += right - left + 1
        right += 1
    return count


def exactlyK(arr, n, k):
    return (atMostK(arr, n, k) -
            atMostK(arr, n, k - 1))


n = int(input("Enter number of elements : "))
a = list(map(int, input("\nEnter the numbers : ").strip().split()))[:n]
k = int(input("Enter the value of k : "))
print(exactlyK(a, n, k))
