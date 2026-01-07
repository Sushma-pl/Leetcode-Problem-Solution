class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n1, n2 = len(nums1), len(nums2)
        if n1 > n2:
            a, b = nums2, nums1

        else:
            a, b = nums1, nums2
        n1,n2 = min(n1,n2), max(n1,n2)

        l, r= 0, len(a)
        total =( n1+n2+1)//2
        
        
        # check the valid division of element in to left and right half
        while l <= r:
            mid1 = (l+r)//2
            mid2 = total-mid1

            l1,l2 = -sys.maxsize, -sys.maxsize
            r1,r2 = sys.maxsize, sys.maxsize

            if mid1-1 >=0 :
                l1 = a[mid1-1]
            if mid2-1>=0:
                l2 = b[mid2-1]

            
            if mid1 < n1:
                r1 = a[mid1]
            if mid2 < n2:
                r2 = b[mid2]
            
            if l1 <= r2 and l2 <= r1:
                if (n1+n2)&1:
                    return max(l1,l2)
                else:
                    return (max(l1,l2)+min(r1,r2))/2
            elif l1 > r2:
                r = mid1-1
            else:
                l = mid1+1
        return 0.0