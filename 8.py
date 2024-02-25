class Solution:
    def merge_plus_count(self, nums, left, middle, right):
        left_arr = nums[left:middle]
        right_arr = nums[middle:right]
        length_l = len(left_arr)
        length_r = len(right_arr)
        i, j, k = 0, 0, left
        count = 0

        while i < length_l and j < length_r:
            if left_arr[i] <= right_arr[j]:
                nums[k] = left_arr[i]
                i += 1
            else:
                nums[k] = right_arr[j]
                j += 1
                count += middle - i - left
            k += 1

        while i < length_l:
            nums[k] = left_arr[i]
            i += 1
            k += 1

        while j < length_r:
            nums[k] = right_arr[j]
            j += 1
            k += 1

        return count

    def globalInversionCount(self, nums, left, right):
        count = 0

        if right - left - 1 != 0:
            middle = (left + right) // 2

            count += self.globalInversionCount(nums, left, middle)
            count += self.globalInversionCount(nums, middle, right)
            count += self.merge_plus_count(nums, left, middle, right)

        return count

    def localInversionCount(self, nums, length):
        count = 0
        for i in range(1, length):
            if nums[i - 1] > nums[i]:
                count += 1
        return count

    def isIdealPermutation(self, nums: List[int]) -> bool:
        length = len(nums)

        loc_inv = self.localInversionCount(nums, length)
        glob_inv = self.globalInversionCount(nums, 0, length)

        return loc_inv == glob_inv


#Простое решение
class Solution:
    def isIdealPermutation(self, A: List[int]) -> bool:
        for i in range(len(A)):
            if abs(A[i] - i) > 1: return False
        return True
