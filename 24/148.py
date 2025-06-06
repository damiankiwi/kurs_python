class node():
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def insert(self, val):
        if self.val:
            if val < self.val:
                if self.left is None:
                    self.left = node(val)
                else:
                    self.left.insert(val)
            elif val > self.val:
                if self.right is None:
                    self.right = node(val)
                else:
                    self.right.insert(val)
        else:
            self.val = val

def inorder(root, res):
    if root:
        inorder(root.left, res)
        res.append(root.val)
        inorder(root.right, res)

def treesort(arr):
    if len(arr) == 0:
        return arr
    root = node(arr[0])
    for i in range(1, len(arr)):
        root.insert(arr[i])
    res = []
    inorder(root, res)
    return res

print(treesort([7, 1, 5, 2, 19, 14, 17]))