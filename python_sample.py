# BinarySearchTree sample code 

class BST:
    def __init__(self,root,left,right):
        self.root = root
        self.left = left
        self.right = right

    def __eq__(self, other):
        if other == None:
            return False
        else:
            return self.root == other.root and self.left == other.left and self.right == other.right

class BinarySearchTree:
    def __init__(self,BST,comes_before):
        self.BST = BST
        self.comes_before = comes_before

    def __eq__(self, other):
        if other == None:
            return False
        else:
            return self.BST == other.BST and self.comes_before == other.comes_before

# Returns True if empty, and false otherwise
def is_empty(inputBST):
    if inputBST.BST == None:
        return True
    else:
        return False

def insert(inputTree,value):
    if inputTree == None:
        raise IndexError

    if inputTree.BST == None:
        return BinarySearchTree(BST(value,None,None),inputTree.comes_before)
    else:
        if inputTree.comes_before(value,inputTree.BST.root):
            if inputTree.BST.left != None:
                return BinarySearchTree(BST(inputTree.BST.root, insert(BinarySearchTree(inputTree.BST.left,inputTree.comes_before), value),inputTree.BST.right),inputTree.comes_before)
            else:
                temp = inputTree.BST.left
                inputTree.BST.left = value
                inputTree.BST.root = inputTree.BST.left
                inputTree.BST.root = temp
            return inputTree
        else:
            if inputTree.BST.right != None: #has children nodes
                tempBST = BST(inputTree.BST.root, inputTree.BST.right, insert(BinarySearchTree(inputTree.BST.right,inputTree.comes_before),value))
                return BinarySearchTree(tempBST,inputTree.comes_before)
            else: #no children nodes
                inputTree.BST.right = BST(value,None,None)
    return inputTree
#
# def lookup(inputTree,value):
#     if inputTree == None:
#         return BinarySearchTree(BST(None,None,None),comes_before=print_function)
#     else:
#         if inputTree.comes_before(value,inputTree.BST.root):
#             return lookup(inputTree.BST.left,value)
#         elif inputTree.comes_before(inputTree.BST.root,value):
#             return lookup(inputTree.BST.right.value)
#         else:
#             return True

# def delete(inputTree,value):
#     itExists = lookup(inputTree,value) #Checks to see whether the value is inside the given tree at all
#     if itExists is False:
#         return inputTree
#     else:
#         if inputTree.comes_before(value,inputTree.BST.root): #left
#             return delete(inputTree)
