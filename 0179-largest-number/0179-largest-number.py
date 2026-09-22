class Solution:
    def largestNumber(self, nums: list[int]) -> str:
        lst = []
        for num in nums:
            lst.append(str(num))

        def merge_sort(arr):

            if len(arr) <= 1:
                return arr

            mid = len(arr) // 2

            left = merge_sort(arr[:mid])
            right = merge_sort(arr[mid:])

            return merge(left, right)

        def merge(left, right):
            result = []

            i = 0
            j = 0

            while i < len(left) and j < len(right):

                if left[i] + right[j] >= right[j] + left[i]:
                    result.append(left[i])
                    i += 1
                else:
                    result.append(right[j])
                    j += 1

            while i < len(left):
                result.append(left[i])
                i += 1

            while j < len(right):
                result.append(right[j])
                j += 1

            return result

        lst = merge_sort(lst)

        if lst[0] == "0":
            return "0"

        return ''.join(lst)
