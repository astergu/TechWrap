class SelectionSort(object):
    def sort(self, nums):
        for i in xrange(len(nums)):
            min_idx = i
            for j in xrange(i + 1, len(nums)):
                if nums[j] < nums[min_idx]:
                    min_idx = j
            nums[min_idx], nums[i] = nums[i], nums[min_idx]

if __name__ == '__main__':
    nums = [64, 25, 12, 22, 11]
    ss = SelectionSort()
    ss.sort(nums)
    print nums
