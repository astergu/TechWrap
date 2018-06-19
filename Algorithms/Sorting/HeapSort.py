class HeapSort(object):

    def sort(self, nums):
        self.build_heap(nums)
        for i in xrange(len(nums) - 1, -1, -1):
            nums[i], nums[0] = nums[0], nums[i]
            self.heapify(nums, i, 0)

    def build_heap(self, nums):
        for i in xrange(len(nums) / 2, -1, -1):
            self.heapify(nums, len(nums), i)

    def heapify(self, nums, n, i):
        l, r = 2 * i + 1, 2 * i + 2
        largest = i
        if l < n and nums[l] > nums[i]:
            largest = l
        if r < n and nums[r] > nums[largest]:
            largest = r
        if largest != i:
            nums[i], nums[largest] = nums[largest], nums[i]
            self.heapify(nums, n, largest)


if __name__ == '__main__':
    nums = [4, 10, 3, 5, 1]
    hp = HeapSort()
    hp.sort(nums)
    print nums
