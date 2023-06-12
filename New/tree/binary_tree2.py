from abc import ABC,abstractclassmethod
# interface class
class Binary_tree_interface(ABC):
    '''
    This is the interface class for binary_search
    '''
    @abstractclassmethod
    def binary_tree(val):
        pass
    @abstractclassmethod
    def set_root_val(val):
        pass
    @abstractclassmethod
    def get_root_val(val):
        pass
    @abstractclassmethod
    def get_left_child(self):
        pass
    @abstractclassmethod
    def get_right_child(self):
        pass
    @abstractclassmethod
    def insert_left_child(self):
        pass
    @abstractclassmethod
    def insert_right_child(self):
        pass

class Binary_tree_concret(Binary_tree_interface):
    def __init__(self,val):
        self.tree=Binary_tree_concret.binary_tree(val)
    def binary_tree(val):
        root=Node(5)
        return root
    def set_root_val(root,new_val):
        root.val=new_val
    def get_root_val(root):
        return root.val
    def get_left_child(root):
        return root.left
    def get_right_child(root):
        return root.right
    def insert_left_child(root,val):
        if root.left==None:
            root.left=Binary_tree_concret.binary_tree(val)  
        else:
            t=Binary_tree_concret.binary_tree(val)
            t.left=root.left
            root.left=t    
    def insert_right_child(root,val):
        if root.right==None:
            root.right=Binary_tree_concret.binary_tree(val)  
        else:
            t=Binary_tree_concret.binary_tree(val)
            t.right=root.right
            root.right=t    

class Node:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None



t=Binary_tree_concret(5)
Binary_tree_concret.insert_left_child(t.tree, 6)
print(t.tree.val)
print(t.tree.left.val)


