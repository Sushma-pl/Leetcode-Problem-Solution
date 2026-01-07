# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        ans = []
        totalsum = 0
        def findsum(node):
            if node is None:
                return 0
            
            return node.val + findsum(node.left) + findsum(node.right)

        def dfs(node,ts):
            if node is None:
                return 0
            
            s = node.val
            l = dfs(node.left,ts)
            r = dfs(node.right,ts)

            # two way to break on edge
            t1 = l* (ts-l)
            t2 =  (ts-r)* (r)

            if len(ans) ==0:
                ans.append(t1)
            else:
                ans[-1] = max(ans[-1], t1)
            ans[-1] = max(ans[-1], t2)

            return s+l+r
         
        totalsum = findsum(root)
        # print(totalsum, root.val)
        temp = dfs(root,totalsum)
        # maxp = max(ans)
        return ans[0]%(10**9 + 7)