# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        q=deque()
        q.append(root)
        val = root.val
        ans = 1
        level = 1
        while q:
            temp = 0
            s = len(q)
            
            for i in range(s):
                node = q.popleft()
                temp += node.val
                if node.left:
                    q.append(node.left)
                    # temp+= node.left.val
                
                if node.right:
                    q.append(node.right)
                    # temp+=node.right.val
            
            # print("level sum:" , temp, level)
            if temp > val:
                val = temp
                ans = level
            level +=1

            # print("ans level and sum: ",ans, val)
        
        # if val < 0:
        #     return ans+1
        return ans