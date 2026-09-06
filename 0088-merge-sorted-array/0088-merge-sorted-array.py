class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        a = m - 1
        b = n - 1
        c = m + n - 1
        # using 3 pointers we saw last element of nums1 as c , m = 3 as largest of nums1 and n = 3 as largest of nums2

        while a >= 0  and b >= 0:

            if nums1[a] > nums2[b]:
                nums1[c] = nums1[a]
                a-=1
            else:
                nums1[c] = nums2[b]
                b-=1
            c-=1
        
        # if nums2 array is still there add all in nums1
        while b >= 0:
            nums1[c] = nums2[b]
            b-=1
            c-=1