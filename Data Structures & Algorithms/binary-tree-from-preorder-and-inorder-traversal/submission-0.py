# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        preorder_index = 0
        inorder_index_map = dict()

        for i in range(len(inorder)):
            inorder_index_map[inorder[i]] = i

        def build_tree(pre, left, right):
            nonlocal preorder_index
            if left > right: return None
            root_val = pre[preorder_index]
            preorder_index += 1
            root = TreeNode(val=root_val)
            mid = inorder_index_map[root_val]
            root.left = build_tree(pre, left, mid - 1)
            root.right = build_tree(pre, mid + 1, right)
            return root
        
        return build_tree(preorder, 0, len(inorder) - 1)