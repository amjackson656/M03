#User function template for Python

class Solution:
    def binarysearch(self, arr, N, K):
        low = 0
        high = N - 1

        while low <= high:
            mid = low + (high - low) // 2

            if arr[mid] == K:
                return mid
            elif arr[mid] < K:
                low = mid + 1
            else:
                high = mid - 1

        return -1

# Create a Solution object
s = Solution()

# Define the array, its size, and the value to find
N = 5
arr = [1, 2, 3, 4, 5]
K = 4

# Perform the binary search
print(s.binarysearch(arr, N, K))
