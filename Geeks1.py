#User function Template for python3

class Solution:
    def sort012(self,arr,n):
        low = 0
        mid = 0
        high = n - 1

        while mid <= high:
            if arr[mid] == 0:
                arr[low], arr[mid] = arr[mid], arr[low]
                low += 1
                mid += 1
            elif arr[mid] == 1:
                mid += 1
            else:
                arr[mid], arr[high] = arr[high], arr[mid]
                high -= 1
        return arr

# Create a Solution object
s = Solution()

# Define the array and its size
N = 5
arr = [1, 2, 0, 0, 2]

# Sort the array
# print(str(s.sort012(arr, N))) this produced brackets in output but not on the website

# Sort the array
sorted_arr = s.sort012(arr, N)

# Print the sorted array elements without brackets
print(' '.join(map(str, sorted_arr)))